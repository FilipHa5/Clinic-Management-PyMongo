import sys
from PyQt5 import QtWidgets
from gui import Ui_Menu
from utils import MongoManager


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mongo_manager = MongoManager().getInstance()
    ui = Ui_Menu(mongo_manager)
    ui.show()
    sys.exit(app.exec_())