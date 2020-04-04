import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit, QMainWindow, QAction
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sqlite3


class Start_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Start_window.ui", self)


        self.line_user.textChanged.connect(self.Data_user)
        self.line_password.textChanged.connect(self.Data_password)
        self.line_password2.textChanged.connect(self.Validate_password)
        self.Button_register.clicked.connect(self.Login)


    #Variables:

        #User = self.line_user.text()
        #Password = self.line_password.text()
        Password2 = self.line_password2.text()

    def Data_user(self):
        User = self.line_user.text()

        validate = re.match('^[a-z\sáéíóúàèìòùäëïöüñ0-9]+$', User, re.I)

        if len(User)<=8 or len(User)>=14 :
            self.line_user.setStyleSheet("border: 1px solid red;")
            return False

        elif not validate:

            self.line_user.setStyleSheet("border: 1px solid red;")
            return False

        else:
            self.line_user.setStyleSheet("border: 1px solid green;")
            return True
    
    def Data_password(self):
        Password = self.line_password.text()
        
        validate = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$',Password, re.I)

        if len(Password)<=8 or len(Password)>=12:
            self.line_password.setStyleSheet("border: 1px solid red;")
            return False

        elif not validate:
            self.line_password.setStyleSheet("border: 1px solid red;")
            return False

        else:
            self.line_password.setStyleSheet("border: 1px solid green;")
            return True
    

       
    def Validate_password(self,Password2):

        if Password2 != self.Data_password():
            self.line_password2.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.line_password2.setStyleSheet("border: 1px solid green;")
            return True


    def Login(self):
        if self.Data_user() and self.Data_password() and self. Validate_password():
            QMessageBox.information(self, "Registro", "Registro exitoso", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "Error", "Datos incorrecto", QMessageBox.Discard)
        







app = QApplication(sys.argv)
startwindow = Start_window()
startwindow.show()
app.exec_()
