# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ZofiaHalo\Documents\Mongo\AddPhysician.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPhysican(object):
    def setupUi(self, AddPhysican):
        AddPhysican.setObjectName("AddPhysican")
        AddPhysican.resize(323, 380)
        self.push_button_add = QtWidgets.QPushButton(AddPhysican)
        self.push_button_add.setGeometry(QtCore.QRect(100, 320, 121, 31))
        self.push_button_add.setObjectName("push_button_add")
        self.label_no_pwz = QtWidgets.QLabel(AddPhysican)
        self.label_no_pwz.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_no_pwz.setFont(font)
        self.label_no_pwz.setObjectName("label_no_pwz")
        self.label_last_name = QtWidgets.QLabel(AddPhysican)
        self.label_last_name.setGeometry(QtCore.QRect(40, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName("label_last_name")
        self.line_edit_pesel = QtWidgets.QLineEdit(AddPhysican)
        self.line_edit_pesel.setGeometry(QtCore.QRect(170, 50, 121, 20))
        self.line_edit_pesel.setObjectName("line_edit_pesel")
        self.label_header = QtWidgets.QLabel(AddPhysican)
        self.label_header.setGeometry(QtCore.QRect(90, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.line_edit_given_name = QtWidgets.QLineEdit(AddPhysican)
        self.line_edit_given_name.setGeometry(QtCore.QRect(170, 90, 121, 20))
        self.line_edit_given_name.setObjectName("line_edit_given_name")
        self.label_given_name = QtWidgets.QLabel(AddPhysican)
        self.label_given_name.setGeometry(QtCore.QRect(40, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_given_name.setFont(font)
        self.label_given_name.setObjectName("label_given_name")
        self.line_edit_last_name = QtWidgets.QLineEdit(AddPhysican)
        self.line_edit_last_name.setGeometry(QtCore.QRect(170, 130, 121, 20))
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.text_edit_description = QtWidgets.QTextEdit(AddPhysican)
        self.text_edit_description.setGeometry(QtCore.QRect(40, 200, 251, 91))
        self.text_edit_description.setObjectName("text_edit_description")
        self.label_last_name_2 = QtWidgets.QLabel(AddPhysican)
        self.label_last_name_2.setGeometry(QtCore.QRect(40, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_last_name_2.setFont(font)
        self.label_last_name_2.setObjectName("label_last_name_2")

        self.retranslateUi(AddPhysican)
        QtCore.QMetaObject.connectSlotsByName(AddPhysican)

    def retranslateUi(self, AddPhysican):
        _translate = QtCore.QCoreApplication.translate
        AddPhysican.setWindowTitle(_translate("AddPhysican", "Form"))
        self.push_button_add.setText(_translate("AddPhysican", "Add"))
        self.label_no_pwz.setText(_translate("AddPhysican", "No PWZ"))
        self.label_last_name.setText(_translate("AddPhysican", "Last name"))
        self.label_header.setText(_translate("AddPhysican", "Add new physician"))
        self.label_given_name.setText(_translate("AddPhysican", "Given name"))
        self.label_last_name_2.setText(_translate("AddPhysican", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPhysican = QtWidgets.QWidget()
    ui = Ui_AddPhysican()
    ui.setupUi(AddPhysican)
    AddPhysican.show()
    sys.exit(app.exec_())
