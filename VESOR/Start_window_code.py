##VESOR##

import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit
from PyQt5 import uic


class Start_window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("Start_window.ui", self)

##############################################################################################
		self.line_user.textChanged.connect(self.Validate_user)
		self.line_password.textChanged.connect(self.Validate_Password)
		self.line_password2.textChanged.connect(self.Validate_password2) 
		self.Button_Cancel.clicked.connect(exit) #conecta con el boton para cerrar la aplicacion
##############################################################################################
		
##########################Declarando funciones para los lineEdit##############################
	def Validate_user(self):
		line_user = self.line_user.text()
		validate = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+[0-9]+$', line_user, re.I)
		if line_user == "":
			self.line_user.setStyleSheet("border: 1px solid yellow;")
			return False
		elif len(line_user)<8:
			self.line_user.setStyleSheet("border: 1px solid red;")
			return False
		elif not validate:
			self.line_user.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.line_user.setStyleSheet("border: 1px solid green;")
			return True

	def Validate_Password(self):
		line_password = self.line_password.text()
		validate = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$', line_password, re.I) 
		if line_password == "":
			self.line_password.setStyleSheet("border: 1px solid yellow;")
			return False
		elif len(line_password)<8:
			self.line_password.setStyleSheet("border: 1px solid red;")
			return False
		elif not validate:
			self.line_password.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.line_password.setStyleSheet("border: 1px solid green;")
			return True

	def Validate_password2(self):
		# Puedes quitar el "pass" cuando quieras
		pass 
################################################################################################


app = QApplication(sys.argv)
startwindow = Start_window()
startwindow.show()
app.exec_()
