from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_Prescription(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Prescription")
        self.resize(448, 441)
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
        self.text_edit_drug.setGeometry(QtCore.QRect(20, 210, 411, 171))
        self.text_edit_drug.setObjectName("text_edit_drug")
        self.line_edit_ID = QtWidgets.QLineEdit(self)
        self.line_edit_ID.setGeometry(QtCore.QRect(350, 30, 81, 22))
        self.line_edit_ID.setReadOnly(True)
        self.line_edit_ID.setObjectName("line_edit_ID")
        self.label_ID = QtWidgets.QLabel(self)
        self.label_ID.setGeometry(QtCore.QRect(350, 10, 81, 20))
        self.label_ID.setObjectName("label_ID")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(350, 400, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(260, 400, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Prescription", "Form"))
        self.label_title.setText(_translate("Prescription", "Insert prescription data"))
        self.label_patient_data.setText(_translate("Prescription", "Patient data"))
        self.label_drug_conc.setText(_translate("Prescription", "Drug and concentration, quantity, dose, refund"))
        self.label_ID.setText(_translate("Prescription", "Generated ID"))
        self.push_button_return.setText(_translate("Prescription", "Return"))
        self.push_button_add.setText(_translate("Prescription", "Add"))

        self.push_button_return.clicked.connect(self.push_button_return_clicked)


    def create_prescription_data(self):
        prescription_data = {
            'id' : self.line_edit_ID.text(),
            'content' : self.text_edit_drug()
        }

    def push_button_return_clicked(self):
        self.close()