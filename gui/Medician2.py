from optparse import Values
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from .AppointmentData import Ui_AppointmentData
from .Prescription import Ui_Prescription
from .Referral import Ui_Referral
import datetime
from .utils import block_parrent_window
from .utils import make_str_from_documents
from. utils import make_str_from_appoinment


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
        self.display_text_edit = QtWidgets.QTextEdit(self)
        self.display_text_edit.setGeometry(QtCore.QRect(20, 40, 521, 181))
        self.display_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.display_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_text_edit.setReadOnly(True)
        self.display_text_edit.setObjectName("display_text_edit")
        self.label_visits = QtWidgets.QLabel(self)
        self.label_visits.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_visits.setObjectName("label_visits")
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
        self.label_appointment.setGeometry(QtCore.QRect(640, 300, 81, 20))
        self.label_appointment.setObjectName("label_appointment")
        self.combo_box_appointments = QtWidgets.QComboBox(self)
        self.combo_box_appointments.setGeometry(QtCore.QRect(560, 330, 241, 26))
        self.combo_box_appointments.setObjectName("combo_box_appointments")
        self.label_patient_2 = QtWidgets.QLabel(self)
        self.label_patient_2.setGeometry(QtCore.QRect(650, 110, 131, 16))
        self.label_patient_2.setObjectName("label_patient_2")
        self.combo_box_date = QtWidgets.QComboBox(self)
        self.combo_box_date.setGeometry(QtCore.QRect(560, 140, 241, 26))
        self.combo_box_date.setObjectName("combo_box_date")
        self.apply_date_push_button = QtWidgets.QPushButton(self)
        self.apply_date_push_button.setGeometry(QtCore.QRect(610, 180, 161, 32))
        self.apply_date_push_button.setObjectName("apply_date_push_button")
        self.apply_appointment_push_button = QtWidgets.QPushButton(self)
        self.apply_appointment_push_button.setGeometry(QtCore.QRect(600, 370, 161, 32))
        self.apply_appointment_push_button.setObjectName("apply_appointment_push_button")

        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Medician2", "Form"))
        self.apply_pwz_push_button.setText(_translate("Medician2", "Apply"))
        self.pwz_line_edit.setPlaceholderText(_translate("Medician2", "Insert your PWZ"))
        self.label_visits.setText(_translate("Medician2", "Visits"))
        self.push_button_ref.setText(_translate("Medician2", "Add referral"))
        self.push_button_presc.setText(_translate("Medician2", "Add prescription"))
        self.push_button_desc.setText(_translate("Medician2", "Add description"))
        self.return_push_button.setText(_translate("Medician2", "Return"))
        self.label_history.setText(_translate("Medician2", "Medical history"))
        self.label_appointment.setText(_translate("Medician2", "Appointment"))
        self.label_patient_2.setText(_translate("Medician2", "Select date"))
        self.apply_date_push_button.setText(_translate("Medician2", "Apply"))
        self.apply_appointment_push_button.setText(_translate("Medician2", "Apply"))

        self.push_button_desc.clicked.connect(self.push_button_desc_clicked)
        self.push_button_presc.clicked.connect(self.push_button_presc_clicked)
        self.push_button_ref.clicked.connect(self.push_button_ref_clicked)
        self.return_push_button.clicked.connect(self.return_push_button_clicked)

        self.mongo_manager = mongo_manager

        self.apply_pwz_push_button.clicked.connect(self.apply_pwz_push_button_clicked)
        self.apply_date_push_button.clicked.connect(self.populate_visit_display)
        self.apply_date_push_button.clicked.connect(self.apply_date_push_button_clicked)
        self.date_dict = {}
        self.appointments_dict = {}
        self.values_dict = {}
        self.pesel_dict = {}



    def apply_pwz_push_button_clicked(self):
        if not self.pwz_line_edit.text == '':
            if self.combo_box_date.currentText() == '':
                self.combo_box_date.addItems(self.populate_visit_display())

    def populate_visit_display(self):
        self.date_dict = {}
        
        for appointment in self.mongo_manager.Appointment.find({
                            'pwz':
                                {'$eq': int(self.pwz_line_edit.text())}
                            }):
            key_name = str(appointment['time'])[:-8]
            self.date_dict[key_name] = appointment['time']
        
        return list(self.date_dict.keys())

    def apply_date_push_button_clicked(self):
        selected_date = self.date_dict[self.combo_box_date.currentText()]
        output_to_print = self.mongo_manager.Appointment.find( 
                    {
                        "time": {
                            "$gte": selected_date,
                            "$lt" : selected_date + datetime.timedelta(days=1)
                        }
                    })
        out_str = make_str_from_appoinment(output_to_print, self.mongo_manager)
        print (out_str)
        self.display_text_edit.setPlainText(out_str)
        self.combo_box_appointments.addItems(self.populate_combo_box_appointments())

    def populate_combo_box_appointments(self):
        selected_date = self.date_dict[self.combo_box_date.currentText()]
        self.combo_box_appointments.clear()
        self.appointments_dict = {}
        
        for appointment in self.mongo_manager.Appointment.find({
                        "time": {
                            "$gte": selected_date,
                            "$lt" : selected_date + datetime.timedelta(days=1)
                        },
                        "pwz" : int(self.pwz_line_edit.text())
                    }, {"pesel":1, "_id" : 1, "time":1}):
            patient = (self.mongo_manager.Patient.find_one({
                       "pesel" : appointment['pesel'] 
                        }, {"name" : 1, "last_name" : 1, "_id" : 0}))

            if patient == None:
                continue

            key_name = patient["name"] + " " + patient["last_name"] + " "+ str(appointment['pesel']) + " " +str(appointment['time'])[11:-3]
            self.appointments_dict[key_name] = appointment['_id']
            self.pesel_dict[key_name] = appointment["pesel"]
        return list(self.appointments_dict.keys())
    


    def return_push_button_clicked(self):
        self.close()

    def push_button_ref_clicked(self):
        if not self.combo_box_appointments.currentText() == '':
            nr_id = self.appointments_dict[self.combo_box_appointments.currentText()]
            pwz = int(self.pwz_line_edit.text())
            pesel = self.pesel_dict[self.combo_box_appointments.currentText()]
            self.values_dict = {"pwz" : pwz, "pesel": pesel,"nr_id" : nr_id}
            self.ui = Ui_Referral(self.mongo_manager, self.values_dict)
            block_parrent_window(self)

    def push_button_presc_clicked(self):
        if not self.combo_box_appointments.currentText() == '':
            nr_id = self.appointments_dict[self.combo_box_appointments.currentText()]
            pwz = int(self.pwz_line_edit.text())
            pesel = self.pesel_dict[self.combo_box_appointments.currentText()]
            self.values_dict = {"pwz" : pwz, "pesel": pesel,"nr_id" : nr_id}
            self.ui = Ui_Prescription(self.mongo_manager, self.values_dict)
            block_parrent_window(self)

    def push_button_desc_clicked(self):
        if not self.combo_box_appointments.currentText() == '':
            nr_id = self.appointments_dict[self.combo_box_appointments.currentText()]
            pwz = int(self.pwz_line_edit.text())
            pesel = self.pesel_dict[self.combo_box_appointments.currentText()]
            self.values_dict = {"pwz" : pwz, "pesel": pesel,"nr_id" : nr_id}
            self.ui = Ui_AppointmentData(self.mongo_manager, self.values_dict)
            block_parrent_window(self)