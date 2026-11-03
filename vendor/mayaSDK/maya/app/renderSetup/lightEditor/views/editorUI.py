from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QBoxLayout
from maya.app.renderSetup.views.renderSetupStyle import RenderSetupStyle
from PySide6.QtCore import QPersistentModelIndex
from PySide6.QtCore import Signal
from functools import partial
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QMimeData
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QToolTip
from PySide6.QtCore import QEvent
from PySide6.QtCore import QObject
from PySide6.QtCore import Slot
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPen
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame
from maya.app.renderSetup.views.renderSetupButton import RenderSetupButton
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QGroupBox
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from maya.app.renderSetup.views.propertyEditor.layout import Layout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QTreeView
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLayoutItem
from maya.app.renderSetup.lightEditor.views.delegate import LightEditorDelegate
from PySide6.QtWidgets import QMenuBar
from PySide6.QtCore import QThread

class LookThroughWindow(MayaQWidgetDockableMixin, QWidget):
    """
    This class implements the look through window.
    """
    
    
    
    def __del__(self):
        """
        This is a workaround for a runtime error raised when the window is closed.
        'Internal C++ object (LookThroughWindow) already deleted.
        See MAYA-82966 for details.
        """
    
        pass
    
    
    def __init__(self, parent):
        pass
    
    
    def closeEvent(self, event):
        pass
    
    
    def lookThroughLight(self, light):
        """
        Opens a model panel with camera looking through the given light.
        """
    
        pass
    
    
    def minimumSizeHint(self):
        pass
    
    
    def setSizeHint(self, size):
        pass
    
    
    def sizeHint(self):
        pass
    
    
    MINIMUM_SIZE = None
    
    
    PREFERRED_SIZE = None
    
    
    STARTING_SIZE = None
    
    
    staticMetaObject = None


class LightEditorCentralWidget(QWidget):
    """
    This class implements the controls inside the light editor window
    """
    
    
    
    def __init__(self, parent):
        pass
    
    
    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
    
        pass
    
    
    def getLightCreator(self, lightType):
        pass
    
    
    def lookThroughWindowDestroyed(self):
        pass
    
    
    def minimumSizeHint(self):
        pass
    
    
    def newGroup(*args, **kwargs):
        pass
    
    
    def newLight(*args, **kwargs):
        pass
    
    
    def propertyEditorWindowDestroyed(self):
        pass
    
    
    def renderSetupAdded(self):
        pass
    
    
    def renderSetupPreDelete(self):
        pass
    
    
    def saveLookThroughWindowState(self):
        pass
    
    
    def savePropertyEditorWindowState(self):
        pass
    
    
    def selectionChanged(self):
        pass
    
    
    def sizeHint(self):
        pass
    
    
    BUTTON_SIZE = 40.0
    
    
    MINIMUM_SIZE = None
    
    
    PREFERRED_SIZE = None
    
    
    staticMetaObject = None


class LightEditorView(QTreeView):
    """
    This class implements the light editor view.
    """
    
    
    
    def __init__(self, parent):
        pass
    
    
    def dispose(self):
        pass
    
    
    def eventFilter(self, object, event):
        pass
    
    
    def leaveEvent(self, *args, **kwargs):
        pass
    
    
    def mouseDoubleClickEvent(self, event):
        pass
    
    
    def mouseMoveEvent(self, event):
        pass
    
    
    def mousePressEvent(self, event):
        pass
    
    
    def mouseReleaseEvent(self, event):
        pass
    
    
    def paintEvent(self, e):
        """
        Overrides the paint event to make it so that place holder text is displayed when the list is empty.
        """
    
        pass
    
    
    def refreshView(self):
        pass
    
    
    def rowsInserted(self, parent, start, end):
        pass
    
    
    def setExpanded(self, index, state):
        """
        Override from the Qt class
        Expands the group and saves its state
        """
    
        pass
    
    
    def showContextMenu(self, point):
        """
        Rebuild from scratch the context menu
        """
    
        pass
    
    
    HALF_FONT_HEIGHT = 14.0
    
    
    NO_LIGHTS_IMAGE_SIZE = 124.0
    
    
    PLACEHOLDER_TEXT_PEN = None
    
    
    staticMetaObject = None


class LightEditorWindow(MayaQWidgetDockableMixin, QWidget):
    """
    This class implements the dockable light editor window.
    """
    
    
    
    def __init__(self):
        pass
    
    
    def dispose(self):
        pass
    
    
    def minimumSizeHint(self):
        pass
    
    
    def setSizeHint(self, size):
        pass
    
    
    def show(self, *args, **kwargs):
        pass
    
    
    def sizeHint(self):
        pass
    
    
    MINIMUM_SIZE = None
    
    
    PREFERRED_SIZE = None
    
    
    STARTING_SIZE = None
    
    
    staticMetaObject = None
    
    
    width = 600



def getCppPointer(*args, **kwargs):
    pass


def lightEditorWindowChanged():
    pass


def lightEditorWindowClosed():
    pass


def createLightEditorWindow(restore='False'):
    """
    # Sets up the light editor main window
    """

    pass


def lightEditorWindowDestroyed(object='None'):
    pass


def saveWindowState(editor, optionVar):
    pass


def createPropertyEditorWindow(restore='False'):
    pass


def windowClosed(editor):
    pass


def createLookThroughWindow(restore='False', shouldBringToFront='True'):
    pass



kLightEditorHelp = []

_lightEditorWindow = None

kLayerText = []

kDefaultLayerText = []

kLookThroughLightsToolTip = []

kSnapToSelectedToolTip = []

kPropertyEditorToolTip = []

kLightEditorTitle = []

kHelp = []

kMayaHelp = []


