# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Medician.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MedicianWindow(object):
    def setupUi(self, MedicianWindow):
        MedicianWindow.setObjectName("MedicianWindow")
        MedicianWindow.resize(703, 593)
        self.centralwidget = QtWidgets.QWidget(MedicianWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.display_text_edit.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.display_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.display_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_text_edit.setReadOnly(True)
        self.display_text_edit.setObjectName("display_text_edit")
        self.editable_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.editable_text_edit.setGeometry(QtCore.QRect(10, 280, 461, 281))
        self.editable_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.editable_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.editable_text_edit.setObjectName("editable_text_edit")
        self.patientsLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientsLabel.setGeometry(QtCore.QRect(550, 30, 71, 21))
        self.patientsLabel.setObjectName("patientsLabel")
        self.show_all_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_all_push_button.setGeometry(QtCore.QRect(470, 100, 113, 32))
        self.show_all_push_button.setObjectName("show_all_push_button")
        self.show_abowe_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_abowe_push_button.setGeometry(QtCore.QRect(590, 100, 113, 32))
        self.show_abowe_push_button.setObjectName("show_abowe_push_button")
        self.patient_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_line_edit.setGeometry(QtCore.QRect(490, 70, 161, 21))
        self.patient_line_edit.setObjectName("patient_line_edit")
        self.return_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_push_button.setGeometry(QtCore.QRect(530, 520, 113, 32))
        self.return_push_button.setObjectName("return_push_button")
        self.document_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.document_line_edit.setGeometry(QtCore.QRect(490, 320, 161, 21))
        self.document_line_edit.setObjectName("document_line_edit")
        self.document_label = QtWidgets.QLabel(self.centralwidget)
        self.document_label.setGeometry(QtCore.QRect(540, 280, 101, 21))
        self.document_label.setObjectName("document_label")
        self.document_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.document_combo_box.setGeometry(QtCore.QRect(490, 350, 161, 26))
        self.document_combo_box.setObjectName("document_combo_box")
        self.save_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_push_button.setGeometry(QtCore.QRect(530, 460, 113, 32))
        self.save_push_button.setObjectName("save_push_button")
        self.show_document_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.show_document_line_edit.setGeometry(QtCore.QRect(490, 140, 161, 21))
        self.show_document_line_edit.setObjectName("show_document_line_edit")
        self.show_document_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_document_push_button.setGeometry(QtCore.QRect(520, 170, 131, 32))
        self.show_document_push_button.setObjectName("show_document_push_button")
        self.pesel_append_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pesel_append_line_edit.setGeometry(QtCore.QRect(490, 430, 161, 21))
        self.pesel_append_line_edit.setObjectName("pesel_append_line_edit")
        self.type_append_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.type_append_combo_box.setGeometry(QtCore.QRect(490, 400, 161, 26))
        self.type_append_combo_box.setObjectName("type_append_combo_box")
        MedicianWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MedicianWindow)
        self.statusbar.setObjectName("statusbar")
        MedicianWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MedicianWindow)
        QtCore.QMetaObject.connectSlotsByName(MedicianWindow)

    def retranslateUi(self, MedicianWindow):
        _translate = QtCore.QCoreApplication.translate
        MedicianWindow.setWindowTitle(_translate("MedicianWindow", "Medician"))
        self.patientsLabel.setText(_translate("MedicianWindow", "Patients"))
        self.show_all_push_button.setText(_translate("MedicianWindow", "Show All"))
        self.show_abowe_push_button.setText(_translate("MedicianWindow", "Show Abowe"))
        self.patient_line_edit.setText(_translate("MedicianWindow", "PESEL"))
        self.return_push_button.setText(_translate("MedicianWindow", "Return"))
        self.document_line_edit.setText(_translate("MedicianWindow", "Document ID"))
        self.document_label.setText(_translate("MedicianWindow", "Edit document"))
        self.save_push_button.setText(_translate("MedicianWindow", "Save"))
        self.show_document_line_edit.setText(_translate("MedicianWindow", "Document ID"))
        self.show_document_push_button.setText(_translate("MedicianWindow", "Show Document"))
        self.pesel_append_line_edit.setText(_translate("MedicianWindow", "PESEL"))

