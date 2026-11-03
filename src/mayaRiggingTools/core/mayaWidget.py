import maya.cmds as mc
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Qt

import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

def GetMayaMainWindow()->QMainWindow:
    mayaMainWindow = omui.MQtUtil.mainWindow()
    # mayaMainWindow is a low C++ object, we convert it to an int to get it's address, and then convert to python QMainWindow
    return wrapInstance(int(mayaMainWindow), QMainWindow)

def RemoveWidgetWithHash(hashName):
    for widget in GetMayaMainWindow().findChildren(QWidget, hashName):
        # close the window
        widget.deleteLater()

# creates a class called QMayaWidget that is based on QWidget
class QMayaWidget(QWidget):
    def __init__(self):
        super().__init__(parent = GetMayaMainWindow())
        # remove any existing widget tha has the hash name
        RemoveWidgetWithHash(self.GetWidgetHash())

        # give every new instance of this widget the same widget hash as their name
        self.setObjectName(self.GetWidgetHash())
        self.setWindowFlags(Qt.WindowType.Window)

    # a hash is a globally unique id 
    def GetWidgetHash(self):
        return "62cba722687f9cb48774bc8ebc699d9004f6839e76fe1ce1fdc5f7dd89454ecb"
    
