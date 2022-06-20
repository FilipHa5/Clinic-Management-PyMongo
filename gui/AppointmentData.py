from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import datetime

class Ui_AppointmentData(QMainWindow):
    def __init__(self, mongo_manager, values):
        super().__init__()
        self.setObjectName("AppointmentData")
        self.resize(658, 606)
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_patient_data = QtWidgets.QLabel(self)
        self.label_patient_data.setGeometry(QtCore.QRect(10, 50, 181, 16))
        self.label_patient_data.setObjectName("label_patient_data")
        self.text_edit_patient_data = QtWidgets.QTextEdit(self)
        self.text_edit_patient_data.setGeometry(QtCore.QRect(10, 70, 611, 51))
        self.text_edit_patient_data.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text_edit_patient_data.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.text_edit_patient_data.setReadOnly(True)
        self.text_edit_patient_data.setObjectName("text_edit_patient_data")
        self.text_edit_sub = QtWidgets.QTextEdit(self)
        self.text_edit_sub.setGeometry(QtCore.QRect(10, 150, 611, 101))
        self.text_edit_sub.setObjectName("text_edit_sub")
        self.label_subj_exam = QtWidgets.QLabel(self)
        self.label_subj_exam.setGeometry(QtCore.QRect(10, 130, 181, 16))
        self.label_subj_exam.setObjectName("label_subj_exam")
        self.label_physical_exam = QtWidgets.QLabel(self)
        self.label_physical_exam.setGeometry(QtCore.QRect(10, 260, 181, 16))
        self.label_physical_exam.setObjectName("label_physical_exam")
        self.text_edit_physical_exam = QtWidgets.QTextEdit(self)
        self.text_edit_physical_exam.setGeometry(QtCore.QRect(10, 290, 611, 101))
        self.text_edit_physical_exam.setObjectName("text_edit_physical_exam")
        self.text_edit_recom = QtWidgets.QTextEdit(self)
        self.text_edit_recom.setGeometry(QtCore.QRect(10, 440, 611, 101))
        self.text_edit_recom.setObjectName("text_edit_recom")
        self.label_recom = QtWidgets.QLabel(self)
        self.label_recom.setGeometry(QtCore.QRect(10, 410, 181, 16))
        self.label_recom.setObjectName("label_recom")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(540, 560, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(450, 560, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager
        self.values = values
        self.now = datetime.datetime.now()

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AppointmentData", "Form"))
        self.label_title.setText(_translate("AppointmentData", "Insert appointment data"))
        self.label_patient_data.setText(_translate("AppointmentData", "Patient data"))
        self.label_subj_exam.setText(_translate("AppointmentData", "Subjective examination"))
        self.label_physical_exam.setText(_translate("AppointmentData", "Physical examination"))
        self.label_recom.setText(_translate("AppointmentData", "Recommendations"))
        self.push_button_return.setText(_translate("AppointmentData", "Return"))
        self.push_button_add.setText(_translate("AppointmentData", "Add"))

        self.push_button_return.clicked.connect(self.push_button_return_clicked)
        self.push_button_add.clicked.connect(self.push_button_add_clicked)
        self.text_edit_patient_data.setText("PESEL:" + str(self.values["pesel"]))


    def create_appointment_dict(self):
        appointment_data = {
            "title" : ("report for patient" + str(self.values["pesel"])),
            "type" : "description",
            "pwz" : self.values["pwz"],
            "pesel" : self.values["pesel"],
            "creation_date" : self.now,
            "subjective_examination" : self.text_edit_sub.toPlainText(),
            "physical_examination" : self.text_edit_physical_exam.toPlainText(),
            "recomendations" : self.text_edit_recom.toPlainText()
        }
        return appointment_data

    def push_button_add_clicked(self):
        try:
            appointment_data = self.create_appointment_dict()
            x = self.mongo_manager.TextInformation.insert_one(appointment_data)
            _id = "ObjectId('%s')"
            to_insert = (_id % x.inserted_id)
            self.mongo_manager.Appointment.update_one({'_id': self.values["nr_id"]}, 
                        {'$push': {'documents':to_insert}})
            self.close()  
        except Exception as e:
            print (e)

    def push_button_return_clicked(self):
        self.close()