import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from utils import make_str_from_documents



class Ui_Show_appointments(QMainWindow):
    def __init__(self, mongo_manager):
        super().__init__()
        self.setObjectName("Show_appointments")
        self.resize(752, 611)
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(320, 0, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.push_button_display = QtWidgets.QPushButton(self)
        self.push_button_display.setGeometry(QtCore.QRect(580, 80, 71, 21))
        self.push_button_display.setObjectName("push_button_display")
        self.return_push_button = QtWidgets.QPushButton(self)
        self.return_push_button.setGeometry(QtCore.QRect(660, 80, 71, 21))
        self.return_push_button.setObjectName("return_push_button")
        self.display_text_edit = QtWidgets.QTextEdit(self)
        self.display_text_edit.setGeometry(QtCore.QRect(30, 150, 691, 431))
        self.display_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.display_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display_text_edit.setReadOnly(True)
        self.display_text_edit.setObjectName("display_text_edit")
        self.combo_box_pesel = QtWidgets.QComboBox(self)
        self.combo_box_pesel.setGeometry(QtCore.QRect(40, 80, 121, 20))
        self.combo_box_pesel.setFont(font)
        self.combo_box_pesel.setObjectName("combo_box_pesel")
        self.combo_box_pesel.addItem("")
        self.date_edit = QtWidgets.QDateEdit(self)
        self.date_edit.setGeometry(QtCore.QRect(180, 80, 110, 21))
        self.date_edit.setObjectName("date_edit")
        self.combo_box_physicans_name = QtWidgets.QComboBox(self)
        self.combo_box_physicans_name.setGeometry(QtCore.QRect(300, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box_physicans_name.setFont(font)
        self.combo_box_physicans_name.setObjectName("combo_box_physicans_name")
        self.combo_box_physicans_name.addItem("")
        self.label_date = QtWidgets.QLabel(self)
        self.label_date.setGeometry(QtCore.QRect(180, 50, 55, 16))
        self.label_date.setObjectName("label_date")
        self.label_physicians_name = QtWidgets.QLabel(self)
        self.label_physicians_name.setGeometry(QtCore.QRect(300, 50, 121, 16))
        self.label_physicians_name.setObjectName("label_physicians_name")
        self.label_filter = QtWidgets.QLabel(self)
        self.label_filter.setGeometry(QtCore.QRect(40, 50, 55, 16))
        self.label_filter.setObjectName("label_filter")
        self.combo_box_specialization = QtWidgets.QComboBox(self)
        self.combo_box_specialization.setGeometry(QtCore.QRect(430, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box_specialization.setFont(font)
        self.combo_box_specialization.setObjectName("combo_box_specialization")
        self.combo_box_specialization.addItem("")
        self.label_physicians_specialization = QtWidgets.QLabel(self)
        self.label_physicians_specialization.setGeometry(QtCore.QRect(430, 50, 151, 16))
        self.label_physicians_specialization.setObjectName("label_physicians_specialization")
        self.pesel_radio_button = QtWidgets.QRadioButton(self)
        self.pesel_radio_button.setGeometry(QtCore.QRect(40, 110, 100, 20))
        self.pesel_radio_button.setText("")
        self.pesel_radio_button.setObjectName("pesel_radio_button")
        self.date_radio_button = QtWidgets.QRadioButton(self)
        self.date_radio_button.setGeometry(QtCore.QRect(180, 110, 100, 20))
        self.date_radio_button.setText("")
        self.date_radio_button.setObjectName("date_radio_button")
        self.phy_name_radio_button = QtWidgets.QRadioButton(self)
        self.phy_name_radio_button.setGeometry(QtCore.QRect(300, 110, 100, 20))
        self.phy_name_radio_button.setText("")
        self.phy_name_radio_button.setObjectName("phy_name_radio_button")
        self.pesel_group = QtWidgets.QButtonGroup()
        self.pesel_group.setExclusive(False)
        self.pesel_group.addButton(self.pesel_radio_button)
        self.date_group = QtWidgets.QButtonGroup()
        self.date_group.setExclusive(False)
        self.date_group.addButton(self.date_radio_button)
        self.phy_name_group = QtWidgets.QButtonGroup()
        self.phy_name_group.setExclusive(False)
        self.phy_name_group.addButton(self.phy_name_radio_button)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Show_appointments", "Form"))
        self.label_header.setText(_translate("Show_appointments", "Appointments"))
        self.push_button_display.setText(_translate("Show_appointments", "Display"))
        self.return_push_button.setText(_translate("Show_appointments", "Return"))
        self.combo_box_pesel.setItemText(0, _translate("Show_appointments", ""))
        self.combo_box_physicans_name.setItemText(0, _translate("Show_appointments", ""))
        self.label_date.setText(_translate("Show_appointments", "Date"))
        self.label_physicians_name.setText(_translate("Show_appointments", "Physician\'s name"))
        self.label_filter.setText(_translate("Show_appointments", "Filter:"))
        self.combo_box_specialization.setItemText(0, _translate("Show_appointments", ""))
        self.label_physicians_specialization.setText(_translate("Show_appointments", "Physician\'s specialization"))
        
        self.mongo_manager = mongo_manager
        self.return_push_button.clicked.connect(self.return_push_button_clicked)
        self.push_button_display.clicked.connect(self.push_button_display_clicked)
        self.combo_box_pesel.addItems( [str(pesel) for pesel in self.mongo_manager.Patient.distinct('pesel')] )
        self.combo_box_specialization.addItems( self.mongo_manager.Specialization.distinct('specialization') )
        self.combo_box_specialization.currentIndexChanged.connect(self.populate_combo_box_physicans_name)
    
    
    def populate_combo_box_physicans_name(self):
        self.pwz_dict = {}
        self.combo_box_physicans_name.clear()
        medicians = self.mongo_manager.Medician.find(
                        {'specializations.specialization': 
                            {'$eq': self.combo_box_specialization.currentText()}
                        }
                    )
        for med in medicians:
            key_name = med['name'] + ' ' + med['last_name'] + ' ' + str(med['pwz'])
            self.pwz_dict[key_name] = med['pwz']
        
        self.combo_box_physicans_name.addItems(self.pwz_dict.keys())
    
    
    def return_push_button_clicked(self):
        self.close()
    
    
    def push_button_display_clicked(self):
        mongo_dicts = self.push_button_display_logic()
        output_string = make_str_from_documents(mongo_dicts, self.mongo_manager)
        self.display_text_edit.setPlainText(output_string)
        
    
    def push_button_display_logic(self):
        
        if not(self.pesel_radio_button.isChecked() or self.date_radio_button.isChecked() or self.phy_name_radio_button.isChecked()):
            mongo_output = self.no_radio_checked()
        
        if self.pesel_radio_button.isChecked() and not(self.date_radio_button.isChecked() or self.phy_name_radio_button.isChecked()):
            mongo_output = self.only_pesel_checked()
        
        if self.date_radio_button.isChecked() and not(self.pesel_radio_button.isChecked() or self.phy_name_radio_button.isChecked()):
            mongo_output = self.only_date_checked()
        
        if self.phy_name_radio_button.isChecked() and not(self.pesel_radio_button.isChecked() or self.date_radio_button.isChecked()):
            mongo_output = self.only_phy_name_checked()
        
        if self.pesel_radio_button.isChecked() and self.date_radio_button.isChecked() and not(self.phy_name_radio_button.isChecked()):
            mongo_output = self.pesel_date_checked()
        
        if self.pesel_radio_button.isChecked() and not(self.date_radio_button.isChecked()) and self.phy_name_radio_button.isChecked():
            mongo_output = self.pesel_phy_name_checked()
        
        if not(self.pesel_radio_button.isChecked()) and self.date_radio_button.isChecked() and self.phy_name_radio_button.isChecked():
            mongo_output = self.date_phy_name_checked()
        
        if self.pesel_radio_button.isChecked() and self.date_radio_button.isChecked() and self.phy_name_radio_button.isChecked():
            mongo_output = self.all_radio_checked()
        
        return mongo_output
    
    
    def no_radio_checked(self):
        output = self.mongo_manager.TextInformation.find()
        return output

    def only_pesel_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "pesel": self.combo_box_pesel.currentText(),
                    }
                )
        return output
    
    def only_date_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "creation_date": {
                            "$gte": self.date_edit.date().toPyDate(),
                            "$lt" : self.date_edit.date().toPyDate() + datetime.timedelta(days=1)
                        }
                    }
                )
        return output
    
    def only_phy_name_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "pwz": self.pwz_dict[self.combo_box_physicans_name.currentText()]
                    }
                )
        return output
    
    def pesel_date_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "pesel": self.combo_box_pesel.currentText(),
                        "creation_date": {
                            "$gte": self.date_edit.date().toPyDate(),
                            "$lt" : self.date_edit.date().toPyDate() + datetime.timedelta(days=1)
                        }
                    }
                )
        return output
    
    def pesel_phy_name_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "pesel": self.combo_box_pesel.currentText(),
                        "pwz": self.pwz_dict[self.combo_box_physicans_name.currentText()]
                    }
                )
        return output
    
    def date_phy_name_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "creation_date": {
                            "$gte": self.date_edit.date().toPyDate(),
                            "$lt" : self.date_edit.date().toPyDate() + datetime.timedelta(days=1)
                        },
                        "pwz": self.pwz_dict[self.combo_box_physicans_name.currentText()]
                    }
                )
        return output
    
    def all_radio_checked(self):
        output = self.mongo_manager.TextInformation.find(
                    {
                        "pesel": self.combo_box_pesel.currentText(),
                        "creation_date": {
                            "$gte": self.date_edit.date().toPyDate(),
                            "$lt" : self.date_edit.date().toPyDate() + datetime.timedelta(days=1)
                        },
                        "pwz": self.pwz_dict[self.combo_box_physicans_name.currentText()]
                    }
                )
        return output

