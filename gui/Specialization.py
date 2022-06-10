# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Specialization.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Specialization(object):
    def setupUi(self, Specialization):
        Specialization.setObjectName("Specialization")
        Specialization.resize(314, 300)
        self.label_specialization = QtWidgets.QLabel(Specialization)
        self.label_specialization.setGeometry(QtCore.QRect(30, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_specialization.setFont(font)
        self.label_specialization.setObjectName("label_specialization")
        self.line_edit_specialization = QtWidgets.QLineEdit(Specialization)
        self.line_edit_specialization.setGeometry(QtCore.QRect(110, 50, 171, 20))
        self.line_edit_specialization.setObjectName("line_edit_specialization")
        self.label_description = QtWidgets.QLabel(Specialization)
        self.label_description.setGeometry(QtCore.QRect(30, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.return_push_button = QtWidgets.QPushButton(Specialization)
        self.return_push_button.setGeometry(QtCore.QRect(170, 240, 121, 32))
        self.return_push_button.setObjectName("return_push_button")
        self.push_button_add = QtWidgets.QPushButton(Specialization)
        self.push_button_add.setGeometry(QtCore.QRect(40, 240, 111, 31))
        self.push_button_add.setObjectName("push_button_add")
        self.text_edit_description = QtWidgets.QTextEdit(Specialization)
        self.text_edit_description.setGeometry(QtCore.QRect(30, 110, 261, 91))
        self.text_edit_description.setObjectName("text_edit_description")

        self.retranslateUi(Specialization)
        QtCore.QMetaObject.connectSlotsByName(Specialization)

    def retranslateUi(self, Specialization):
        _translate = QtCore.QCoreApplication.translate
        Specialization.setWindowTitle(_translate("Specialization", "Form"))
        self.label_specialization.setText(_translate("Specialization", "Specialization"))
        self.label_description.setText(_translate("Specialization", "Description"))
        self.return_push_button.setText(_translate("Specialization", "Return"))
        self.push_button_add.setText(_translate("Specialization", "Add"))



