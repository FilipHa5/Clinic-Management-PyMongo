import sys
from PyQt5 import QtWidgets
from gui import *


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    #ui.setupUi(Menu)
    ui.show()
    sys.exit(app.exec_())