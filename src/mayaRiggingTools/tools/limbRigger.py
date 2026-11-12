import importlib
import mayaRiggingTools.core.mayaUtilities
importlib.reload(mayaRiggingTools.core.mayaUtilities)

from mayaRiggingTools.core.mayaWidget import QMayaWidget
from mayaRiggingTools.core.mayaUtilities import (GetParent,
                                                CreateFKCircleControllerForJnt,
                                                CreateIkBoxControllerForJnt,
                                                CreatePlus,
                                                GetPosAsMVec,
                                                PrintVec,
                                                SetPosToMVec
                                                )
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator

import maya.cmds as mc
from maya.OpenMaya import MVector

class LimbRiggerException(Exception):
    pass

class LimbRigger:
    def __init__(self):
        self.nameBase = None
        self.rootJnt = None
        self.midJnt = None
        self.endJnt = None

    def CollectSelectionAsJnts(self):
        selection = mc.ls(sl=True)
        if not selection or len(selection) != 3: 
            raise LimbRiggerException(f"{selection} is the wrong selection, please select the root, midle, and end joint of the limb")

        for selected in selection:
            if mc.objectType(selected) != "joint":
                raise LimbRiggerException(f"{selected} is not a joint, please select the root, midle, and end joint of the limb")

        if GetParent(selection[2]) != selection[1] or GetParent(selection[1]) != selection[0]:
            raise LimbRiggerException(f"seleted joints are not a limb chain: {selection}")

        self.rootJnt = selection[0]
        self.midJnt = selection[1]
        self.endJnt = selection[2]


    def RigLimb(self):
        endCtrl, endCtrlGrp = CreateFKCircleControllerForJnt(self.endJnt)
        midCtrl, midCtrlGrp = CreateFKCircleControllerForJnt(self.midJnt)
        rootCtrl, rootCtrlGrp = CreateFKCircleControllerForJnt(self.rootJnt)

        # make the fk work.
        mc.parent(endCtrlGrp, midCtrl)
        mc.parent(midCtrlGrp, rootCtrl)

        ikEndCtrl, ikEndCtrlGrp = CreateIkBoxControllerForJnt(self.endJnt)


        ikHandleName = f"ikHandle_{self.nameBase}"
        mc.ikHandle(n=ikHandleName, sj=self.rootJnt, ee=self.endJnt, sol="ikRPsolver")

        rootJntPos = GetPosAsMVec(self.rootJnt)
        endJntPos = GetPosAsMVec(self.endJnt)
        poleVectorValues = mc.getAttr(f"{ikHandleName}.poleVector")[0]
        poleVector = MVector(poleVectorValues[0], poleVectorValues[1], poleVectorValues[2])
        poleVector.normalize()

        PrintVec(rootJntPos)
        PrintVec(endJntPos)
        PrintVec(poleVector)

        rootToEndVec: MVector = endJntPos - rootJntPos
        limbLength = rootToEndVec.length()

        poleVectorCtrlPos = rootJntPos + rootToEndVec/2.0 + poleVector * limbLength

        ikMidCtrl = f"ac_ik_{self.midJnt}"
        mc.spaceLocator(n=ikMidCtrl)

        ikMidCtrlGrp = f"{ikMidCtrl}_grp"
        mc.group(ikMidCtrl, n=ikMidCtrlGrp)

        SetPosToMVec(ikMidCtrlGrp, poleVectorCtrlPos)
        mc.poleVectorConstraint(ikMidCtrl, ikHandleName)

        mc.parent(ikHandleName, ikEndCtrl)

        ikfkBlendCtrl = CreatePlus(self.nameBase + "_ikfk_blend", 1)
        ikfkBlendCtrlGrp = f"{ikfkBlendCtrl}_grp"
        mc.group(ikfkBlendCtrl, n=ikfkBlendCtrlGrp)
        ikfkBlendPos = rootJntPos + MVector(rootJntPos.x, 0, 0)
        SetPosToMVec(ikfkBlendCtrlGrp, ikfkBlendPos)

        ikfkBlendAttrName = "ikfk_blend"
        mc.addAttr(ikfkBlendCtrl, ln=ikfkBlendAttrName, k=True, min=0, max=1, at="double")
        ikfkBlendAttr = f"{ikfkBlendCtrl}.{ikfkBlendAttrName}"

        mc.setAttr(f"{ikfkBlendCtrl}.tx", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.ty", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.tz", lock=True, channelBox=False, k=False)

        mc.setAttr(f"{ikfkBlendCtrl}.sx", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.sy", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.sz", lock=True, channelBox=False, k=False)

        mc.setAttr(f"{ikfkBlendCtrl}.rx", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.ry", lock=True, channelBox=False, k=False)
        mc.setAttr(f"{ikfkBlendCtrl}.rz", lock=True, channelBox=False, k=False)

        mc.setAttr(f"{ikfkBlendCtrl}.v", lock=True, channelBox=False, k=False)

        endOrientConstraint = mc.orientConstraint(ikEndCtrl, self.endJnt)[0]

        mc.expression(s=f"{ikHandleName}.ikBlend={ikfkBlendAttr};")
        mc.expression(s=f"{ikEndCtrlGrp}.v={ikfkBlendAttr};")
        mc.expression(s=f"{ikMidCtrlGrp}.v={ikfkBlendAttr};")

        # finish the rest of the rig:
        # 1, control the fk visibility with expression, you only need one line to do this
        # 2, control the ikfk blend for the wrist rotation with expression, should be 2 lines, each controls one of the weight on the orient constraint
        # 3, group everything into a group with the name self.nameBase+"_rig_grp"
        


class LimbRiggerWidget(QMayaWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Limb Rigger")

        self.rigger = LimbRigger()

        masterLayout = QVBoxLayout() 
        self.setLayout(masterLayout)

        masterLayout.addWidget(QLabel("Please Select the root, middle, and end joint of the limb:"))

        jntInfoLayout = QHBoxLayout()
        masterLayout.addLayout(jntInfoLayout)
        jntInfoLayout.addWidget(QLabel("Joints:"))
        self.jntSelectionLineEdit = QLineEdit()
        self.jntSelectionLineEdit.setReadOnly(True)
        jntInfoLayout.addWidget(self.jntSelectionLineEdit)
        collectJntNameBtn = QPushButton("<<<") 
        collectJntNameBtn.clicked.connect(self.CollectJntNameBtnClicked)
        jntInfoLayout.addWidget(collectJntNameBtn)

        rigInfoLayout = QHBoxLayout()
        masterLayout.addLayout(rigInfoLayout)
        rigInfoLayout.addWidget(QLabel("name base:"))
        self.nameBaseLineEdit = QLineEdit()
        self.nameBaseLineEdit.setValidator(QRegularExpressionValidator("[a-zA-Z_]+[0-9]*"))
        rigInfoLayout.addWidget(self.nameBaseLineEdit)

        rigBtn = QPushButton("Rig Limb")
        rigBtn.clicked.connect(self.RigBtnClicked)
        masterLayout.addWidget(rigBtn)

    def RigBtnClicked(self):
        try:
            self.rigger.nameBase = self.nameBaseLineEdit.text()
            self.rigger.RigLimb()
        except LimbRiggerException as e:
            QMessageBox.critical(self, "Failed to rig the limb", f"{e}") 


    def CollectJntNameBtnClicked(self):
        try:
            self.rigger.CollectSelectionAsJnts()
            self.jntSelectionLineEdit.setText(f"{self.rigger.rootJnt},{self.rigger.midJnt},{self.rigger.endJnt}")
        except LimbRiggerException as e:
            QMessageBox.critical(self, "Failed to collection Joints", f"{e}") 

    def GetWidgetHash(self):
        return "72cba722687f9cb48774bc8ebc699d9004f6839e76fe1ce1fdc5f7dd89454ecc"

LimbRiggerWidget().show()