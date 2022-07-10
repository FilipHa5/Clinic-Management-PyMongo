from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_ScheduleAppointment(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("ScheduleAppointment")
        self.resize(323, 294)
        self.push_button_schedule = QtWidgets.QPushButton(self)
        self.push_button_schedule.setGeometry(QtCore.QRect(40, 240, 121, 31))
        self.push_button_schedule.setObjectName("push_button_schedule")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(170, 240, 121, 31))
        self.push_button_return.setObjectName("push_button_return")
        self.label_pesel = QtWidgets.QLabel(self)
        self.label_pesel.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_pesel.setFont(font)
        self.label_pesel.setObjectName("label_pesel")
        self.label_time = QtWidgets.QLabel(self)
        self.label_time.setGeometry(QtCore.QRect(40, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.label_specialization = QtWidgets.QLabel(self)
        self.label_specialization.setGeometry(QtCore.QRect(40, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_specialization.setFont(font)
        self.label_specialization.setObjectName("label_specialization")
        self.pesel_combo_box = QtWidgets.QComboBox(self)
        self.pesel_combo_box.setGeometry(QtCore.QRect(170, 50, 121, 20))
        self.pesel_combo_box.setObjectName("pesel_combo_box")
        self.combo_box_specialization = QtWidgets.QComboBox(self)
        self.combo_box_specialization.setGeometry(QtCore.QRect(170, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box_specialization.setFont(font)
        self.combo_box_specialization.setObjectName("combo_box_specialization")
        self.combo_box_specialization.addItem("")
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(70, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.date_time_edit = QtWidgets.QDateTimeEdit(self)
        self.date_time_edit.setGeometry(QtCore.QRect(170, 90, 121, 31))
        self.date_time_edit.setObjectName("date_time_edit")
        self.label_physicans_name = QtWidgets.QLabel(self)
        self.label_physicans_name.setGeometry(QtCore.QRect(40, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_physicans_name.setFont(font)
        self.label_physicans_name.setObjectName("label_physicans_name")
        self.combo_box_physicans_name = QtWidgets.QComboBox(self)
        self.combo_box_physicans_name.setGeometry(QtCore.QRect(170, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box_physicans_name.setFont(font)
        self.combo_box_physicans_name.setObjectName("combo_box_physicans_name")
        self.combo_box_physicans_name.addItem("")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ScheduleAppointment", "Form"))
        self.push_button_schedule.setText(_translate("ScheduleAppointment", "Schedule"))
        self.push_button_return.setText(_translate("ScheduleAppointment", "Return"))
        self.label_pesel.setText(_translate("ScheduleAppointment", "Patient PESEL"))
        self.label_time.setText(_translate("ScheduleAppointment", "Time of appointment"))
        self.label_specialization.setText(_translate("ScheduleAppointment", "Physican\'s specialization"))
        self.label_header.setText(_translate("ScheduleAppointment", "Schedule appointment"))
        self.label_physicans_name.setText(_translate("ScheduleAppointment", "Physican\'s name"))
       
        self.mongo_manager = mongo_manager
        self.push_button_return.clicked.connect(self.push_button_return_clicked)
        self.push_button_schedule.clicked.connect(self.push_button_schedule_clicked)
        self.combo_box_specialization.addItems(self.mongo_manager.Specialization.distinct('specialization'))
        self.combo_box_specialization.currentIndexChanged.connect(self.populate_combo_box_physicans_name)
        self.pesel_combo_box.addItems([str (i) for i in self.mongo_manager.Patient.distinct("pesel")])

    
    def populate_combo_box_physicans_name(self):
        self.pwz_dict = {}
        self.combo_box_physicans_name.clear()
        medicians = self.mongo_manager.Medician.find(
                        {'specializations.specialization': 
                            {'$eq': self.combo_box_specialization.currentText()}
                        }
                    )
        for med in medicians:
            key_name = med['name'] + ' ' + med['last_name'] + ' ' + str(med['pwz'])
            self.pwz_dict[key_name] = med['pwz']
        
        self.combo_box_physicans_name.addItems(self.pwz_dict.keys())
    
    
    def create_appointment_dict(self):
        appointment_data = {
            'pesel' : int(self.pesel_combo_box.currentText()),
            'time' : self.date_time_edit.dateTime().toPyDateTime(),
            'physicans_spec' : self.combo_box_specialization.currentText(),
            'pwz' : self.pwz_dict[self.combo_box_physicans_name.currentText()],
            'documents': []
        }
        return appointment_data
    
    def push_button_schedule_clicked(self):
        if not (self.pesel_combo_box.currentText() != '' and 
            self.combo_box_specialization.count() and 
            self.combo_box_physicans_name.count()):
            return
        else:
            self.perform_action_with_data()
        
    def perform_action_with_data(self):
        try:
            appointment_data = self.create_appointment_dict()
            self.mongo_manager.Appointment.insert_one(appointment_data)
            self.close()
        except Exception as e:
            print (e)
    
    def push_button_return_clicked(self):
        self.close()

