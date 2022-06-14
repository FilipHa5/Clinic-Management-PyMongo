from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_AddPhysican(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("AddPhysican")
        self.resize(323, 380)
        self.push_button_add = QtWidgets.QPushButton(self)
        self.push_button_add.setGeometry(QtCore.QRect(40, 320, 121, 31))
        self.push_button_add.setObjectName("push_button_add")
        self.label_no_pwz = QtWidgets.QLabel(self)
        self.label_no_pwz.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_no_pwz.setFont(font)
        self.label_no_pwz.setObjectName("label_no_pwz")
        self.label_last_name = QtWidgets.QLabel(self)
        self.label_last_name.setGeometry(QtCore.QRect(40, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_last_name.setFont(font)
        self.label_last_name.setObjectName("label_last_name")
        self.line_edit_pwz = QtWidgets.QLineEdit(self)
        self.line_edit_pwz.setGeometry(QtCore.QRect(170, 50, 121, 20))
        self.line_edit_pwz.setObjectName("line_edit_pwz")
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(90, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.line_edit_given_name = QtWidgets.QLineEdit(self)
        self.line_edit_given_name.setGeometry(QtCore.QRect(170, 90, 121, 20))
        self.line_edit_given_name.setObjectName("line_edit_given_name")
        self.label_given_name = QtWidgets.QLabel(self)
        self.label_given_name.setGeometry(QtCore.QRect(40, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_given_name.setFont(font)
        self.label_given_name.setObjectName("label_given_name")
        self.line_edit_last_name = QtWidgets.QLineEdit(self)
        self.line_edit_last_name.setGeometry(QtCore.QRect(170, 130, 121, 20))
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.text_edit_description = QtWidgets.QTextEdit(self)
        self.text_edit_description.setGeometry(QtCore.QRect(40, 200, 251, 91))
        self.text_edit_description.setObjectName("text_edit_description")
        self.label_last_description = QtWidgets.QLabel(self)
        self.label_last_description.setGeometry(QtCore.QRect(40, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_last_description.setFont(font)
        self.label_last_description.setObjectName("label_last_description")
        self.return_push_button = QtWidgets.QPushButton(self)
        self.return_push_button.setGeometry(QtCore.QRect(180, 320, 111, 32))
        self.return_push_button.setObjectName("return_push_button")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddPhysican", "Form"))
        self.push_button_add.setText(_translate("AddPhysican", "Add"))
        self.label_no_pwz.setText(_translate("AddPhysican", "No PWZ"))
        self.label_last_name.setText(_translate("AddPhysican", "Last name"))
        self.label_header.setText(_translate("AddPhysican", "Add new physician"))
        self.label_given_name.setText(_translate("AddPhysican", "Given name"))
        self.label_last_description.setText(_translate("AddPhysican", "Description"))
        self.return_push_button.setText(_translate("AddPhysican", "Return"))
        
        self.mongo_manager = mongo_manager
        self.return_push_button.clicked.connect(self.return_push_button_clicked)
        self.push_button_add.clicked.connect(self.push_button_add_clicked)
        
    
    def return_push_button_clicked(self):
        self.close()
    
    
    def create_medician_dict(self):
        medician_data = {
            'pwz': int(self.line_edit_pwz.text()),
            'name': self.line_edit_given_name.text(),
            'last_name': self.line_edit_last_name.text(),
            'description': self.text_edit_description.toPlainText(),
            'password': ''
        }
        return medician_data
    
    def push_button_add_clicked(self):
        try:
            medician_data = self.create_medician_dict()
            self.mongo_manager.Medician.insert_one(medician_data)
            self.close()
        except Exception as e:
            print(e)

