from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_AppointmentData(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("AppointmentData")
        self.resize(658, 884)
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
        self.text_edit_sub.setGeometry(QtCore.QRect(10, 210, 611, 101))
        self.text_edit_sub.setObjectName("text_edit_sub")
        self.label_subj_exam = QtWidgets.QLabel(self)
        self.label_subj_exam.setGeometry(QtCore.QRect(10, 190, 181, 16))
        self.label_subj_exam.setObjectName("label_subj_exam")
        self.label_physical_exam = QtWidgets.QLabel(self)
        self.label_physical_exam.setGeometry(QtCore.QRect(10, 320, 181, 16))
        self.label_physical_exam.setObjectName("label_physical_exam")
        self.text_edit_physical_exam = QtWidgets.QTextEdit(self)
        self.text_edit_physical_exam.setGeometry(QtCore.QRect(10, 350, 611, 101))
        self.text_edit_physical_exam.setObjectName("text_edit_physical_exam")
        self.text_edit_recom = QtWidgets.QTextEdit(self)
        self.text_edit_recom.setGeometry(QtCore.QRect(10, 640, 611, 101))
        self.text_edit_recom.setObjectName("text_edit_recom")
        self.label_recom = QtWidgets.QLabel(self)
        self.label_recom.setGeometry(QtCore.QRect(10, 610, 181, 16))
        self.label_recom.setObjectName("label_recom")
        self.text_edit_drugs = QtWidgets.QTextEdit(self)
        self.text_edit_drugs.setGeometry(QtCore.QRect(10, 490, 611, 101))
        self.text_edit_drugs.setObjectName("text_edit_drugs")
        self.label_drugs = QtWidgets.QLabel(self)
        self.label_drugs.setGeometry(QtCore.QRect(10, 460, 181, 16))
        self.label_drugs.setObjectName("label_drugs")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(560, 850, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(470, 850, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        self.combo_box_codes = QtWidgets.QComboBox(self)
        self.combo_box_codes.setGeometry(QtCore.QRect(10, 770, 611, 22))
        self.combo_box_codes.setObjectName("combo_box_codes")
        self.label_code = QtWidgets.QLabel(self)
        self.label_code.setGeometry(QtCore.QRect(10, 750, 181, 16))
        self.label_code.setObjectName("label_code")
        self.text_edit_reffering_unit = QtWidgets.QTextEdit(self)
        self.text_edit_reffering_unit.setGeometry(QtCore.QRect(10, 150, 611, 31))
        self.text_edit_reffering_unit.setObjectName("text_edit_reffering_unit")
        self.label_ref = QtWidgets.QLabel(self)
        self.label_ref.setGeometry(QtCore.QRect(10, 130, 311, 16))
        self.label_ref.setObjectName("label_ref")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AppointmentData", "Form"))
        self.label_title.setText(_translate("AppointmentData", "Insert appointment data"))
        self.label_patient_data.setText(_translate("AppointmentData", "Patient data"))
        self.label_subj_exam.setText(_translate("AppointmentData", "Subjective examination"))
        self.label_physical_exam.setText(_translate("AppointmentData", "Physical examination"))
        self.label_recom.setText(_translate("AppointmentData", "Recommendations"))
        self.label_drugs.setText(_translate("AppointmentData", "Prescribed drugs"))
        self.push_button_return.setText(_translate("AppointmentData", "Return"))
        self.push_button_add.setText(_translate("AppointmentData", "Add"))
        self.label_code.setText(_translate("AppointmentData", "Code and issue"))
        self.label_ref.setText(_translate("AppointmentData", "Referring unit - fill if appointment is based on referral"))

        self.push_button_return.clicked.connect(self.push_button_return_clicked)


    def populate_combo_box_codes(self):
        with open('ICD.txt') as f:
            self.combo_box_codes.insertItem(f.readlines())

    def create_appointment_data(self):
        appointment_data = {
            'referring_unit' : self.text_edit_reffering_unit.toPlainText(),
            'subjective_exam' : self.text_edit_sub.toPlainText(),
            'physical_exam' : self.text_edit_physical_exam.toPlainText(),
            'drugs' : self.text_edit_drugs.toPlainText(),
            'recommedtations' : self.text_edit_recom.toPlainText(),
            'code' : self.combo_box_codes.currentText()
        }

    def push_button_return_clicked(self):
        self.close()
