from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import datetime
import random

class Ui_Referral(QMainWindow):
    def __init__(self, mongo_manager, values):
        super().__init__()
        self.setObjectName("Referral")
        self.resize(542, 390)
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.line_edit_id = QtWidgets.QLineEdit(self)
        self.line_edit_id.setGeometry(QtCore.QRect(430, 30, 81, 22))
        self.line_edit_id.setReadOnly(True)
        self.line_edit_id.setObjectName("line_edit_id")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(430, 10, 81, 20))
        self.label.setObjectName("label")
        self.label_patient_data = QtWidgets.QLabel(self)
        self.label_patient_data.setGeometry(QtCore.QRect(20, 50, 181, 16))
        self.label_patient_data.setObjectName("label_patient_data")
        self.text_edit_patient_data = QtWidgets.QTextEdit(self)
        self.text_edit_patient_data.setGeometry(QtCore.QRect(20, 70, 501, 71))
        self.text_edit_patient_data.setReadOnly(True)
        self.text_edit_patient_data.setObjectName("text_edit_patient_data")
        self.line_edit_dest = QtWidgets.QLineEdit(self)
        self.line_edit_dest.setGeometry(QtCore.QRect(20, 150, 501, 22))
        self.line_edit_dest.setText("")
        self.line_edit_dest.setObjectName("line_edit_dest")
        self.text_edit_description = QtWidgets.QTextEdit(self)
        self.text_edit_description.setGeometry(QtCore.QRect(20, 200, 501, 131))
        self.text_edit_description.setObjectName("text_edit_description")
        self.label_description = QtWidgets.QLabel(self)
        self.label_description.setGeometry(QtCore.QRect(20, 180, 181, 16))
        self.label_description.setObjectName("label_description")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(350, 350, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(440, 350, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager
        self.values = values

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Referral", "Form"))
        self.label_title.setText(_translate("Referral", "Insert referral data"))
        self.label.setText(_translate("Referral", "Generated ID"))
        self.label_patient_data.setText(_translate("Referral", "Patient data"))
        self.line_edit_dest.setPlaceholderText(_translate("Referral", "Referral destination specialization"))
        self.label_description.setText(_translate("Referral", "Purpose of referral"))
        self.push_button_add.setText(_translate("Referral", "Add"))
        self.push_button_return.setText(_translate("Referral", "Return"))
        
        self.push_button_return.clicked.connect(self.push_button_return_clicked)
        self.push_button_add.clicked.connect(self.push_button_add_clicked)
        self.now = datetime.datetime.now()
        self.line_edit_id.setText(str(random.randint(1000,9999)))
        self.text_edit_patient_data.setText("PESEL:" + str(self.values["pesel"]))

    def create_referral_data(self):
        referral_data = {
            "title" : ("referral for patient" + str(self.values[1])),
            "type" : "description",
            "pwz" : self.values["pwz"],
            "pesel" : self.values["pesel"],
            "creation_date" : self.now,
            'number' : int(self.line_edit_id.text()),
            'destination_specialization' : self.line_edit_dest.text(),
            "purpose" : self.text_edit_description.toPlainText()
        }
        return referral_data
        
    def push_button_add_clicked(self):
        try:
            referral_data = self.create_referral_data()
            self.mongo_manager.TextInformation.insert_one(referral_data)
            ref_id = list(self.mongo_manager.TextInformation.find_one({
                "creation_date" : {"$eq":self.now}
            }, {"_id":1}))
            print(ref_id)
            self.mongo_manager.Appointment.update_one({'_id': self.values["nr_id"]}, 
                        {'$push': {'documents': ref_id}})
        except Exception as e:
            print (e)

    def push_button_return_clicked(self):
        self.close()