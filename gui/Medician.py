from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_MedicianWindow(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Medician")
        self.resize(703, 593)
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.patients_label = QtWidgets.QLabel(self.centralwidget)
        self.patients_label.setGeometry(QtCore.QRect(530, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.patients_label.setFont(font)
        self.patients_label.setObjectName("patients_label")
        self.return_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_push_button.setGeometry(QtCore.QRect(492, 520, 161, 32))
        self.return_push_button.setObjectName("return_push_button")
        self.document_id_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.document_id_combo_box.setGeometry(QtCore.QRect(490, 320, 161, 26))
        self.document_id_combo_box.setObjectName("document_id_combo_box")
        self.document_label = QtWidgets.QLabel(self.centralwidget)
        self.document_label.setGeometry(QtCore.QRect(510, 288, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.document_label.setFont(font)
        self.document_label.setObjectName("document_label")
        self.document_operation_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.document_operation_combo_box.setGeometry(QtCore.QRect(490, 350, 161, 26))
        self.document_operation_combo_box.setObjectName("document_operation_combo_box")
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
        self.days_combo_box.setGeometry(QtCore.QRect(490, 110, 161, 26))
        self.days_combo_box.setObjectName("days_combo_box")
        self.visits_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.visits_combo_box.setGeometry(QtCore.QRect(490, 140, 161, 26))
        self.visits_combo_box.setObjectName("visits_combo_box")
        self.pwz_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pwz_line_edit.setGeometry(QtCore.QRect(490, 10, 161, 21))
        self.pwz_line_edit.setText("")
        self.pwz_line_edit.setObjectName("pwz_line_edit")
        self.apply_pwz_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_pwz_push_button.setGeometry(QtCore.QRect(490, 40, 161, 32))
        self.apply_pwz_push_button.setObjectName("apply_pwz_push_button")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MedicianWindow", "Medician"))
        self.patients_label.setText(_translate("MedicianWindow", "Visits"))
        self.return_push_button.setText(_translate("MedicianWindow", "Return"))
        self.document_label.setText(_translate("MedicianWindow", "Edit document"))
        self.save_push_button.setText(_translate("MedicianWindow", "Save"))
        self.pesel_append_line_edit.setPlaceholderText(_translate("MedicianWindow", "PESEL"))
        self.pwz_line_edit.setPlaceholderText(_translate("MedicianWindow", "PWZ"))
        self.apply_pwz_push_button.setText(_translate("MedicianWindow", "Apply"))
        
        self.mongo_manager = mongo_manager
        self.return_push_button.clicked.connect(self.return_push_button_clicked)
        self.apply_pwz_push_button.clicked.connect(self.apply_pwz_push_button_clicked)

    def populate_type_append_combo_box(self):
        self.type_append_combo_box.addItem("Description")
        self.type_append_combo_box.addItem("Prescription")
        self.type_append_combo_box.addItem("Referral")

    def apply_pwz_push_button_clicked(self):
        pwz_int = int(self.pwz_line_edit.text())
        appointments = self.mongo_manager.Appointment.find(
                        {
                        'pwz':
                            {'$eq': pwz_int}
                        }
                    )        
        for pwz in appointments:
            self.display_text_edit.append(str(pwz))



    def return_push_button_clicked(self):
        self.close()


