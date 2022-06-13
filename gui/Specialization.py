from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_Specialization(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Specialization")
        self.resize(314, 300)
        self.label_specialization = QtWidgets.QLabel(self)
        self.label_specialization.setGeometry(QtCore.QRect(30, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_specialization.setFont(font)
        self.label_specialization.setObjectName("label_specialization")
        self.line_edit_specialization = QtWidgets.QLineEdit(self)
        self.line_edit_specialization.setGeometry(QtCore.QRect(110, 50, 171, 20))
        self.line_edit_specialization.setObjectName("line_edit_specialization")
        self.label_description = QtWidgets.QLabel(self)
        self.label_description.setGeometry(QtCore.QRect(30, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.return_push_button = QtWidgets.QPushButton(self)
        self.return_push_button.setGeometry(QtCore.QRect(170, 240, 121, 32))
        self.return_push_button.setObjectName("return_push_button")
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(40, 240, 111, 31))
        self.push_button_add.setObjectName("push_button_add")
        self.text_edit_description = QtWidgets.QTextEdit(self)
        self.text_edit_description.setGeometry(QtCore.QRect(30, 110, 261, 91))
        self.text_edit_description.setObjectName("text_edit_description")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Specialization", "Form"))
        self.label_specialization.setText(_translate("Specialization", "Specialization"))
        self.label_description.setText(_translate("Specialization", "Description"))
        self.return_push_button.setText(_translate("Specialization", "Return"))
        self.push_button_add.setText(_translate("Specialization", "Add"))
       
        self.mongo_manager = mongo_manager
        self.return_push_button.clicked.connect(self.return_push_button_clicked)
        self.push_button_add.clicked.connect(self.push_button_add_clicked)
    
    def create_specialization_dict(self):
        specialization_data = {
            'specialization' : self.line_edit_specialization.text(),
            'description' : self.text_edit_description.text()
        }
        return specialization_data

    def return_push_button_clicked(self):
        self.close()

    def push_button_add_clicked(self):
        try:
            specialization_data = self.create_specialization_dict()
            self.mongo_manager.Specialization.insert_one(specialization_data)
            self.close()
        except Exception as e:
            print (e)


