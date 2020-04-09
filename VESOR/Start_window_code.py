import sys, re
import sqlite3
from Source_rc import *
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit,
QMainWindow, QAction, QLabel, QFrame,)
from PyQt5 import  uic, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QImage, QColor, QPixmap

 
class Start_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Start_window.ui", self)
      
       
        self.line_user.textChanged.connect(self.Data_user)
        self.line_password.textChanged.connect(self.Data_password)
        self.line_password2.textChanged.connect(self.Validate_password)
        self.Button_register.clicked.connect(self.Login)
        self.Button_cancelar.clicked.connect(self.Exit)
     
        
#============================== #Def. Funciones# ===========================================================================

    def Data_user(self):

        User = self.line_user.text()

        validate = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$', User, re.I)

        if len(User)<8 or len(User)>16 :
            self.line_user.setStyleSheet("border: 1px solid red;")
            self.label_register_status.setText("Su usuario tiene que ser mayor a 8 \n y menor a 16 caracteres")
            return False

        elif not validate:

            self.line_user.setStyleSheet("border: 1px solid red;")
            self.label_register_status.setText("El Usuario tiene que ser alfanumérico \n (Ejemplo: Usuario123)")
            return False

        else:
            self.line_user.setStyleSheet("border: 1px solid green;")
            self.label_register_status.setText(" ")
            return User


    def Data_password(self):

        Password = self.line_password.text()
        
        validate = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$',Password)

        if len(Password)<8 or len(Password)>12:
            self.line_password.setStyleSheet("border: 1px solid red;")
            self.label_register_status.setText("Su contraseña tiene que ser mayor 8 \n y menor a 12 caracteres")
            return False

        elif not validate:
            self.line_password.setStyleSheet("border: 1px solid red;")
            self.label_register_status.setText("Tiene que tener: caracteres en minúscula, \n mayúscula, números y especiales(*+?!)")

            return False

        else:
            self.line_password.setStyleSheet("border: 1px solid green;")  
            self.label_register_status.setText(" ")

            return Password


    def Validate_password(self):
        Password2 = self.line_password2.text()

        if Password2 == self.Data_password():
            self.line_password2.setStyleSheet("border: 1px solid green;")
            self.label_register_status.setText(" ")
            return Password2

        else:
            self.line_password2.setStyleSheet("border: 1px solid red;")
            self.label_register_status.setText("¡Contraseña no coincide!")
            return False


    def Login(self):

        if self.Data_user() and self.Data_password() and self.Validate_password():
            QMessageBox.information(self, "Registro", "Registro exitoso", QMessageBox.Yes)

            print("Usuario: ", self.Data_user())
            print("Contraseña: ", self.Data_password())

        else:
            QMessageBox.warning(self, "Error", "Datos incorrecto", QMessageBox.Discard)


    def Exit(self):
        Question = QMessageBox.question(self, "¡¡Advertencia!!", "¿Seguro que desea salir?",
         QMessageBox.Yes | QMessageBox.No)
        if Question == QMessageBox.Yes:
            exit()
        else: pass 


#===========================================================================================================================


app = QApplication(sys.argv)
startwindow = Start_window()
startwindow.show()
app.exec_()

