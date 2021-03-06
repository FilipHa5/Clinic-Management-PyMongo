from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from .utils import make_str_from_documents



class Ui_Patient(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Patient")
        self.resize(752, 611)
        self.text_display = QtWidgets.QTextEdit(self)
        self.text_display.setGeometry(QtCore.QRect(30, 150, 681, 441))
        self.text_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_display.setReadOnly(True)
        self.text_display.setObjectName("text_display")
        self.line_edit_pesel = QtWidgets.QLineEdit(self)
        self.line_edit_pesel.setGeometry(QtCore.QRect(30, 110, 131, 20))
        self.line_edit_pesel.setText("")
        self.line_edit_pesel.setObjectName("line_edit_pesel")
        self.line_edit_last_name = QtWidgets.QLineEdit(self)
        self.line_edit_last_name.setGeometry(QtCore.QRect(400, 110, 131, 20))
        self.line_edit_last_name.setText("")
        self.line_edit_last_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.line_edit_given_name = QtWidgets.QLineEdit(self)
        self.line_edit_given_name.setGeometry(QtCore.QRect(210, 110, 131, 20))
        self.line_edit_given_name.setText("")
        self.line_edit_given_name.setObjectName("line_edit_given_name")
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(310, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.push_button_display = QtWidgets.QPushButton(self)
        self.push_button_display.setGeometry(QtCore.QRect(560, 110, 71, 21))
        self.push_button_display.setObjectName("push_button_display")
        self.label_desc = QtWidgets.QLabel(self)
        self.label_desc.setGeometry(QtCore.QRect(250, 60, 321, 16))
        self.label_desc.setObjectName("label_desc")
        self.return_push_button = QtWidgets.QPushButton(self)
        self.return_push_button.setGeometry(QtCore.QRect(640, 110, 71, 21))
        self.return_push_button.setObjectName("return_push_button")
        QtCore.QMetaObject.connectSlotsByName(self)
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Patient", "Form"))
        self.line_edit_pesel.setPlaceholderText(_translate("Patient", "PESEL"))
        self.line_edit_last_name.setPlaceholderText(_translate("Patient", "Last name"))
        self.line_edit_given_name.setPlaceholderText(_translate("Patient", "Given name"))
        self.label_header.setText(_translate("Patient", "Patient menu"))
        self.push_button_display.setText(_translate("Patient", "Display"))
        self.label_desc.setText(_translate("Patient", "Insert your data to display your medical history"))
        self.return_push_button.setText(_translate("Patient", "Return"))
        
        self.mongo_manager = mongo_manager
        self.push_button_display.clicked.connect(self.push_button_display_clicked)
        self.return_push_button.clicked.connect(self.return_push_button_clicked)
    
    
    def return_push_button_clicked(self):
        self.close()
    
    
    def push_button_display_clicked(self):
        if not (self.line_edit_pesel.text() != '' and 
            self.line_edit_given_name.text() != '' and 
            self.line_edit_last_name.text() != ''):
            return
        else:
            self.perform_action_data()
    
    
    def get_mongo_dicts(self):
        try:
            informations_dict = self.mongo_manager.TextInformation.find({'pesel': int(self.line_edit_pesel.text())})
            return informations_dict
        except Exception as e:
            print (e)
    
    
    def perform_action_data(self):
        self.display_text_edit.clear()
        mongo_dicts = self.push_button_display_logic()
        output_string = make_str_from_documents(mongo_dicts, self.mongo_manager)
        self.display_text_edit.setPlainText(output_string)


