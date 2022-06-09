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
        self.patientsLabel.setGeometry(QtCore.QRect(530, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patientsLabel.setFont(font)
        self.patientsLabel.setObjectName("patientsLabel")
        self.return_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_push_button.setGeometry(QtCore.QRect(492, 520, 161, 32))
        self.return_push_button.setObjectName("return_push_button")
        self.document_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.document_line_edit.setGeometry(QtCore.QRect(490, 320, 161, 21))
        self.document_line_edit.setText("")
        self.document_line_edit.setObjectName("document_line_edit")
        self.document_label = QtWidgets.QLabel(self.centralwidget)
        self.document_label.setGeometry(QtCore.QRect(510, 280, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.document_label.setFont(font)
        self.document_label.setObjectName("document_label")
        self.document_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.document_combo_box.setGeometry(QtCore.QRect(490, 350, 161, 26))
        self.document_combo_box.setObjectName("document_combo_box")
        self.save_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_push_button.setGeometry(QtCore.QRect(490, 470, 161, 32))
        self.save_push_button.setObjectName("save_push_button")
        self.pesel_append_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pesel_append_line_edit.setGeometry(QtCore.QRect(490, 430, 161, 21))
        self.pesel_append_line_edit.setText("")
        self.pesel_append_line_edit.setObjectName("pesel_append_line_edit")
        self.type_append_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.type_append_combo_box.setGeometry(QtCore.QRect(490, 400, 161, 26))
        self.type_append_combo_box.setObjectName("type_append_combo_box")
        self.days_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.days_combo_box.setGeometry(QtCore.QRect(490, 70, 161, 26))
        self.days_combo_box.setObjectName("days_combo_box")
        self.visits_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.visits_combo_box.setGeometry(QtCore.QRect(490, 110, 161, 26))
        self.visits_combo_box.setObjectName("visits_combo_box")
        self.patients_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.patients_combo_box.setGeometry(QtCore.QRect(490, 150, 161, 26))
        self.patients_combo_box.setObjectName("patients_combo_box")
        MedicianWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MedicianWindow)
        self.statusbar.setObjectName("statusbar")
        MedicianWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MedicianWindow)
        QtCore.QMetaObject.connectSlotsByName(MedicianWindow)

    def retranslateUi(self, MedicianWindow):
        _translate = QtCore.QCoreApplication.translate
        MedicianWindow.setWindowTitle(_translate("MedicianWindow", "Medician"))
        self.patientsLabel.setText(_translate("MedicianWindow", "Visits"))
        self.return_push_button.setText(_translate("MedicianWindow", "Return"))
        self.document_line_edit.setPlaceholderText(_translate("MedicianWindow", "Document ID"))
        self.document_label.setText(_translate("MedicianWindow", "Edit document"))
        self.save_push_button.setText(_translate("MedicianWindow", "Save"))
        self.pesel_append_line_edit.setPlaceholderText(_translate("MedicianWindow", "PESEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MedicianWindow = QtWidgets.QMainWindow()
    ui = Ui_MedicianWindow()
    ui.setupUi(MedicianWindow)
    MedicianWindow.show()
    sys.exit(app.exec_())

