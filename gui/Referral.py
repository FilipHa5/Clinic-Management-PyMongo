from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import random as r

class Ui_Referral(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Referral")
        self.resize(542, 545)
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
        self.line_edit_dest.setGeometry(QtCore.QRect(20, 220, 501, 22))
        self.line_edit_dest.setText("")
        self.line_edit_dest.setObjectName("line_edit_dest")
        self.text_edit_description = QtWidgets.QTextEdit(self)
        self.text_edit_description.setGeometry(QtCore.QRect(20, 300, 501, 131))
        self.text_edit_description.setObjectName("text_edit_description")
        self.label_description = QtWidgets.QLabel(self)
        self.label_description.setGeometry(QtCore.QRect(20, 280, 181, 16))
        self.label_description.setObjectName("label_description")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(350, 510, 75, 24))
        self.push_button_add.setObjectName("push_button_add")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(440, 510, 75, 24))
        self.push_button_return.setObjectName("push_button_return")
        self.combo_box_codes = QtWidgets.QComboBox(self)
        self.combo_box_codes.setGeometry(QtCore.QRect(20, 180, 501, 22))
        self.combo_box_codes.setObjectName("combo_box_codes")
        self.label_code = QtWidgets.QLabel(self)
        self.label_code.setGeometry(QtCore.QRect(20, 160, 181, 16))
        self.label_code.setObjectName("label_code")
        self.line_edit_just = QtWidgets.QLineEdit(self)
        self.line_edit_just.setGeometry(QtCore.QRect(20, 250, 501, 22))
        self.line_edit_just.setText("")
        self.line_edit_just.setObjectName("line_edit_dest_2")
        self.line_edit_comment = QtWidgets.QLineEdit(self)
        self.line_edit_comment.setGeometry(QtCore.QRect(20, 450, 501, 22))
        self.line_edit_comment.setText("")
        self.line_edit_comment.setObjectName("line_edit_dest_3")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.mongo_manager = mongo_manager

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Referral", "Form"))
        self.label_title.setText(_translate("Referral", "Insert referral data"))
        self.label.setText(_translate("Referral", "Generated ID"))
        self.label_patient_data.setText(_translate("Referral", "Patient data"))
        self.line_edit_dest.setPlaceholderText(_translate("Referral", "Referral destination specialization"))
        self.label_description.setText(_translate("Referral", "Purpose of referral"))
        self.push_button_add.setText(_translate("Referral", "Add"))
        self.push_button_return.setText(_translate("Referral", "Return"))
        self.label_code.setText(_translate("Referral", "Code and issue"))
        self.line_edit_just.setPlaceholderText(_translate("Referral", "Justification"))
        self.line_edit_comment.setPlaceholderText(_translate("Referral", "Comment"))

        self.push_button_return.clicked.connect(self.push_button_return_clicked)

    def populate_combo_box_codes(self):
        with open('ICD.txt') as f:
            self.combo_box_codes.insertItem(f.readlines())

    def create_referral_data(self):
        referral_data = {
            'id' : r.randint(1000,99999),
            'code_issue' : self.combo_box_codes.currentText(),
            'destination' : self.line_edit_dest.text(),
            'description': self.text_edit_description.toPlainText(),
            'justification' : self.line_edit_just.text(),
            'comment' : self.line_edit_comment.text()
        }

    def push_button_return_clicked(self):
        self.close()

    def push_button_add_clicked(self):
        print('swfde')
        #self.close()