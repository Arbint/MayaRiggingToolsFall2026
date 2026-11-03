from PySide6.QtGui import QPen
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QListWidget
from PySide6.QtGui import QAbstractTextDocumentLayout
from PySide6.QtWidgets import QStyleOptionViewItem
from PySide6.QtWidgets import QAction
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import QShortcut
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtGui import QPalette
from PySide6.QtGui import QKeySequence
from functools import partial
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QStyle
from PySide6.QtWidgets import QAbstractItemView

class HTMLDelegate(QStyledItemDelegate):
    def __init__(self, selector):
        pass
    
    
    def paint(self, painter, option, index):
        """
        Renders the delegate using the given painter and style option for the item specified by index.
        """
    
        pass
    
    
    def sizeHint(self, option, index):
        pass
    
    
    staticMetaObject = None


class CollectionStaticSelectionWidget(QListWidget):
    """
    This class implements a widget that displays a list of dropped Outliner objects.
    """
    
    
    
    def __init__(self, selector, parent='None'):
        pass
    
    
    def addEntry(self):
        """
        Adds the selected items to the list
        """
    
        pass
    
    
    def dragEnterEvent(self, event):
        """
        Accepts drag events if the dragged event text contains only commands
        """
    
        pass
    
    
    def dragMoveEvent(self, event):
        """
        Accepts drag move events. Validation is already done in the enter event
        """
    
        pass
    
    
    def dropEvent(self, event):
        """
        Adds the dropped object names to the list (if they don't already exist)
        """
    
        pass
    
    
    def highlight(self, names):
        pass
    
    
    def onDoubleClick(self, item):
        pass
    
    
    def paintEvent(self, e):
        """
        Overrides the paint event to make it so that place holder text is displayed when the list is empty.
        """
    
        pass
    
    
    def populate(self):
        pass
    
    
    def removeEntry(self):
        """
        Removes the selected items from the list
        """
    
        pass
    
    
    def removeFilteredObjects(self):
        pass
    
    
    def removeMissingObjects(self):
        pass
    
    
    def rightClicked(self, point):
        """
        Displays the right click context menu
        """
    
        pass
    
    
    def selectEntry(self):
        """
        Selects the selected items from the list
        """
    
        pass
    
    
    def selectFilteredObjects(self):
        pass
    
    
    def selectMembers(self):
        pass
    
    
    def selectMissingObjects(self):
        pass
    
    
    def setSortingEnabled(self, enabled):
        pass
    
    
    def sizeHintForRow(self, row):
        pass
    
    
    MAX_VISIBLE_ENTRIES = 10
    
    
    MIN_VISIBLE_ENTRIES = 4
    
    
    PLACEHOLDER_TEXT_PEN = None
    
    
    ROW_HEIGHT = 21
    
    
    staticMetaObject = None



kCouldNotSelectMissingObject = []


