from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Ui_LinkPhysician(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("LinkPhysician")
        self.resize(323, 227)
        self.push_button_link = QtWidgets.QPushButton(self)
        self.push_button_link.setGeometry(QtCore.QRect(40, 160, 121, 31))
        self.push_button_link.setObjectName("push_button_link")
        self.push_button_return = QtWidgets.QPushButton(self)
        self.push_button_return.setGeometry(QtCore.QRect(170, 160, 121, 31))
        self.push_button_return.setObjectName("push_button_return")
        self.label_no_pwz = QtWidgets.QLabel(self)
        self.label_no_pwz.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_no_pwz.setFont(font)
        self.label_no_pwz.setObjectName("label_no_pwz")
        self.label_header = QtWidgets.QLabel(self)
        self.label_header.setGeometry(QtCore.QRect(40, 10, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.combo_box_no_pwz = QtWidgets.QComboBox(self)
        self.combo_box_no_pwz.setGeometry(QtCore.QRect(170, 50, 121, 22))
        self.combo_box_no_pwz.setObjectName("combo_box_no_pwz")
        self.label_specialization = QtWidgets.QLabel(self)
        self.label_specialization.setGeometry(QtCore.QRect(40, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_specialization.setFont(font)
        self.label_specialization.setObjectName("label_specialization")
        self.combo_box_specialization = QtWidgets.QComboBox(self)
        self.combo_box_specialization.setGeometry(QtCore.QRect(170, 100, 121, 22))
        self.combo_box_specialization.setObjectName("combo_box_specialization")
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LinkPhysician", "Form"))
        self.push_button_link.setText(_translate("LinkPhysician", "Link"))
        self.push_button_return.setText(_translate("LinkPhysician", "Return"))
        self.label_no_pwz.setText(_translate("LinkPhysician", "No PWZ"))
        self.label_header.setText(_translate("LinkPhysician", "Link physician to specialization"))
        self.label_specialization.setText(_translate("LinkPhysician", "Specialization"))
        
        self.push_button_return.clicked.connect(self.push_button_return_clicked)


    def push_button_return_clicked(self):
        self.close()


