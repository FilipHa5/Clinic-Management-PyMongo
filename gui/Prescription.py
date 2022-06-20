from tokenize import Number
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import datetime
import random

class Ui_Prescription(QMainWindow):
    def __init__(self, mongo_manager, values):
        super().__init__()
        self.setObjectName("Prescription")
        self.resize(448, 364)
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_patient_data = QtWidgets.QLabel(self)
        self.label_patient_data.setGeometry(QtCore.QRect(20, 60, 181, 16))
        self.label_patient_data.setObjectName("label_patient_data")
        self.text_display = QtWidgets.QTextEdit(self)
        self.text_display.setGeometry(QtCore.QRect(20, 80, 411, 71))
        self.text_display.setReadOnly(True)
        self.text_display.setObjectName("text_display")
        self.label_drug_conc = QtWidgets.QLabel(self)
        self.label_drug_conc.setGeometry(QtCore.QRect(20, 180, 271, 16))
        self.label_drug_conc.setObjectName("label_drug_conc")
        self.text_edit_drug = QtWidgets.QTextEdit(self)
        self.text_edit_drug.setGeometry(QtCore.QRect(20, 210, 411, 31))
        self.text_edit_drug.setObjectName("text_edit_drug")
        self.line_edit_ID = QtWidgets.QLineEdit(self)
        self.line_edit_ID.setGeometry(QtCore.QRect(350, 30, 81, 22))
        self.line_edit_ID.setReadOnly(True)
        self.line_edit_ID.setObjectName("line_edit_ID")
        self.label_ID = QtWidgets.QLabel(self)
        self.label_ID.setGeometry(QtCore.QRect(350, 10, 81, 20))
        self.label_ID.setObjectName("label_ID")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(360, 330, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(270, 330, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        self.push_button_add_2 = QtWidgets.QPushButton(self)
        self.push_button_add_2.setGeometry(QtCore.QRect(340, 250, 91, 24))
        self.push_button_add_2.setObjectName("push_button_add_2")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager
        self.values = values
        self.now = datetime.datetime.now()

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Prescription", "Form"))
        self.label_title.setText(_translate("Prescription", "Insert prescription data"))
        self.label_patient_data.setText(_translate("Prescription", "Patient data"))
        self.label_drug_conc.setText(_translate("Prescription", "Drug and concentration, quantity, dose, refund"))
        self.label_ID.setText(_translate("Prescription", "Generated ID"))
        self.push_button_return.setText(_translate("Prescription", "Return"))
        self.push_button_add.setText(_translate("Prescription", "Add"))
        self.push_button_add_2.setText(_translate("Prescription", "Add to list"))

        self.push_button_return.clicked.connect(self.push_button_return_clicked)
        self.push_button_add.clicked.connect(self.push_button_add_clicked)
        self.push_button_add_2.clicked.connect(self.add_drug)
        self.line_edit_ID.setText(str(random.randint(1000,9999)))
        self.text_display.setText("PESEL:" + str(self.values["pesel"]))
        self.drugs_list = []

    def generate_number(self):
        number = random.randint(1000, 9999)
        self.line_edit_ID.setText(str(number))
        return number

    def create_prescription_data(self):

        prescription_data = {
            "title" : ("prescription for patient" + str(self.values["pesel"])),
            "type" : "prescription",
            "pwz" : self.values["pwz"],
            "pesel" : self.values["pesel"],
            "creation_date" : self.now,
            'number' : int(self.line_edit_ID.text()),
            "drugs_list" : self.drugs_list,
        }
        return prescription_data

    def push_button_add_clicked(self):
        try:
            prescription_data = self.create_prescription_data()
            x = self.mongo_manager.TextInformation.insert_one(prescription_data)
            #_id = "ObjectId('%s')"
            self.mongo_manager.Appointment.update_one({'_id': self.values["nr_id"]}, 
                        {'$push': {'documents': x.inserted_id}})
            self.close()         
        except Exception as e:
            print (e)

    def add_drug(self):
        self.drugs_list.append(self.text_edit_drug.toPlainText())
        self.text_edit_drug.clear()

    def push_button_return_clicked(self):
        self.close()
