# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys



class Ui_Menu(QMainWindow):
    def push_button_patient_clicked(self):
        print ("patient clicked")
    def push_button_medician_clicked(self):
        print ("medician clicked")
    def push_button_reception_clicked(self):
        print ("reception clicked")
        
    def __init__(self):
        super().__init__()
        self.setObjectName("Menu")
        self.resize(604, 270)
        self.push_button_reception = QtWidgets.QPushButton(self)
        self.push_button_reception.setGeometry(QtCore.QRect(40, 100, 141, 71))
        self.push_button_reception.setObjectName("push_button_reception")
        self.push_button_medician = QtWidgets.QPushButton(self)
        self.push_button_medician.setGeometry(QtCore.QRect(230, 100, 141, 71))
        self.push_button_medician.setObjectName("push_button_medician")
        self.push_button_patient = QtWidgets.QPushButton(self)
        self.push_button_patient.setGeometry(QtCore.QRect(420, 100, 141, 71))
        self.push_button_patient.setObjectName("push_button_patient")        
        self.label_menu = QtWidgets.QLabel(self)
        self.label_menu.setGeometry(QtCore.QRect(180, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_menu.setFont(font)
        self.label_menu.setObjectName("label_menu")
        QtCore.QMetaObject.connectSlotsByName(self)
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Menu", "Menu"))
        self.push_button_reception.setText(_translate("Menu", "Reception"))
        self.push_button_medician.setText(_translate("Menu", "Medician"))
        self.push_button_patient.setText(_translate("Menu", "Patient"))
        self.label_menu.setText(_translate("Menu", "Choose your access level"))
        
        self.push_button_patient.clicked.connect(self.push_button_patient_clicked)
        self.push_button_medician.clicked.connect(self.push_button_medician_clicked)
        self.push_button_reception.clicked.connect(self.push_button_reception_clicked)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    #ui.setupUi(Menu)
    ui.show()
    sys.exit(app.exec_())
