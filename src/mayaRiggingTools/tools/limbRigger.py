from mayaRiggingTools.core.mayaWidget import QMayaWidget
from mayaRiggingTools.core.mayaUtilities import GetParent
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
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


    def RigLimb(self):
        print("rigging")


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
        jntSelectionLineEdit = QLineEdit()
        jntSelectionLineEdit.setReadOnly(True)
        jntInfoLayout.addWidget(jntSelectionLineEdit)
        collectJntNameBtn = QPushButton("<<<") 
        collectJntNameBtn.clicked.connect(self.CollectJntNameBtnClicked)
        jntInfoLayout.addWidget(collectJntNameBtn)

        rigInfoLayout = QHBoxLayout()
        masterLayout.addLayout(rigInfoLayout)
        rigInfoLayout.addWidget(QLabel("name base:"))
        nameBaseLineEdit = QLineEdit()
        rigInfoLayout.addWidget(nameBaseLineEdit)

        rigBtn = QPushButton("Rig Limb")
        masterLayout.addWidget(rigBtn)

    def CollectJntNameBtnClicked(self):
        try:
            self.rigger.CollectSelectionAsJnts()
        except LimbRiggerException as e:
            QMessageBox.critical(self, "Failed to collection Joints", f"{e}") 

    def GetWidgetHash(self):
        return "72cba722687f9cb48774bc8ebc699d9004f6839e76fe1ce1fdc5f7dd89454ecc"

LimbRiggerWidget().show()