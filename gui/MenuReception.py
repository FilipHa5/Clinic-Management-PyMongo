from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from .utils import block_parrent_window
from .ScheduleAppointment import Ui_ScheduleAppointment
from .AddPatient import Ui_AddPatient
from .LinkPhysician import Ui_LinkPhysician
from .ShowAppointments import Ui_Show_appointments
from .AddPhysician import Ui_AddPhysican
from .Specialization import Ui_Specialization




class Ui_MenuReception(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MenuReception")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(617, 471)
        self.push_button_add_patient = QtWidgets.QPushButton(self)
        self.push_button_add_patient.setGeometry(QtCore.QRect(210, 120, 171, 71))
        self.push_button_add_patient.setObjectName("push_button_add_patient")
        self.push_button_appointment = QtWidgets.QPushButton(self)
        self.push_button_appointment.setGeometry(QtCore.QRect(40, 120, 161, 71))
        self.push_button_appointment.setObjectName("push_button_appointment")
        self.push_button_show_appointments = QtWidgets.QPushButton(self)
        self.push_button_show_appointments.setGeometry(QtCore.QRect(40, 200, 161, 71))
        self.push_button_show_appointments.setObjectName("push_button_show_appointments")
        self.label_menu_reception = QtWidgets.QLabel(self)
        self.label_menu_reception.setGeometry(QtCore.QRect(240, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_menu_reception.setFont(font)
        self.label_menu_reception.setObjectName("label_menu_reception")
        self.push_button_patient_link_spec_to_ph = QtWidgets.QPushButton(self)
        self.push_button_patient_link_spec_to_ph.setGeometry(QtCore.QRect(390, 120, 161, 71))
        self.push_button_patient_link_spec_to_ph.setObjectName("push_button_patient_link_spec_to_ph")
        self.push_button_reception_add_physician = QtWidgets.QPushButton(self)
        self.push_button_reception_add_physician.setGeometry(QtCore.QRect(210, 200, 171, 71))
        self.push_button_reception_add_physician.setObjectName("push_button_reception_add_physician")
        self.push_button_add_specialization = QtWidgets.QPushButton(self)
        self.push_button_add_specialization.setGeometry(QtCore.QRect(390, 200, 161, 71))
        self.push_button_add_specialization.setObjectName("push_button_add_specialization")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(210, 280, 171, 71))
        self.push_button_return.setObjectName("push_button_return")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MenuReception", "Form"))
        self.push_button_add_patient.setText(_translate("MenuReception", "Add new patient"))
        self.push_button_appointment.setText(_translate("MenuReception", "Schedule appointment"))
        self.push_button_show_appointments.setText(_translate("MenuReception", "Show appointments"))
        self.label_menu_reception.setText(_translate("MenuReception", "Select option"))
        self.push_button_patient_link_spec_to_ph.setText(_translate("MenuReception", " Link specialization to physican"))
        self.push_button_reception_add_physician.setText(_translate("MenuReception", "Add new physican"))
        self.push_button_add_specialization.setText(_translate("MenuReception", "Add new specialization"))
        self.push_button_return.setText(_translate("MenuReception", "Return"))
        
        self.ui = None
        self.push_button_appointment.clicked.connect(self.push_button_appointment_clicked)
        self.push_button_add_patient.clicked.connect(self.push_button_add_patient_clicked)
        self.push_button_patient_link_spec_to_ph.clicked.connect(self.push_button_patient_link_spec_to_ph_clicked)
        self.push_button_return.clicked.connect(self.push_button_return_clicked)
        self.push_button_show_appointments.clicked.connect(self.push_button_show_appointments_clicked)
        self.push_button_reception_add_physician.clicked.connect(self.push_button_reception_add_physician_clicked)
        self.push_button_add_specialization.clicked.connect(self.push_button_add_specialization_clicked)


    def push_button_appointment_clicked(self):
        self.ui = Ui_ScheduleAppointment()
        block_parrent_window(self)

    def push_button_add_patient_clicked(self):
        self.ui = Ui_AddPatient()
        block_parrent_window(self)

    def push_button_patient_link_spec_to_ph_clicked(self):
        self.ui = Ui_LinkPhysician()
        block_parrent_window(self)

    def push_button_show_appointments_clicked(self):
        self.ui = Ui_Show_appointments()
        block_parrent_window(self)

    def push_button_reception_add_physician_clicked(self):
        self.ui = Ui_AddPhysican()
        block_parrent_window(self)

    def push_button_add_specialization_clicked(self):
        self.ui = Ui_Specialization(self)
        block_parrent_window(self)

    
    def push_button_return_clicked(self):
        self.close()


