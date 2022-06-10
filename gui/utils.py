from PyQt5 import QtCore


def block_parrent_window(self):
    """
    object need to have field named `ui` of type QWidget
    """
    self.ui.setWindowModality(QtCore.Qt.ApplicationModal)
    self.ui.show()