# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from .utils import block_parrent_window
from .Medician2 import Ui_Medician2
from .Patient import Ui_Patient
from .MenuReception import Ui_MenuReception
from .ShowAppointments import Ui_Show_appointments
from .AddPhysician import Ui_AddPhysican
from .Specialization import Ui_Specialization



class Ui_Menu(QMainWindow):
    def __init__(self, mongo_manager):
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
        
        self.mongo_manager = mongo_manager
        self.ui = None
        self.push_button_patient.clicked.connect(self.push_button_patient_clicked)
        self.push_button_medician.clicked.connect(self.push_button_medician_clicked)
        self.push_button_reception.clicked.connect(self.push_button_reception_clicked)
    
    
    def push_button_patient_clicked(self):
        self.ui = Ui_Patient(self.mongo_manager)
        block_parrent_window(self)
    
    def push_button_medician_clicked(self):
        self.ui = Ui_Medician2(self.mongo_manager)
        block_parrent_window(self)
    
    def push_button_reception_clicked(self):
        self.ui = Ui_MenuReception(self.mongo_manager)
        block_parrent_window(self)
    

