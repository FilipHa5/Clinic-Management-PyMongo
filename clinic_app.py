import sys
from PyQt5 import QtWidgets
from gui import Ui_Menu


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Menu()
    ui.show()
    sys.exit(app.exec_())