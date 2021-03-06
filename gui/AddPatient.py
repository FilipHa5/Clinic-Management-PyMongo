from ctypes.wintypes import tagPOINT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_AddPatient(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("AddPatient")
        self.resize(323, 318)
        self.push_button_add_patient = QtWidgets.QPushButton(self)
        self.push_button_add_patient.setGeometry(QtCore.QRect(60, 270, 81, 31))
        self.push_button_add_patient.setObjectName("push_button_add_patient")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(170, 270, 81, 31))
        self.push_button_return.setObjectName("push_button_return")
        self.label_pesel = QtWidgets.QLabel(self)
        self.label_pesel.setGeometry(QtCore.QRect(40, 50, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_pesel.setFont(font)
        self.label_pesel.setObjectName("label_pesel")
        self.label_given_name = QtWidgets.QLabel(self)
        self.label_given_name.setGeometry(QtCore.QRect(40, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_given_name.setFont(font)
        self.label_given_name.setObjectName("label_given_name")
        self.label_last_name = QtWidgets.QLabel(self)
        self.label_last_name.setGeometry(QtCore.QRect(40, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName("label_last_name")
        self.label_sex = QtWidgets.QLabel(self)
        self.label_sex.setGeometry(QtCore.QRect(40, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_sex.setFont(font)
        self.label_sex.setObjectName("label_sex")
        self.label_date_of_birth = QtWidgets.QLabel(self)
        self.label_date_of_birth.setGeometry(QtCore.QRect(40, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_date_of_birth.setFont(font)
        self.label_date_of_birth.setObjectName("label_date_of_birth")
        self.line_edit_pesel = QtWidgets.QLineEdit(self)
        self.line_edit_pesel.setGeometry(QtCore.QRect(120, 50, 171, 20))
        self.line_edit_pesel.setObjectName("line_edit_pesel")
        self.line_edit_given_name = QtWidgets.QLineEdit(self)
        self.line_edit_given_name.setGeometry(QtCore.QRect(120, 90, 171, 21))
        self.line_edit_given_name.setObjectName("line_edit_given_name")
        self.line_edit_last_name = QtWidgets.QLineEdit(self)
        self.line_edit_last_name.setGeometry(QtCore.QRect(122, 130, 171, 20))
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.combo_box_sex = QtWidgets.QComboBox(self)
        self.combo_box_sex.setGeometry(QtCore.QRect(120, 170, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box_sex.setFont(font)
        self.combo_box_sex.setObjectName("combo_box_sex")
        self.combo_box_sex.addItem("")
        self.combo_box_sex.addItem("")
        self.date_of_birth_edit = QtWidgets.QDateEdit(self)
        self.date_of_birth_edit.setGeometry(QtCore.QRect(120, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_of_birth_edit.setFont(font)
        self.date_of_birth_edit.setObjectName("date_of_birth_edit")
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(90, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddPatient", "Form"))
        self.push_button_add_patient.setText(_translate("AddPatient", "Add patient"))
        self.push_button_return.setText(_translate("AddPatient", "Return"))
        self.label_pesel.setText(_translate("AddPatient", "PESEL"))
        self.label_given_name.setText(_translate("AddPatient", "Given name"))
        self.label_last_name.setText(_translate("AddPatient", "Last name"))
        self.label_sex.setText(_translate("AddPatient", "Sex"))
        self.label_date_of_birth.setText(_translate("AddPatient", "Date of birth"))
        self.combo_box_sex.setItemText(0, _translate("AddPatient", "Male"))
        self.combo_box_sex.setItemText(1, _translate("AddPatient", "Female"))
        self.label_header.setText(_translate("AddPatient", "Insert patient data"))
        
        self.mongo_manager = mongo_manager
        self.push_button_add_patient.clicked.connect(self.push_button_add_patient_clicked)
        date_of_birth = self.date_of_birth_edit.date()
        self.push_button_return.clicked.connect(self.push_button_return_clicked)

    
    def create_patient_dict(self):
        patient_data = {
            'pesel': int(self.line_edit_pesel.text()),
            'name': self.line_edit_given_name.text(),
            'last_name': self.line_edit_last_name.text(),
            'sex': self.combo_box_sex.currentText(),
            'date_of_birth': self.date_of_birth_edit.dateTime().toPyDateTime()
        }
        return patient_data
    
    def push_button_add_patient_clicked(self):
        if (self.line_edit_pesel.text() == '' or self.line_edit_given_name.text() == '' or
            self.line_edit_last_name.text() == ''):
            return
        else:
            self.perform_action_on_data()
        
    def perform_action_on_data(self):
        try:
            patient_data = self.create_patient_dict()
            self.mongo_manager.Patient.insert_one(patient_data)
            self.close()
        except Exception as e:
            print(e)
    
    def push_button_return_clicked(self):
        self.close()


