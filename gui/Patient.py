# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patient.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Patient(object):
    def setupUi(self, Patient):
        Patient.setObjectName("Patient")
        Patient.resize(752, 611)
        self.text_display = QtWidgets.QTextEdit(Patient)
        self.text_display.setGeometry(QtCore.QRect(30, 150, 681, 441))
        self.text_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_display.setReadOnly(True)
        self.text_display.setObjectName("text_display")
        self.line_edit_pesel = QtWidgets.QLineEdit(Patient)
        self.line_edit_pesel.setGeometry(QtCore.QRect(30, 110, 131, 20))
        self.line_edit_pesel.setText("")
        self.line_edit_pesel.setObjectName("line_edit_pesel")
        self.line_edit_last_name = QtWidgets.QLineEdit(Patient)
        self.line_edit_last_name.setGeometry(QtCore.QRect(400, 110, 131, 20))
        self.line_edit_last_name.setText("")
        self.line_edit_last_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.line_edit_given_name = QtWidgets.QLineEdit(Patient)
        self.line_edit_given_name.setGeometry(QtCore.QRect(210, 110, 131, 20))
        self.line_edit_given_name.setText("")
        self.line_edit_given_name.setObjectName("line_edit_given_name")
        self.label_header = QtWidgets.QLabel(Patient)
        self.label_header.setGeometry(QtCore.QRect(310, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.push_button_display = QtWidgets.QPushButton(Patient)
        self.push_button_display.setGeometry(QtCore.QRect(560, 110, 71, 21))
        self.push_button_display.setObjectName("push_button_display")
        self.label_desc = QtWidgets.QLabel(Patient)
        self.label_desc.setGeometry(QtCore.QRect(250, 60, 321, 16))
        self.label_desc.setObjectName("label_desc")
        self.return_push_button = QtWidgets.QPushButton(Patient)
        self.return_push_button.setGeometry(QtCore.QRect(640, 110, 71, 21))
        self.return_push_button.setObjectName("return_push_button")

        self.retranslateUi(Patient)
        QtCore.QMetaObject.connectSlotsByName(Patient)

    def retranslateUi(self, Patient):
        _translate = QtCore.QCoreApplication.translate
        Patient.setWindowTitle(_translate("Patient", "Form"))
        self.line_edit_pesel.setPlaceholderText(_translate("Patient", "PESEL"))
        self.line_edit_last_name.setPlaceholderText(_translate("Patient", "Last name"))
        self.line_edit_given_name.setPlaceholderText(_translate("Patient", "Given name"))
        self.label_header.setText(_translate("Patient", "Patient menu"))
        self.push_button_display.setText(_translate("Patient", "Display"))
        self.label_desc.setText(_translate("Patient", "Insert your data to display your medical history"))
        self.return_push_button.setText(_translate("Patient", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Patient = QtWidgets.QWidget()
    ui = Ui_Patient()
    ui.setupUi(Patient)
    Patient.show()
    sys.exit(app.exec_())

