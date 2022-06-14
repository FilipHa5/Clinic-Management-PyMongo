from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox


def block_parrent_window(self):
    """
    object need to have field named `ui` of type QWidget
    """
    self.ui.setWindowModality(QtCore.Qt.ApplicationModal)
    self.ui.show()


def populate_combo_box(combo_box, items):
    
    for item in items:
        combo_box.addItem(str(item))
