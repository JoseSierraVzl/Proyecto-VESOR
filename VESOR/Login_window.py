import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit,
QMainWindow, QAction, QLabel, QFrame)
from Source_rc import *
from Interface import *
import sqlite3

class Login_window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("Login_window.ui", self)
		self.setWindowTitle("Iniciar sección")
		self.setWindowIcon(QtGui.QIcon('Imagenes-iconos/Icono_window.png'))
		
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(16)
		self.frame.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(16)
		self.Button_iniciar.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(16)
		self.pushButton_2.setGraphicsEffect(self.shadow)
		



		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.Button_iniciar.clicked.connect(self.login_iniciar)
			
		self.pushButton_2.clicked.connect(self.Exit)
		
			 # Funciones a llamar----------------------------------------------------------------		
	def Information(self,info):
		msg = QMessageBox()

		msg.setWindowIcon(QtGui.QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setIcon(QMessageBox.Information)
		msg.setText("Iniciar")
		msg.setInformativeText(info)
		msg.setWindowTitle("Inicio")

		msg.setStandardButtons(QMessageBox.Yes)
		msg.setStyleSheet("QDialog{\n"
			"background-color: rgb(243,243,243);\n"
			"border-image: url(:/FONDO/Fondo.jpg);\n"
			"\n"
			"}\n"
			"\n"
			"")
		if (msg.exec_() == QMessageBox.Yes):
			self.interface = Interface()
			self.interface.show()
			self.destroy() 	            

	def Warning(self):
		msg = QMessageBox()

		msg.setWindowIcon(QtGui.QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setIcon(QMessageBox.Warning)
		msg.setText("Error")
		msg.setInformativeText("Usuario o contraseña incorrectos")
		msg.setWindowTitle("¡¡Advertencia!!")

		msg.setStandardButtons(QMessageBox.Discard)			 
		msg.setStyleSheet("QDialog{\n"
			"background-color: rgb(243,243,243);\n"
			"border-image: url(:/FONDO/Fondo.jpg);\n"
			"\n"
			"}\n"
			"\n"
			"")

		msg.exec_()

	def Exit(self):
		msg = QMessageBox()

		msg.setWindowIcon(QtGui.QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("Salir")
		msg.setInformativeText("Está seguro de que desea salir?")
		msg.setWindowTitle("¡Advertencia!")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msg.setStyleSheet("QDialog{\n"
			"background-color: rgb(243,243,243);\n"
			"border-image: url(:/FONDO/Fondo.jpg);\n"
			"\n"
			"}\n"
			"\n"
			"")
		if (msg.exec_() == QMessageBox.Yes):
			exit()
		else:
			pass



		# Fin de funciones llamadas-----------------------------------------------------------------
	def login_iniciar(self):

		with sqlite3.connect('Users_database.db') as db:
			cursor = db.cursor()
					
		User = str(self.lineEdit.text())
		Password = str(self.lineEdit_2.text())
		cursor.execute('SELECT * FROM DATA_USERS WHERE USERS = ? and PASSWORD = ?',(User,Password))
		data = cursor.fetchone()

		if data != None:
			info = '''
				   ¡Bienvenido! %s,
				   Presione Yes para continuar...
				   ''' %(data[0])
			self.Information(info)
		else:
			self.Warning()

if __name__ == "__main__":
	app = QtWidgets.QApplication([]) 
	login_window = Login_window()
	login_window.show() 
	app.exec_() 