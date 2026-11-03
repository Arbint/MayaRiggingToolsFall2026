from mayaRiggingTools.core.mayaWidget import QMayaWidget

class LimbRiggerWidget(QMayaWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Limb Rigger")

LimbRiggerWidget().show()