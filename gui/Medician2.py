from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from .AppointmentData import Ui_AppointmentData
from .Prescription import Ui_Prescription
from .Referral import Ui_Referral
from .utils import block_parrent_window


class Ui_Medician2(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Medician2")
        self.resize(815, 643)
        self.apply_pwz_push_button = QtWidgets.QPushButton(self)
        self.apply_pwz_push_button.setGeometry(QtCore.QRect(610, 50, 161, 32))
        self.apply_pwz_push_button.setObjectName("apply_pwz_push_button")
        self.pwz_line_edit = QtWidgets.QLineEdit(self)
        self.pwz_line_edit.setGeometry(QtCore.QRect(610, 20, 161, 21))
        self.pwz_line_edit.setText("")
        self.pwz_line_edit.setObjectName("pwz_line_edit")
        self.combo_box_patient = QtWidgets.QComboBox(self)
        self.combo_box_patient.setGeometry(QtCore.QRect(560, 310, 241, 26))
        self.combo_box_patient.setObjectName("combo_box_patient")
        self.display_text_edit = QtWidgets.QTextEdit(self)
        self.display_text_edit.setGeometry(QtCore.QRect(20, 40, 521, 181))
        self.display_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.display_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_text_edit.setReadOnly(True)
        self.display_text_edit.setObjectName("display_text_edit")
        self.label_visits = QtWidgets.QLabel(self)
        self.label_visits.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_visits.setObjectName("label_visits")
        self.label_patient = QtWidgets.QLabel(self)
        self.label_patient.setGeometry(QtCore.QRect(660, 280, 55, 16))
        self.label_patient.setObjectName("label_patient")
        self.push_button_ref = QtWidgets.QPushButton(self)
        self.push_button_ref.setGeometry(QtCore.QRect(690, 460, 111, 24))
        self.push_button_ref.setObjectName("push_button_ref")
        self.push_button_presc = QtWidgets.QPushButton(self)
        self.push_button_presc.setGeometry(QtCore.QRect(560, 500, 111, 24))
        self.push_button_presc.setObjectName("push_button_presc")
        self.push_button_desc = QtWidgets.QPushButton(self)
        self.push_button_desc.setGeometry(QtCore.QRect(560, 460, 111, 24))
        self.push_button_desc.setObjectName("push_button_desc")
        self.return_push_button = QtWidgets.QPushButton(self)
        self.return_push_button.setGeometry(QtCore.QRect(560, 590, 241, 31))
        self.return_push_button.setObjectName("return_push_button")
        self.display_history_text_edit = QtWidgets.QTextEdit(self)
        self.display_history_text_edit.setGeometry(QtCore.QRect(20, 280, 521, 341))
        self.display_history_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.display_history_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_history_text_edit.setReadOnly(True)
        self.display_history_text_edit.setObjectName("display_history_text_edit")
        self.label_history = QtWidgets.QLabel(self)
        self.label_history.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.label_history.setObjectName("label_history")
        self.label_appointment = QtWidgets.QLabel(self)
        self.label_appointment.setGeometry(QtCore.QRect(640, 390, 81, 20))
        self.label_appointment.setObjectName("label_appointment")
        self.combo_box_appointments = QtWidgets.QComboBox(self)
        self.combo_box_appointments.setGeometry(QtCore.QRect(560, 420, 241, 26))
        self.combo_box_appointments.setObjectName("combo_box_appointments")
        self.push_button_edit = QtWidgets.QPushButton(self)
        self.push_button_edit.setGeometry(QtCore.QRect(690, 500, 111, 24))
        self.push_button_edit.setObjectName("push_button_edit")
        self.label_patient_2 = QtWidgets.QLabel(self)
        self.label_patient_2.setGeometry(QtCore.QRect(650, 110, 131, 16))
        self.label_patient_2.setObjectName("label_patient_2")
        self.combo_box_patient_2 = QtWidgets.QComboBox(self)
        self.combo_box_patient_2.setGeometry(QtCore.QRect(560, 140, 241, 26))
        self.combo_box_patient_2.setObjectName("combo_box_patient_2")
        QtCore.QMetaObject.connectSlotsByName(self)

        self.mongo_manager = mongo_manager

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Medician2", "Form"))
        self.apply_pwz_push_button.setText(_translate("Medician2", "Apply"))
        self.pwz_line_edit.setPlaceholderText(_translate("Medician2", "Insert your PWZ"))
        self.label_visits.setText(_translate("Medician2", "Visits"))
        self.label_patient.setText(_translate("Medician2", "Patient"))
        self.push_button_ref.setText(_translate("Medician2", "Add referral"))
        self.push_button_presc.setText(_translate("Medician2", "Add prescription"))
        self.push_button_desc.setText(_translate("Medician2", "Add description"))
        self.return_push_button.setText(_translate("Medician2", "Return"))
        self.label_history.setText(_translate("Medician2", "Medical history"))
        self.label_appointment.setText(_translate("Medician2", "Appointment"))
        self.push_button_edit.setText(_translate("Medician2", "Edit data"))
        self.label_patient_2.setText(_translate("Medician2", "Select date"))

        self.push_button_desc.clicked.connect(self.push_button_desc_clicked)
        self.push_button_presc.clicked.connect(self.push_button_presc_clicked)
        self.push_button_ref.clicked.connect(self.push_button_ref_clicked)
        self.return_push_button.clicked.connect(self.return_push_button_clicked)

    def return_push_button_clicked(self):
        self.close()

    def push_button_ref_clicked(self):
        self.ui = Ui_Referral(self.mongo_manager)
        block_parrent_window(self)

    def push_button_presc_clicked(self):
        self.ui = Ui_Prescription(self.mongo_manager)
        block_parrent_window(self)

    def push_button_desc_clicked(self):
        self.ui = Ui_AppointmentData(self.mongo_manager)
        block_parrent_window(self)
