import importlib
import mayaRiggingTools.core.mayaUtilities
importlib.reload(mayaRiggingTools.core.mayaUtilities)

from mayaRiggingTools.core.mayaWidget import QMayaWidget
from mayaRiggingTools.core.mayaUtilities import GetParent, CreateFKCircleControllerForJnt, CreateIkBoxControllerForJnt, CreatePlus
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator

import maya.cmds as mc

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

        ikfkBlendCtrl = CreatePlus(self.nameBase + "_ikfk_blend")


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