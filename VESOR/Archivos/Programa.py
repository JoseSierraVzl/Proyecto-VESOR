# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       Programa.py
# Autores:      Cristian Cala Sierra / Jose Alejandro Sierra Mendez (Fundadores de CODELOID)
# Creado:       21 de Julio del 2020
# Modificado:   04 de Marzo de 2021
# Copyright:    (c) 2020 CODELOID
# License:      MIT License
# ----------------------------------------------------------------------------
__version__ = "2.0"

import sys
import re
import os
import time
import sqlite3
import webbrowser
import platform

# para exportar a Excell
import xlwt
from xlwt import Workbook

# Encriptación
# import Crypto
# from Crypto.Cipher import DES
# import binascii
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

from Source_rc import *
from os import getcwd, makedirs
import shutil
from random import randint

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, uic


# Primera clase y verificador
class CustomWindow(QMainWindow):

	Color = QColor(0, 170,255)
	Clockwise = True
	Delta = 24
	Color2 = QColor(85, 85, 255)

	def __init__(self, color=None, clockwise=True, **kwargs):
		super(CustomWindow, self).__init__(**kwargs)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WA_TranslucentBackground, True)

		self.Label = QtWidgets.QLabel(self)
		self.Label.setGeometry(QRect(390, 300, 200, 100))
		self.Label.setText("Bienvenidos a ")
		self.Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
				"font: 75 14pt \"MS Shell Dlg 2\";\n"
				"color: rgb(255, 255, 255);")

		self.label_tres = QtWidgets.QLabel(self)
		self.label_tres.setGeometry(QRect(420, 290, 341, 251))
		self.label_tres.setStyleSheet(
			"QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png);}")

		self.Label_cuatro = QtWidgets.QLabel(self)
		self.Label_cuatro.setGeometry(QRect(590, 430, 340, 100))
		self.Label_cuatro.setText("El programa de gestión comunitaria")
		self.Label_cuatro.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
				"font: 75 13pt \"MS Shell Dlg 2\";\n"
				"color: rgb(255, 255, 255);")

		self._timer = QTimer()
		self._timer.singleShot(5000, self.ValidarSerial)

		self.angle = 5
		self.Clockwise = clockwise
		if color:
			self.Color = color
		self._timer = QTimer(self, timeout=self.update)
		self._timer.start(100)

	def paintEvent(self, event):

		pinturito = QPainter(self)
		pinturito.setRenderHint(QPainter.Antialiasing)
		pinturito.translate(620, 650)
		side = min(self.width(), self.height())
		pinturito.scale(side / 100.0, side / 100.0)
		pinturito.rotate(self.angle)
		pinturito.save()
		pinturito.setPen(Qt.NoPen)
		color = self.Color.toRgb()
		for i in range(11):
			color.setAlphaF(1.0 * i / 10)
			pinturito.setBrush(color)
			pinturito.drawEllipse(3, 3, 5, 5)
			pinturito.rotate(10)
		pinturito.restore()
		self.angle += self.Delta if self.Clockwise else -self.Delta
		self.angle %= 360

		pinturito2 = QPainter(self)
		pinturito2.setRenderHint(QPainter.Antialiasing)
		pinturito2.translate(620, 650)
		side = min(self.width(), self.height())
		pinturito2.scale(side / 200.0, side / 200.0)
		pinturito2.rotate(self.angle)
		pinturito2.save()
		pinturito2.setPen(Qt.NoPen)
		color = self.Color2.toRgb()
		for i in range(10):
			color.setAlphaF(1.0 * i / 10)
			pinturito2.setBrush(color)
			pinturito2.drawEllipse(2,2,5,5)
			pinturito2.rotate(15)
		pinturito2.restore()
		self.angle += self.Delta if self.Clockwise else -self.Delta
		self.angle %= 360

		painter = QtGui.QPainter(self)
		painter.setOpacity(0.3)
		painter.setBrush(Qt.black)
		painter.setPen(QPen(Qt.black))
		painter.drawRect(self.rect())

	def ValidarSerial(self):
		sistema = platform.system()
		dato = 'isOk'
		dato2 = 'OSTR0-SFCGX-EACCC-MJ9X1-XW08D'
		ruta = ""
		if sistema == "Linux":
			ruta = ('//')
		else:
			ruta = ('C:/Windows/')

		if os.access(ruta, 2) == True:
			if os.path.isfile(ruta + 'verification_vesor/Serial.txt'):
				verificador = open(ruta + 'verification_vesor/Serial.txt', "rb").read()


				if str(verificador.decode()) == dato:
					if os.path.isfile('Users_database.db'):

						self.login_window = Login_window()
						self.login_window.show()
						self.close()
					else:
						self.start_window = Start_window()
						self.start_window.show()
						self.close()

				elif str(verificador.decode()) == dato2:
					QMessageBox.information(self, "Validación", "Aún no has validado VESOR", QMessageBox.Yes)
					self.serial_validar = serial_validation()
					self.serial_validar.show()
					self.close()

				else:
					QMessageBox.information(self, "Error 404", "A ocurrido un problema", QMessageBox.Yes)
					shutil.rmtree(ruta + 'verification_vesor')
					self.close()


			elif os.path.exists(ruta + 'verification_vesor') and os.path.isdir(ruta + 'verification_vesor'):
				if not os.listdir(ruta + 'verification_vesor'):
					QMessageBox.information(self, "Error de directorio", "Cierre y abra de nuevo la aplicación", QMessageBox.Yes)
					os.rmdir(ruta + 'verification_vesor')
					self.close()

			else:
				self.serial_validar = serial_validation()
				self.serial_validar.show()
				self.close()

		else:
			QMessageBox.information(self, "Control de acceso", "Abra la aplicación con permisos de administrador", QMessageBox.Yes)
			self.close()

# Clase del Login
class Login_window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("ui/Login_window.ui", self)
		self.setWindowTitle("Iniciar sesión")
		self.setWindowIcon(QtGui.QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		self.setWindowFlags(Qt.WindowTitleHint |
							Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.Button_iniciar.clicked.connect(self.login_iniciar)
		self.pushButton_2.clicked.connect(self.Exit)
		self.button_CrearUsuario.clicked.connect(self.OpenUser)

		# Interacciones
		self.lineEdit.setToolTip("Ingresa tu nombre de usuario aquí")
		self.lineEdit_2.setToolTip("Ingresa tu contraseña aquí")

	def OpenUser(self):
		self.user_window = Start_window()
		self.user_window.show()
		self.close()

	def Information(self, info):
		msg = QMessageBox(self)
		msg.setWindowIcon(QtGui.QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setIcon(QMessageBox.Information)
		msg.setWindowTitle("Inicio")
		msg.setText("¡¡Bienvenido!!\n\n" + info + "\n\n Presione Siguiente para continuar")
		botonSiguiente = msg.addButton("Siguiente", QMessageBox.YesRole)

		msg.exec_()
		if msg.clickedButton() == botonSiguiente:
			self.interface = Interface()
			self.interface.show()
			self.close()
		else:
			pass

	def Warning(self):
		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Warning)
		msg.setWindowTitle("¡¡Advertencia!!")
		msg.setText("Usuario o contraseña incorrectos")
		botonSalir = msg.addButton("Ok", QMessageBox.YesRole)

		msg.exec_()
		if msg.clickedButton() == botonSalir:
			pass
		else:
			pass

	def Exit(self):
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de VESOR?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar esta ventana?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)

		cerrar.exec_()

		if cerrar.clickedButton() == botonSalir:
			self.close()
		else:
			pass

		# Fin de funciones llamadas-----------------------------------------------------------------
	def login_iniciar(self):

		with sqlite3.connect('Users_database.db') as db:
			cursor = db.cursor()

		User = str(self.lineEdit.text())
		Password = str(self.lineEdit_2.text())
		cursor.execute(
			'SELECT * FROM DATA_USERS WHERE USERS = ? and PASSWORD = ?', (User, Password))
		data = cursor.fetchone()
		if data != None:
			info = (data[0])
			self.Information(info)
		else:
			self.Warning()

# clase de la ventana de Registro
class Start_window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("ui/Start_window.ui", self)
		self.setWindowTitle("Registro")
		self.setWindowIcon(QtGui.QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		self.setWindowFlags(Qt.WindowTitleHint |
							Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(16)
		self.frame.setGraphicsEffect(self.shadow)

		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(16)
		self.Button_register.setGraphicsEffect(self.shadow)

		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(16)
		self.Button_cancelar.setGraphicsEffect(self.shadow)

		self.line_user.textChanged.connect(self.Data_user)
		self.line_password.textChanged.connect(self.Data_password)
		self.line_password2.textChanged.connect(self.Validate_password)
		self.Button_register.clicked.connect(self.Database_users_create)
		self.Button_cancelar.clicked.connect(self.Exit)

		# Interacciones
		self.line_user.setToolTip("Ingrese un usuario")
		self.line_password.setToolTip("Ingrese un contraseña")


	def Database_users_create(self):

		if self.Data_user() and self.Data_password() and self.Validate_password():
			try:

				with sqlite3.connect('Users_database.db') as db:
					cursor = db.cursor()
				cursor.execute(
					'CREATE TABLE IF NOT EXISTS DATA_USERS( USERS     TEXT   NOT NULL, PASSWORD     TEXT      NOT NULL)')
				db.commit()
				cursor.close()
				db.close()
			except Exception as e:
					print(e)
			try:
				User = str(self.Data_user())
				Password = str(self.Data_password())

				with sqlite3.connect('Users_database.db') as db:

					cursor = db.cursor()

				cursor.execute('INSERT INTO DATA_USERS VALUES(?,?)', (User, Password))
				db.commit()

				cursor.execute('SELECT * FROM DATA_USERS')
				db.commit()
				cursor.close()
				db.close()
			except Exception as e:
				print(e)
				pass

			QMessageBox.information(self, "Registro", "Registro exitoso", QMessageBox.Yes)

			# LLamando a login
			self.interface = Interface()
			self.interface.show()
			self.close()

			return True
		else:
			self.Warning()
			# QMessageBox.warning(self, "Error", "Sus datos no cumplen con las reglas", QMessageBox.Discard)

	def Data_user(self):

		User = self.line_user.text()

		validate = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).*$', User, re.I)

		if len(User) < 8 or len(User) > 16:
			self.line_user.setStyleSheet("border: 1px solid red;")
			self.label_register_status.setText(
				"Su usuario tiene que ser mayor a 8 \n y menor a 16 carácteres")
			return False

		elif not validate:

			self.line_user.setStyleSheet("border: 1px solid red;")
			self.label_register_status.setText(
				"El Usuario tiene que ser alfanumérico \n (Ejemplo: Usuario123)")
			return False

		else:
			self.line_user.setStyleSheet("border: 1px solid green;")
			self.label_register_status.setText(" ")
			return User

	def Data_password(self):

		Password = self.line_password.text()

		validate = re.match(
			'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$', Password)

		if len(Password) < 8 or len(Password) > 12:
			self.line_password.setStyleSheet("border: 1px solid red;")
			self.label_register_status.setText(
				"Su contraseña tiene que ser mayor 8 \n y menor a 12 caracteres")
			return False

		elif not validate:
			self.line_password.setStyleSheet("border: 1px solid red;")
			self.label_register_status.setText(
				"Tiene que tener: caracteres en minúscula, \n mayúscula, números y especiales(*+?!)")

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

	def Warning(self):
		msg = QMessageBox(self)
		msg.setWindowTitle("Validación")
		msg.setIcon(QMessageBox.Warning)
		msg.setText("Los datos no cumplen con las reglas")
		botonSalir = msg.addButton("Salir", QMessageBox.YesRole)

		msg.exec_()
		if msg.clickedButton() == botonSalir:
			pass
		else:
			pass

	def Exit(self):
		msg = QMessageBox(self)
		msg.setWindowTitle("¡¡Advertencia!!")
		msg.setIcon(QMessageBox.Question)
		msg.setText("¿Seguro que desea salir?")
		botonSalir = msg.addButton("Salir", QMessageBox.YesRole)
		botonNo = msg.addButton("No", QMessageBox.NoRole)

		msg.exec_()
		if msg.clickedButton() == botonSalir:
			self.close()
		else:
			pass

# Clase de ventana Serial
class serial_validation(QDialog):
	def __init__(self, parent=None):
		super(serial_validation, self).__init__()
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Validación de VESOR")
		self.setWindowFlags(Qt.WindowTitleHint |
							Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(800, 440)
		self.setStyleSheet("QDialog{\n"
						   "background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
						   "}\n"
						   "")
		self.initUi()
		self.time_image()
		self.crearSerial()

	def crearSerial(self):
		sistema = platform.system()
		ruta = ""

		if sistema == "Linux":
			ruta = ('//')
		else:
			ruta = ('C:/Windows/')


		if os.path.exists (ruta + 'verification_vesor/Serial.txt'):
			pass

		else:
			os.mkdir(ruta + 'verification_vesor')
			dato = 'LPQO0-PCZDU-BXZZZ-JG9U1-UT08A'

			def cifrado(dato):
				pos = 3 
				dato_cifrado = ""

				for c in dato:

					if c.isupper():
						resta_pos = ord(c) - ord("A")
						nueva_pos = (resta_pos + pos) % 26
						nueva_unicode = nueva_pos + ord("A")
						convertir_str = chr(nueva_unicode)
						dato_cifrado = dato_cifrado + convertir_str
					else:
						dato_cifrado += c

				return dato_cifrado

			dato_encriptado = cifrado(dato)

			with open(ruta + "verification_vesor/Serial.txt", "w") as archivo_cifrado:
				archivo_cifrado.write(dato_encriptado)
				archivo_cifrado.close()

	def initUi(self):
		# Style de carousel
		style_frame_carousel = ("QFrame\n"
								"{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		# Style Label Vesor
		style_label_vesor = (
			"QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png)}")

		# Style label text
		style_label_text = ("QLabel{\n"
							"color:#12191D;\n"
							"border-radius: 6px;\n"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							"}")
		style_label_text_especial = ("QLabel{\n"
									 "color: rgb(255,255,255);\n"
									 "border-radius: 6px;\n"
									 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
									 "}")

		# Style LineEdit_serial
		style_lineEdit_serial = ("QLineEdit{\n"
									"border-radius: 7px;\n"
									"color:  white;\n"
									"background-color:rgba(0,0,0,0.6);\n"
									"}\n"
									"QLineEdit:hover{\n"
									"color: black;\n"
									"background-color: rgba(255,255,255,0.6);\n"
									"border: 1px solid rgb(85, 0, 127);\n"
									"}")

		# Style QPushButton
		style_QPushButton = ("QPushButton{\n"
							"border: 2px solid white;"
							"}\n"
							"QPushButton:hover{\n"
							"background-color:rgb(0, 0, 0);\n"
							"color:rgb(255, 255, 255);\n"
							"}")

		# Style_labelImagen_1
		style_labelImagen_1 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_1.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		# style_labelImagen_2
		style_labelImagen_2 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_2.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		# style_labelImagen_3
		style_labelImagen_3 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_3.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")

		# style_labelImagen_4
		style_labelImagen_4 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_4.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")

		# style_labelImagen_5
		style_labelImagen_5 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_5.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")

		# style_labelImagen_6
		style_labelImagen_6 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_6.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")

		self.frame_carousel = QFrame(self)
		self.frame_carousel.setGeometry(QRect(20, 90, 491, 370))
		self.frame_carousel.setStyleSheet(style_frame_carousel)
		self.frame_carousel.move(300, 20)

		self.label_vesor = QLabel(self)
		self.label_vesor.setGeometry(QRect(100, 100, 200, 150))
		self.label_vesor.setStyleSheet(style_label_vesor)
		self.label_vesor.move(50, -20)

		self.label_encabezado = QLabel(self)
		self.label_encabezado.setGeometry(QRect(100, 300, 300, 150))
		self.label_encabezado.setStyleSheet(style_label_text_especial)
		self.label_encabezado.setText("Ingrese el serial para validar")
		self.label_encabezado.setFont(
			QtGui.QFont("Comic Sans", 11, QtGui.QFont.Bold))
		self.label_encabezado.move(30, 50)

		self.text_explicacion = QLabel(self)
		self.text_explicacion.setGeometry(QRect(100, 300, 300, 150))
		self.text_explicacion.setStyleSheet(style_label_text_especial)
		self.text_explicacion.setAlignment(Qt.AlignJustify)
		self.text_explicacion.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.text_explicacion.setText(
			"Recibirá el código de parte de los\ndesarrolladores de Vesor,\ny a continuación podrá validar\nVESOR con facilidad para que pueda\ndisfrutar de todo lo que el programa\npuede ofrecerle.")
		self.text_explicacion.move(20, 150)

		self.text_encabezado = QLabel(self)
		self.text_encabezado.setGeometry(QRect(100, 300, 300, 150))
		self.text_encabezado.setStyleSheet(style_label_text_especial)
		self.text_encabezado.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.text_encabezado.setText(
			"El serial es similar a esto:\nSerial:\nXXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
		self.text_encabezado.move(20, 190)

		self.label_text = QLabel(self)
		self.label_text.setGeometry(QRect(20, 460, 411, 20))
		self.label_text.setStyleSheet(style_label_text_especial)
		self.label_text.setText("Serial del producto:")
		self.label_text.setFont(QtGui.QFont("Comic Sans", 11, QtGui.QFont.Bold))
		self.label_text.move(20, 380)

		self.lineEdit_serial = QLineEdit(self)
		self.lineEdit_serial.setGeometry(QRect(10, 200, 300, 20))
		self.lineEdit_serial.setAlignment(Qt.AlignCenter)
		self.lineEdit_serial.setMaxLength(29)
		self.lineEdit_serial.setInputMask('XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')
		self.lineEdit_serial.setStyleSheet(style_lineEdit_serial)
		self.lineEdit_serial.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.lineEdit_serial.setToolTip(
			"Ingrese el serial para la validación del programa")
		self.lineEdit_serial.move(20, 400)

		self.buttonAceptar = QPushButton(self)
		self.buttonAceptar.setGeometry(QRect(450, 500, 80, 31))
		self.buttonAceptar.setStyleSheet(style_QPushButton)
		self.buttonAceptar.setText("Aceptar")
		self.buttonAceptar.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.buttonAceptar.move(350, 400)

		self.buttonCancelar = QPushButton(self)
		self.buttonCancelar.setGeometry(QRect(450, 500, 80, 31))
		self.buttonCancelar.setStyleSheet(style_QPushButton)
		self.buttonCancelar.setText("Cancelar")
		self.buttonCancelar.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.buttonCancelar.move(700, 400)

		# Label description
		self.label_description_1 = QLabel(self)
		self.label_description_1.setGeometry(QRect(20, 100, 491, 20))
		self.label_description_1.setStyleSheet(style_label_text)
		self.label_description_1.setText("")
		self.label_description_1.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
		self.label_description_1.setAlignment(Qt.AlignCenter)
		self.label_description_1.move(300, 30)

		# Imagen_1
		self.label_Imagen_1 = QLabel(self.frame_carousel)
		self.label_Imagen_1.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_1.setStyleSheet(style_labelImagen_1)

		# Imagen_2
		self.label_Imagen_2 = QLabel(self.frame_carousel)
		self.label_Imagen_2.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_2.setStyleSheet(style_labelImagen_2)

		# Imagen_3
		self.label_Imagen_3 = QLabel(self.frame_carousel)
		self.label_Imagen_3.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_3.setStyleSheet(style_labelImagen_3)

		# Imagen_4
		self.label_Imagen_4 = QLabel(self.frame_carousel)
		self.label_Imagen_4.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_4.setStyleSheet(style_labelImagen_4)

		# Imagen_5
		self.label_Imagen_5 = QLabel(self.frame_carousel)
		self.label_Imagen_5.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_5.setStyleSheet(style_labelImagen_5)

		# Imagen_6
		self.label_Imagen_6 = QLabel(self.frame_carousel)
		self.label_Imagen_6.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_6.setStyleSheet(style_labelImagen_6)

		# Eventos
		self.buttonAceptar.clicked.connect(self.Encriptar)
		self.buttonCancelar.clicked.connect(self.cancelar)

	def time_image(self):
		self.timer_imagen = QTimer()
		self.timer_imagen.singleShot(500, self.Mostrar_imagenes)
		self.timer_imagen.singleShot(69000, self.Mostrar_imagenes)
		self.timer_imagen.singleShot(138000, self.Mostrar_imagenes)
		self.timer_imagen.singleShot(276000, self.Mostrar_imagenes)

	def Mostrar_imagenes(self):
		self.timer = QTimer()
		self.timer.singleShot(500, self.Mostrar_1)
		self.timer.singleShot(10000, self.Ocultar_1)

		self.timer.singleShot(11500, self.Mostrar_2)
		self.timer.singleShot(21500, self.Ocultar_2)

		self.timer.singleShot(23000, self.Mostrar_3)
		self.timer.singleShot(33000, self.Ocultar_3)

		self.timer.singleShot(34500, self.Mostrar_4)
		self.timer.singleShot(44500, self.Ocultar_4)

		self.timer.singleShot(46000, self.Mostrar_5)
		self.timer.singleShot(56000, self.Ocultar_5)

		self.timer.singleShot(57500, self.Mostrar_6)
		self.timer.singleShot(67500, self.Ocultar_6)

	def Mostrar_1(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_1, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("Vista general de datos")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_1(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_1, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_2(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_2, b"geometry")
		self.animacionMostar.finished.connect(lambda: (
			self.label_description_1.setText("Registro de usuarios de forma detallada")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_2(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_2, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_3(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_3, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText(
			"Vista general de usuarios ordenados por número de vivienda")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_3(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_3, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_4(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
		self.animacionMostar.finished.connect(lambda: (
			self.label_description_1.setText("Opciones de búsqueda especificadas")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_4(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_5(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_5, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText(
			"Visualización de fecha y hora de registro del usuario")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_5(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_5, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_6(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_6, b"geometry")
		self.animacionMostar.finished.connect(lambda: (
			self.label_description_1.setText("Registro completo y detallado del usuario")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_6(self):
		self.animacionMostar = QPropertyAnimation(self.label_Imagen_6, b"geometry")
		self.animacionMostar.finished.connect(
			lambda: (self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Encriptar(self):
		lineAceptar = str(self.lineEdit_serial.text()).upper()

		sistema = platform.system()
		ruta = ""
		if sistema == "Linux":
			ruta = ('//')
		else:
			ruta = ('C:/Windows/')

		if os.path.isfile(ruta + 'verification_vesor/Serial.txt'):
			serial = open(ruta + 'verification_vesor/Serial.txt', "r").read()

			def descifrado(serial): 
				pos = 3 
				dato_descifrado = ""

				for c in serial:
				    if c.isupper():
				        resta_pos = ord(c) - ord("A")
				        nueva_pos = (resta_pos - pos) % 26
				        nueva_unicode = nueva_pos + ord("A")
				        new_character = chr(nueva_unicode)
				        dato_descifrado = dato_descifrado + new_character
				    else:
				        dato_descifrado += c
				return dato_descifrado

			dato_desencriptado = descifrado(serial)

			if dato_desencriptado == lineAceptar:
				with open(ruta + 'verification_vesor/Serial.txt', "w") as escribirOk:
					escribirOk.write("isOk")
					escribirOk.close()

				if os.path.isfile('Users_database.db'):
					self.login_window = Login_window()
					self.login_window.show()
					self.close()

				else:
					self.startwindow = Start_window()
					self.startwindow.show()
					self.close()
			else:
				QMessageBox.information(self, "Error", "Serial no válido", QMessageBox.Yes)
		else:
			QMessageBox.information(self, "Error", "Contacte a los creadores de VESOR\npara adquirir el programa", QMessageBox.Yes)

	def cancelar(self):
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de validación?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar esta ventana?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
				
		cerrar.exec_()
		if cerrar.clickedButton() == botonSalir:
			self.close()
		else:
			pass

# Clase de ventana principal
class Interface(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("ui/Ventana_inicial_menus.ui", self)
		self.setWindowTitle("Menu principal")
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)
		self.valor_1.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_1))
		self.valor_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self.valor_1_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self.valor_2_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self._timer = QTimer()
		self._timer.singleShot(1000, self.mostrar_datos)
		self.move(300,300)
		#Buttons
		self.buttonNewUser.setIcon(QIcon(":/Icono_usuario/Imagenes-iconos/Usuario_blanco.png"))
		self.buttonNewUser.setIconSize(QSize(18,18))

		# Interacciones 
		self.operacion_1.setToolTip("Presione aquí para realizar la operación")
		self.operacion_2.setToolTip("Presione aquí para realizar la operación")

		self.Cantidad_m.setToolTip("Cantidad total de hombres registrados")
		self.Cantidad_f.setToolTip("Cantidad total de mujeres registradas")
		self.Cantidad_rep.setToolTip("Cantidad total de usuarios registrados\n"
									"en el Registro Electoral Permanente")
		self.Cantidad_estudiante.setToolTip("Cantidad total de estudiantes registrados")
		self.Cantidad_discapacidad.setToolTip("Cantidad total de discapacitados registrados")
		self.Cantidad_enfermedad.setToolTip("Cantidad total de enfermos registrados")
		self.Cantidad_pensionado.setToolTip("Cantidad total de pensionados registrados")
		self.Cantidad_embarazo.setToolTip("Cantidad total de embarazadas registradas")
		self.Cantidad_lactante.setToolTip("Cantidad total de lactantes registradas")
		self.groupBox_3.setToolTip("Cantidad total de usuarios registrados, distribuidos por edades")
		self.Button_menu_2.setToolTip("Click para actualizar la vista general de datos de usuario")

		# Shadow
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_2.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_3.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_5.setGraphicsEffect(self.shadow)

		# Menu
		self.menuArchivo = QMenu()
		self.menuArchivo.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:1px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:5px;"
		"margin-right:5px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		
		self.acercade = self.menuArchivo.addAction("Acerca de VESOR", self.Abrir_window)
		
		# Menu opciones de usuario
		self.menu_usuario = QMenu()
		self.menu_usuario.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_user = self.menu_usuario.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar usuario", self.Nuevo_user)
		self.Editar_usuario = self.menu_usuario.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Eliminar usuario", self.Editar_usuario)

		# Menu opciones de vocero =====================================================================================================  

		self.menu_vocero = QMenu()
		self.menu_vocero.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar vocero", self.Nv_vocero)

		self.Editar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Elimina vocero")

		# Eventos
		self.operacion_1.clicked.connect(self.realizar_operacion_1)
		self.operacion_2.clicked.connect(self.realizar_operacion_2)
		self.Button_menu.setMenu(self.menuArchivo)
		self.buttonNewUser.setMenu(self.menu_usuario)
		self.buttonNewUser.setToolTip("Click para ver opciones de usuario")
		self.buttonStatus.setToolTip("Click para ver estatus de los usuarios")
		self.buttonStatus.clicked.connect(self.Abrir_ventana)
		self.Button_menu_2.clicked.connect(self.mostrar_datos)
		self.Button_menu_2.setToolTip("Click para actualizar la vista general de datos de usuario")

	def mostrar_datos(self):

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				self.cursor_masculino = self.con.cursor()
				self.cursor_femenino = self.con.cursor()
				self.cursor_edad_0 = self.con.cursor()
				self.cursor_edad_13 = self.con.cursor()
				self.cursor_edad_18 = self.con.cursor()
				self.cursor_edad_30 = self.con.cursor()
				self.cursor_edad_55 = self.con.cursor()
				self.cursor_estud = self.con.cursor()
				self.cursor_rep = self.con.cursor()
				self.cursor_pensionado = self.con.cursor()
				self.cursor_discapacidad = self.con.cursor()
				self.cursor_enfermedad = self.con.cursor()
				self.cursor_enbarazo = self.con.cursor()
				self.cursor_lactante = self.con.cursor()

				# Cursor masculino
				self.cursor_masculino.execute("SELECT COUNT(GENERO) FROM USUARIO_DT_GNR WHERE GENERO = 'Masculino'")
				dato_masculino = self.cursor_masculino.fetchall()
				for m in dato_masculino:
					dato_m = m[0]
				mostrar_m = str(dato_m)
				self.Cantidad_m.setText(mostrar_m)

				# Cursor femenino
				self.cursor_femenino.execute("SELECT COUNT(GENERO) FROM USUARIO_DT_GNR WHERE GENERO = 'Femenino'")
				dato_femenino = self.cursor_femenino.fetchall()
				for f in dato_femenino:
					dato_f = f[0]
				mostrar_f = str(dato_f)
				self.Cantidad_f.setText(mostrar_f)

				# Cursor edad  >= 0 años
				self.cursor_edad_0.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 0 AND EDAD <= 12 ")
				dato_edad_0 = self.cursor_edad_0.fetchall()
				for e_0 in dato_edad_0:
					dato_e_0 = e_0[0]
				dato_0_12 = str(dato_e_0)
				self.Cantidad_0_12.setText(dato_0_12)

				# Cursor edad  >= 13 años
				self.cursor_edad_13.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 13 AND EDAD <= 18")
				dato_edad_13 = self.cursor_edad_13.fetchall()
				for e_13 in dato_edad_13:
					dato_e_13 = e_13[0]
				dato_12_18 =str(dato_e_13)
				self.Cantidad_12_18.setText(dato_12_18)

				# Cursor edad  >= 18 años
				self.cursor_edad_18.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 19 AND EDAD <= 30")
				dato_edad_18 = self.cursor_edad_18.fetchall()
				for e_18 in dato_edad_18:
					dato_e_18 = e_18[0]
				dato_19_30 = str(dato_e_18)
				self.Cantidad_19_30.setText(dato_19_30)

				# Cursor edad  >= 30 años
				self.cursor_edad_30.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 31 AND EDAD <= 54")
				dato_edad_30 = self.cursor_edad_30.fetchall()
				for e_30 in dato_edad_30:
					dato_e_30 = e_30[0]
				dato_31_54 = str(dato_e_30)
				self.Cantidad_31_54.setText(dato_31_54)

				# Cursor edad  >= 55 años
				self.cursor_edad_55.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 55")
				dato_edad_55 = self.cursor_edad_55.fetchall()
				for e_55 in dato_edad_55:
					dato_e_55 = e_55[0]
				dato_mayor_55 = str(dato_e_55)
				self.Cantidad_55.setText(dato_mayor_55)

				# Cursor estudiante
				self.cursor_estud.execute("SELECT COUNT(PROFESION_OFICIO) FROM USUARIO_DT_GNR WHERE PROFESION_OFICIO = 'Estudiante'")
				dato_estudiante = self.cursor_estud.fetchall()
				for estudiante in dato_estudiante:
					dato_de_estudiante = estudiante[0]
				dato_mostrar_estudiante = str(dato_de_estudiante)
				self.Cantidad_estudiante.setText(dato_mostrar_estudiante)

				# Inscrito en el REP
				self.cursor_rep.execute("SELECT COUNT(INSCRITO_REP) FROM USUARIO_DT_GNR WHERE INSCRITO_REP = 'Si'")
				dato_rep= self.cursor_rep.fetchall()
				for rep in dato_rep:
					dato_de_rep = rep[0]
				dato_mostrar_rep = str(dato_de_rep)
				self.Cantidad_rep.setText(dato_mostrar_rep)

				# Si esta pensionado 
				self.cursor_pensionado.execute("SELECT COUNT(PENSIONADO) FROM USUARIO_DT_GNR WHERE PENSIONADO = 'Pensionado'")
				dato_pensionado= self.cursor_pensionado.fetchall()
				for pensionado in dato_pensionado:
					dato_de_pensionado = pensionado[0]
				dato_mostrar_pensionado = str(dato_de_pensionado)
				self.Cantidad_pensionado.setText(dato_mostrar_pensionado)

				# Si posee discapacidad
				self.cursor_discapacidad.execute("SELECT COUNT(DESCRIBA_DISCAPACIDAD) FROM USUARIO_DT_GNR WHERE DESCRIBA_DISCAPACIDAD != '' ")
				dato_discapacidad = self.cursor_discapacidad.fetchall()

				for discapacidad in dato_discapacidad:
					dato_de_discapacidad = discapacidad[0]
				if dato_de_discapacidad > 0:
					dato_mostrar_discapacidad = str(dato_de_discapacidad)
					self.Cantidad_discapacidad.setText(dato_mostrar_discapacidad)
				else:
					self.Cantidad_discapacidad.setText("0")
					"0"
					
				# Si posee enfermedad
				self.cursor_enfermedad.execute("SELECT COUNT(DESCRIBA_ENFERMEDAD) FROM USUARIO_DT_GNR WHERE DESCRIBA_ENFERMEDAD != '' ")
				dato_enfermedad = self.cursor_enfermedad.fetchall()

				for enfermedad in dato_enfermedad:
					dato_de_enfermedad = enfermedad[0]
				if dato_de_enfermedad > 0:
					datos_mostrar_enfermedad = str(dato_de_enfermedad)
					self.Cantidad_enfermedad.setText(datos_mostrar_enfermedad)
				else:
					self.Cantidad_enfermedad.setText("0")
					"0"

				# Si esta en estado de embarazo
				self.cursor_enbarazo.execute("SELECT COUNT(EMBARAZADA) FROM USUARIO_DT_GNR WHERE EMBARAZADA = 'Si' ")
				dato_enbarazo = self.cursor_enbarazo.fetchall()

				for enbarazo in dato_enbarazo:
					dato_de_enbarazo = enbarazo[0]
				datos_mostrar_embarazo = str(dato_de_enbarazo)
				self.Cantidad_embarazo.setText(datos_mostrar_embarazo)

				# Si esta en estado de lactante
				self.cursor_lactante.execute("SELECT COUNT(LACTANTE) FROM USUARIO_DT_GNR WHERE LACTANTE = 'Si' ")
				dato_lactante = self.cursor_lactante.fetchall()

				for lactante in dato_lactante:
					dato_de_lactante = lactante[0]
				datos_mostrar_lactante = str(dato_de_lactante)
				self.Cantidad_lactante.setText(datos_mostrar_lactante)
				
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
										 QMessageBox.Ok)                
		else:   
			QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
										"información.   ", QMessageBox.Ok)

	def realizar_operacion_1(self):     
		valor_1 = self.valor_1.text()
		valor_2 = self.valor_2.text()

		if not valor_1:
			self.valor_1.setFocus()
		elif not valor_2:
			self.valor_2.setFocus()
		else:
			operacion = (int(valor_1) * int(valor_2))
			division = (int(operacion) // 100)
			mostrar_resultado_1 = str(division)

			self.resultado_1.setText(mostrar_resultado_1)

	def realizar_operacion_2(self):     
		valor_1_2 = self.valor_1_2.text()
		valor_2_2 = self.valor_2_2.text()

		if not valor_1_2:
			self.valor_1_2.setFocus()
		elif not valor_2_2:
			self.valor_2_2.setFocus()
		else:
			operacion = (100 * int(valor_1_2))
			division = (int(operacion) // int(valor_2_2))
			mostrar_resultado_2= str(division)

			self.resultado_2.setText(mostrar_resultado_2 + "%")

	def Abrir_ventana(self):
		Window_status_user(self).exec_()

	def Editar_usuario(self):
		self.interface = Window_edit_elim_user()
		self.interface.show()
	
	def Nuevo_user(self):
		Window_nv_users(self).exec_()

	def Abrir_window(self):
		Acerca_de(self).exec_()

	def Nv_vocero(self):
		Window_vocero(self).exec_()

	def closeEvent(self, event):
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de VESOR?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar VESOR?   ")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
		cerrar.exec_()
			
		if cerrar.clickedButton() == botonSalir:
			event.accept()
		else:
			event.ignore()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()

# Clase Ventana editar y eliminar usuario
class Window_edit_elim_user(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Editar usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(783, 460)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()

	def initUi(self):
		# Style frame principal
		Style_frame_principal = ("QFrame#frame{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		# Style QTable con el contenido

		Style_qtable_contenido = ("QTableWidget::item{\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget::item:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget{\n"
									"background-color:#ced4da;\n"
									"border:5px solid #000000;\n"
									"border-radius:10px;\n"
									"color:#000000;\n"
									"}\n"
									"QHeaderView::section{\n"
									"background-color:#12191D;\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000;\n"
									"}\n"
									"QHeaderView::section:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000\n"                                   
									"}\n"
									"QHeaderView::section:checked{\n"
									"background-color: rgb(0, 170, 255);\n"
									"}")
		# Style frame menu
		Style_frame_menu = ("QFrame{\n"
							
							"background-color:#12191D;\n"
							"border-radius: 45px\n"
							"}")

		# Style buttons
		Style_buttons = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"color:rgb(255, 255, 255);\n"
						"font-size: 12px\n"
						"}\n"

						"QPushButton:hover{\n"
						"background-color:rgb(0, 170, 255);\n"
						"color:rgb(255, 255, 255);\n"
						"font-size: 12px;\n"
						"}")
		# Style actualizar 
		Style_actulizar_button =    ("QPushButton{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
									"border-radIus: 3px\n"
									"}\n"
									"QPushButton:hover{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 204, 204, 129));\n"
									"border-radius:10px;\n"
									"}")
		# Style label titulo
		Style_label_menu = ("QLabel{\n"
							"color:rgb(255, 255, 255);\n"
							"font: 10pt 'Comic Sans MS';\n"
							"border-radius: 6px;\n"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"

							"}")
		# Style label busqueda
		Style_label_busqueda = ("QLabel{\n"
								"color:rgb(255, 255, 255);\n"
								"font: 8pt 'Comic Sans MS';\n"
								"background-color:#1C262D\n"
								"}")
		# Style busqueda
		Style_line_edit_busqueda = ("QLineEdit{\n"
									"border-radius: 6px;\n"
									"}\n"
									"QLineEdit:hover{\n"
									"border:1px solid rgb(0, 170, 255);\n"
									"}")
		# Style menu button buscar
		Style_button_menu =("QMenu{background-color:#12191D;\n"
		"color: #ffffff;}\n"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}") 

		# Frames
		self.menu_buscar = QMenu()
		self.menu_buscar.setStyleSheet(Style_button_menu)
		self.buscar_estudiante = self.menu_buscar.addAction("Buscar estudiante", self.Mostrar_estudiantes)
		self.buscar_discapacidad = self.menu_buscar.addAction("Buscar discapacitados", self.Mostrar_discapacitados)
		self.buscar_enfermedad = self.menu_buscar.addAction("Buscar enfermos", self.Mostrar_enfermos)
		self.buscar_pensionados = self.menu_buscar.addAction("Buscar pensionados", self.Mostrar_pensionados)
		self.buscar_embarazadas = self.menu_buscar.addAction("Buscar embarazadas", self.Mostrar_embarazadas)
		self.buscar_lactantes = self.menu_buscar.addAction("Buscar lactantes", self.Mostrar_lactantes)
		self.buscar_rep = self.menu_buscar.addAction("Buscar inscritos en el REP", self.Mostrar_inscritosRep)

		self.buscar_parentesco = self.menu_buscar.addMenu("Buscar por parentesco")
		self.buscar_parentesco.addAction("Jefe/a de familia", self.Mostrar_jefe_de_familia)
		
		self.buscar_genero = self.menu_buscar.addMenu("Buscar por género")
		self.buscar_genero.addAction("Masculino", self.Mostrar_masculino)
		self.buscar_genero.addAction("Femenino", self.Mostrar_femenino)
		
		self.buscar_edad = self.menu_buscar.addAction("Buscar por edad",self.Mostrar_edad)

		# Frame principal contenido
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(180,20,581,411))
		self.frame_principal_contenido.setObjectName("frame")
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)

		# Frame menu
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(30,20,121,411))
		self.frame_menu.setStyleSheet(Style_frame_menu)

		# Labels		
		# label menu
		self.Label = QLabel(self.frame_menu)
		self.Label.setGeometry(QRect(30,30,121,51))
		self.Label.setText("ELIMINAR \nY EDITAR \nUSUARIO")
		self.Label.setStyleSheet(Style_label_menu)

		self.Label_4 = QLabel(self.frame_menu)
		self.Label_4.setGeometry(QRect(0,300,121,21))
		self.Label_4.setText("BÚSQUEDA")
		self.Label_4.setAlignment(Qt.AlignCenter)
		self.Label_4.setStyleSheet(Style_label_busqueda)    
	
		# LineEdit busqueda nombre ==========================================================================================
		self.line_edit_busqueda = QLineEdit(self.frame_menu)
		self.line_edit_busqueda.setObjectName("Enter")
		self.line_edit_busqueda.setGeometry(QRect(5,330,111,21))
		self.line_edit_busqueda.setToolTip("Ingresa el primer nombre del usuario\npara la busqueda")
		self.line_edit_busqueda.setPlaceholderText("Ingresa nombre")
		self.line_edit_busqueda.setStyleSheet(Style_line_edit_busqueda)

		# Buttons ==========================================================================================
		#  Actualizar            
		self.actualizar = QPushButton(self.frame_menu)
		self.actualizar.setText("")
		self.actualizar.setGeometry(QRect(50, 120, 23, 21))
		self.actualizar.setStyleSheet(Style_actulizar_button)
		self.actualizar.setIcon(QIcon(":/Icono_recargar/Imagenes-iconos/Recargar.png"))
		self.actualizar.setIconSize(QSize(26,26))
		self.actualizar.setToolTip("Click para actualizar\nla lista de usuarios")

		# Button Buscar
		self.buscar = QPushButton(self.frame_menu)
		self.buscar.setObjectName("Buscar")
		self.buscar.setText("Buscar")
		self.buscar.setGeometry(QRect(-3,355,130,21))
		self.buscar.setStyleSheet(Style_buttons)
		self.buscar.setToolTip("Click para buscar usuario")

		# Buttons aceptar
		self.aceptar_edit_user = QPushButton(self.frame_menu)
		self.aceptar_edit_user.setText("Aceptar")
		self.aceptar_edit_user.setGeometry(QRect(0, 150, 121, 31))
		self.aceptar_edit_user.setStyleSheet(Style_buttons)
		self.aceptar_edit_user.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.aceptar_edit_user.setIconSize(QSize(15,15))

		# Button eliminar
		self.eliminar = QPushButton(self.frame_menu)
		self.eliminar.setText("Eliminar")
		self.eliminar.setGeometry(QRect(0, 180, 121, 31))
		self.eliminar.setStyleSheet(Style_buttons)
		self.eliminar.setIcon(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"))
		self.eliminar.setIconSize(QSize(17,17))
		self.eliminar.setToolTip("Click para eliminar un usuario seleccionado")
		
		# Buttons opciones buscar 
		self.opciones_de_busqueda = QPushButton(self.frame_menu)
		self.opciones_de_busqueda.setText("Opciones")
		self.opciones_de_busqueda.setGeometry(QRect(-12, 210, 151, 31))
		self.opciones_de_busqueda.setStyleSheet(Style_buttons)
		self.opciones_de_busqueda.setToolTip("Click para mostrar opciones de búsqueda")
		self.opciones_de_busqueda.setIcon(QIcon(":/Icono_lupa/Imagenes-iconos/Lupa_blanca.png"))
		self.opciones_de_busqueda.setIconSize(QSize(16,16))

		# Buttons cancelar
		self.cancelar_edit_user = QPushButton(self.frame_menu)
		self.cancelar_edit_user.setText("Cancelar")
		self.cancelar_edit_user.setGeometry(QRect(0, 240, 121, 31))
		self.cancelar_edit_user.setStyleSheet(Style_buttons)
		self.cancelar_edit_user.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.cancelar_edit_user.setIconSize(QSize(15,15))

		self.exportar = QPushButton(self.frame_menu)
		self.exportar.setText("Exportar")
		self.exportar.setGeometry(0,270,121,31)
		self.exportar.setToolTip("Exportar a Excell")
		self.exportar.setStyleSheet(Style_buttons)

		# QTableWidget ==========================================================================================           
		nombreColumnas = ("ID", "Primer nombre", "Primer apellido", "Cedula",
		 "Edad", "N°Vivienda")

		self.QTableWidget_contenido = QTableWidget(self.frame_principal_contenido)
		self.QTableWidget_contenido.setToolTip("Click para ver usuario")
		self.QTableWidget_contenido.setGeometry(QRect(15,11,551,391))
		self.QTableWidget_contenido.setStyleSheet(Style_qtable_contenido)
		self.QTableWidget_contenido.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.QTableWidget_contenido.setDragDropOverwriteMode(False)
		self.QTableWidget_contenido.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.QTableWidget_contenido.setSelectionMode(QAbstractItemView.SingleSelection)
		self.QTableWidget_contenido.setTextElideMode(Qt.ElideRight)
		self.QTableWidget_contenido.setWordWrap(False)
		self.QTableWidget_contenido.setSortingEnabled(False)
		self.QTableWidget_contenido.setColumnCount(6)
		self.QTableWidget_contenido.setRowCount(0)
		self.QTableWidget_contenido.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.QTableWidget_contenido.horizontalHeader().setHighlightSections(False)
		self.QTableWidget_contenido.horizontalHeader().setStretchLastSection(True)
		self.QTableWidget_contenido.verticalHeader().setVisible(False)
		self.QTableWidget_contenido.setAlternatingRowColors(False)
		self.QTableWidget_contenido.verticalHeader().setDefaultSectionSize(20)
		self.QTableWidget_contenido.setHorizontalHeaderLabels(nombreColumnas)

		for indice, ancho in enumerate((5, 150, 150, 150, 80, 150), start=0):
			self.QTableWidget_contenido.setColumnWidth(indice, ancho)


		# EVENTOS ==========================================================================================            
		
		self.exportar.clicked.connect(self.exportar_Excell)
		self.actualizar.clicked.connect(self.mostrar_datos)
		self.cancelar_edit_user.clicked.connect(self.cerrar_edit_user)
		self.eliminar.clicked.connect(self.eliminar_datos)
		self.aceptar_edit_user.clicked.connect(self.Aceptar_edit_user)
		self.line_edit_busqueda.returnPressed.connect(self.buscar_datos)
		self.buscar.clicked.connect(self.buscar_datos)
		self.opciones_de_busqueda.setMenu(self.menu_buscar)
		self.QTableWidget_contenido.itemDoubleClicked.connect(self.Item_click)

	def exportar_Excell(self):
		archivo, _ = QFileDialog.getSaveFileName(self, 'Guardar Archivo', QDir.homePath(), "Excell Files (*.xls)")
		if archivo:

			wb = Workbook()
			hoja = wb.add_sheet('sheet 1')
			# En cuanto a datos generales
			# hoja.write(0,1,'Primer Nombre')
			# hoja.write(0,2,'Segundo Nombre')
			# hoja.write(0,3,'Primer Apellido')
			# hoja.write(0,4,'Segundo Apellido')
			# hoja.write(0,5,'Cédula')
			# hoja.write(0,6,'Género')
			# hoja.write(0,7,'Teléfono Principal')
			# hoja.write(0,8,'Teléfono Secundario')
			# hoja.write(0,9,'Fecha Nacimiento')
			# hoja.write(0,10,'Edad')
			# hoja.write(0,11,'ProfesiónOficio')
			# hoja.write(0,12,'Nivel de Instrucción')
			# hoja.write(0,13,'Parentesco')
			# hoja.write(0,14,'Edo. Civíl')
			# hoja.write(0,15,'Incrito REP')
			# hoja.write(0,16,'Correo')
			# hoja.write(0,17,'Pensión')
			# hoja.write(0,18,'Discapacidad')
			# hoja.write(0,19,'Discapacidad Motriz')
			# hoja.write(0,20,'Discapacidad Auditiva')
			# hoja.write(0,21,'Discapacidad Visual')
			# hoja.write(0,22,'Discapacidad Intelectual')
			# hoja.write(0,23,'Discapacidad Visceral')
			# hoja.write(0,24,'Discapacidad Otras')
			# hoja.write(0,25,'Silla de Ruedas')
			# hoja.write(0,26,'Muletas')
			# hoja.write(0,27,'Protesis')
			# hoja.write(0,28,'Insumo/Otros')
			# hoja.write(0,29,'Describa discapacidad')
			# hoja.write(0,30,'Medicamento')
			# hoja.write(0,31,'Describa Medicamento')
			# hoja.write(0,32,'Cancer')
			# hoja.write(0,33,'Diabetes')
			# hoja.write(0,34,'Hipertensión')
			# hoja.write(0,35,'Asma')
			# hoja.write(0,36,'Cardio')
			# hoja.write(0,37,'Gastritis')
			# hoja.write(0,38,'Bronquitis')
			# hoja.write(0,39,'Calculos')
			# hoja.write(0,40,'Sinusitis')
			# hoja.write(0,41,'Enfermedad Otras')
			# hoja.write(0,42,'Describa Enfermedad')
			# hoja.write(0,43,'Toma Medicamento')
			# hoja.write(0,44,'Describa Medicamento')
			# hoja.write(0,45,'Embarazada')
			# hoja.write(0,46,'Lactante')
			# hoja.write(0,47,'Nivel de Estudio')
			# hoja.write(0,48,'Carrera Cursando')
			# hoja.write(0,49,'Lugar de estudio')
			# hoja.write(0,50,'N° Vivienda')
			# # En el ambito de vivienda
			# hoja.write(0,51,'Metros Cuadrados')
			# hoja.write(0,52,'Descripción')
			# hoja.write(0,53,'Necesita Reparación')
			# hoja.write(0,54,'R. Techo')
			# hoja.write(0,55,'R. Paredes')
			# hoja.write(0,56,'R. Pintura')
			# hoja.write(0,57,'R. Pisos')
			# hoja.write(0,58,'R. Tendido Eléctrico')
			# hoja.write(0,59,'R. Agua')
			# hoja.write(0,60,'R. Agua Servidas')
			# hoja.write(0,61,'R. Ventanas')
			# hoja.write(0,62,'R. Puertas')
			# hoja.write(0,63,'R. Otras')
			# hoja.write(0,64,'Agua Potable')
			# hoja.write(0,65,'Aguas Servidas')
			# hoja.write(0,67,'Gas Directo')
			# hoja.write(0,68,'Tipo Cilindro')
			# hoja.write(0,69,'N° Bombona')
			# hoja.write(0,70,'Internet')
			# hoja.write(0,71,'Electricidad')
			# hoja.write(0,72,'Telef. Fijo')
			# hoja.write(0,73,'Descripción Reparación')
			# hoja.write(0,74,'Línea blanca Necesaria')
			# # En cuanto a Ubicación
			# hoja.write(0,75,'Estado')
			# hoja.write(0,76,'Municipio')
			# hoja.write(0,77,'Parroquia')
			# hoja.write(0,78,'Dirección')
			# # En cuanto a Protección Social
			# hoja.write(0,79,'Hogares Patria')
			# hoja.write(0,80,'Amor Mayor')
			# hoja.write(0,81,'José Gregorio')
			# hoja.write(0,82,'Parto Humanizado')
			# hoja.write(0,83,'Chamba Juvenil')
			# hoja.write(0,84,'Somos Venezuela')
			# hoja.write(0,85,'Frente Miranda')
			# hoja.write(0,86,'JPSUV')

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				# try: 
					self.conex = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
					self.conex2 = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")
					self.conex3 = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOS_VV.db")
					self.conex4 = sqlite3.connect("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db")

					self.cursor = self.conex.cursor()
					self.cursor2 = self.conex2.cursor()
					self.cursor3 = self.conex3.cursor()
					self.cursor4 = self.conex4.cursor()

					self.cursor.execute("SELECT * FROM USUARIO_DT_GNR ORDER BY ID")
					self.cursor2.execute("SELECT * FROM USUARIO_UBCGEOG ORDER BY ID")
					self.cursor3.execute("SELECT METROS_CUADRADOS, DESCRIPCION, NECESITA_REPARACION,REPARACION_TECHOS , REPARACION_PARED , REPARACION_PINTURA ,REPARACION_PISOS ,REPARACION_ELECTRICO , REPARACION_AGUA , REPARACION_AGUA_SERVIDAS , REPARACION_VENTANAS ,REPARACION_PUERTARS , REPARACION_OTRAS ,AGUA_POTABLE, AGUA_SERVIDAS, GAS_DIRECTO, GAS_BOMBONA, TIPO_DE_CILINDRO, CANTIDAD_DE_BOMBONAS, INTERNET, ElECTRICIDAD, TELEFONO_FIJO, DESCRIPCION_REPARACION, NECESITA_LINEBLANCA FROM USUARIO_DT_VV ORDER BY ID")
					self.cursor4.execute("SELECT * FROM USUARIO_PROT_SOCIAL ORDER BY ID")

					datos_Devueltos = self.cursor.fetchall()
					datos_Devueltos2 = self.cursor2.fetchall()
					datos_Devueltos3 = self.cursor3.fetchall()
					datos_Devueltos4 = self.cursor4.fetchall()

					datos_total = datos_Devueltos + datos_Devueltos2 + datos_Devueltos3 + datos_Devueltos4
					# datos_total = str(datos_total)

					if datos_total:
						col = 1
						fila = 1

						for datos in datos_total:
							hoja.write(col,fila,datos[1])
							hoja.write(col,fila,datos[2])
							hoja.write(col,fila,datos[3])
							hoja.write(col,fila,datos[4])
							fila +=1

			archivo = wb.save(archivo+'.xls')


	def Aceptar_edit_user(self):
		aceptar_user = QMessageBox(self)
		aceptar_user.setWindowTitle("Aceptar")
		aceptar_user.setIcon(QMessageBox.Question)
		aceptar_user.setText("¿Estás seguro de guardar los datos existentes?")
		botonaceptar_user = aceptar_user.addButton("Si", QMessageBox.YesRole)
		botonCancelar_user = aceptar_user.addButton("No", QMessageBox.NoRole)

		aceptar_user.exec_()

		if aceptar_user.clickedButton() == botonaceptar_user:
			self.close()
		else:
			pass

	def cerrar_edit_user(self):
		cerrar_edit = QMessageBox(self)
		cerrar_edit.setWindowTitle("Cancelar")
		cerrar_edit.setIcon(QMessageBox.Question)
		cerrar_edit.setText("¿Estás seguro que desea cancelar?")
		botonSalir_edit = cerrar_edit.addButton("Si", QMessageBox.YesRole)
		botonCancelar_edit = cerrar_edit.addButton("No", QMessageBox.NoRole)

		cerrar_edit.exec_()

		if cerrar_edit.clickedButton() == botonSalir_edit:
			self.close()
		else:
			pass        

	def mostrarOcultar(self, accion):
		columna = accion.data()
		if accion.isChecked():
			self.QTableWidget_contenido.setColumnHidden(columna, False)
		else:
			self.QTableWidget_contenido.setColumnHidden(columna,True)

	def mostrar_datos(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				self.cursor = self.con.cursor()

				self.cursor.execute("SELECT ID, PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA, EDAD, N_VIVIENDA FROM USUARIO_DT_GNR ORDER BY N_VIVIENDA")

				datos_Devueltos = self.cursor.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)

				if datos_Devueltos:
					row = 0

					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[2]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[4]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[5]))
						row +=1

				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)

			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontro la base de datos.   ",
								 QMessageBox.Ok)

	def Item_click(self,celda):
		celda = self.QTableWidget_contenido.selectedItems()

		if celda:
			indice = celda[0].row()
			dato = [self.QTableWidget_contenido.item(indice,i).text()for i in range(4)]

			dato_buscar = dato[3]

			if dato_buscar:
				sql = "SELECT * FROM USUARIO_DT_GNR WHERE CEDULA LIKE ?", (dato_buscar,)
				print("Si")
			else:
				print("NO")

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				conexion = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor = conexion.cursor()
				try:
					cursor.execute(sql[0],sql[1])
					datosdevueltos = cursor.fetchall()
					for dato in datosdevueltos:
						indice = dato[0]

					Window_visualizar_users(dato,self).exec_()
					conexion.close()
				except Exception as e:
					print("A1:",e)
		else:
			print("Error")

	def eliminar_datos(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

			msg = QMessageBox()
			msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
			msg.setText("¿Está seguro de querer eliminar este usuario?")
			msg.setIcon(QMessageBox.Question)
			msg.setWindowTitle("Eliminar Usuario")
			msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

			button_si = msg.button(QMessageBox.Yes)
			button_si.setText("Si")
			button_si.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
			button_si.setIconSize(QSize(13,13))
			button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
			"QPushButton{background:#343a40;\n"
			"}")

			button_no = msg.button(QMessageBox.No)
			button_no.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
			button_no.setIconSize(QSize(13,13))
			button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
			"QPushButton{background:#343a40;}")

			msg.setStyleSheet("\n"
				"color:#ffffff;\n"
				"font-size:12px;\n"
				"background-color:#12191D;")

			if (msg.exec_() == QMessageBox.Yes):
				try:
					self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
					self.con2 = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")
					self.con3 = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOS_VV.db")
					self.con4 = sqlite3.connect("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db")

					self.cursor = self.con.cursor()
					self.cursor2 = self.con2.cursor()
					self.cursor3 = self.con3.cursor()
					self.cursor4 = self.con4.cursor()


					self.QTableWidget_contenido.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
					ID = self.QTableWidget_contenido.selectedIndexes()[0].data()
					print("has clickeado en {ID}")
					
					# Primera Instancia
					query = 'DELETE  FROM USUARIO_DT_GNR WHERE ID =?'
					self.cursor.execute(query, (ID,))
					self.con.commit()

					# Segunda Instancia
					query_2 = 'DELETE FROM USUARIO_UBCGEOG WHERE ID =?'
					self.cursor2.execute(query_2, (ID,))
					self.con2.commit()

					# Tercera Instancia
					query_3 = 'DELETE FROM USUARIO_DT_VV WHERE ID =?'
					self.cursor3.execute(query_3, (ID,))
					self.con3.commit()

					# Cuarta Instancia
					query_4 = 'DELETE FROM USUARIO_PROT_SOCIAL WHERE ID =?'
					self.cursor4.execute(query_4, (ID,))
					self.con4.commit()

					# Seleccionar fila
					self.Seleccion = self.QTableWidget_contenido.selectedItems()
					# Borrar seleccionado
					self.QTableWidget_contenido.removeRow(self.QTableWidget_contenido.currentRow())

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Error", "No existen usuarios para eliminar",
											 QMessageBox.Ok)
			else:
				pass    
		else:
			QMessageBox.critical(self, "Eliminar", "No se encontró la base de datos.   ",
											QMessageBox.Ok)

	def buscar_datos(self):
		try:
			widget = self.sender().objectName()
			if widget in ("Enter", "Buscar"):
				cliente = " ".join(self.line_edit_busqueda.text().split()).lower()

				if len(cliente)== 0:
					QMessageBox.critical(self, "Error", "No se ha escrito nada",
												 QMessageBox.Ok)
				if cliente:
					sql = "SELECT ID, PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA, EDAD, N_VIVIENDA FROM USUARIO_DT_GNR WHERE PRIMER_NOMBRE LIKE ?", ("%"+cliente+"%",)
				else:
					self.line_edit_busqueda.setFocus()
					return
			else:
				self.line_edit_busqueda.clear()
				sql = "SELECT * FROM USUARIO_DT_GNR "

			if QFile.exists('Base de datos/DB_VESOR_USER_DATOSGENERALES.db'):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db')
				cursor = conexion.cursor()
				try:
					if widget in ("Enter", "Buscar"):
						cursor.execute(sql[0], sql[1])	
					else:
						cursor.execute(sql)
						
					datosDevueltos = cursor.fetchall()
					conexion.close()

					self.QTableWidget_contenido.clearContents()
					self.QTableWidget_contenido.setRowCount(0)

					if datosDevueltos:
						fila = 0
						for datos in datosDevueltos:
							self.QTableWidget_contenido.setRowCount(fila + 1)
				
							idDato = QTableWidgetItem(str(datos[0]))
							idDato.setTextAlignment(Qt.AlignCenter)
							
							self.QTableWidget_contenido.setItem(fila, 0, idDato)
							self.QTableWidget_contenido.setItem(fila, 1, QTableWidgetItem(datos[1]))
							self.QTableWidget_contenido.setItem(fila, 2, QTableWidgetItem(datos[2]))
							self.QTableWidget_contenido.setItem(fila, 3, QTableWidgetItem(datos[3]))
							self.QTableWidget_contenido.setItem(fila, 4, QTableWidgetItem(datos[4]))
							self.QTableWidget_contenido.setItem(fila, 5, QTableWidgetItem(datos[5]))

							fila += 1
					else:   
						QMessageBox.information(self, "Buscar usuario", "No se encontró "
												"información.   ", QMessageBox.Ok)
				except Exception as e:
					print(e)
					conexion.close()
					QMessageBox.critical(self, "Buscar usuarios", "Error desconocido.   ",
										 QMessageBox.Ok)
			else:
				QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
									 QMessageBox.Ok)

			self.line_edit_busqueda.setFocus()
		except AttributeError:
			pass

	def Mostrar_estudiantes(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_estudiante = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_estudiante = cur_estudiante.cursor()

				cursor_estudiante.execute("SELECT * FROM USUARIO_DT_GNR WHERE PROFESION_OFICIO = 'Estudiante' ORDER BY EDAD ")

				datos_Devueltos = cursor_estudiante.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)

				if datos_Devueltos:
					row = 0
					print("Viendo: ",datos_Devueltos)
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_discapacitados(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try:
				cur_discapacidad = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_discapacidad = cur_discapacidad.cursor()

				cursor_discapacidad.execute("SELECT * FROM USUARIO_DT_GNR WHERE DESCRIBA_DISCAPACIDAD != '' ORDER BY EDAD")
				
				datos_Devueltos = cursor_discapacidad.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.")

	def Mostrar_enfermos(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_enfermos = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_enfermos = cur_enfermos.cursor()

				cursor_enfermos.execute("SELECT * FROM USUARIO_DT_GNR WHERE DESCRIBA_ENFERMEDAD != ''")

				datos_Devueltos = cursor_enfermos.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
							
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_pensionados(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_pensionado = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_pensionado = cur_pensionado.cursor()
				cursor_pensionado.execute("SELECT * FROM USUARIO_DT_GNR WHERE PENSIONADO = 'Pensionado' ")
				datos_Devueltos = cursor_pensionado.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_embarazadas(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_embarazada = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_embarazada = cur_embarazada.cursor()

				cursor_embarazada.execute("SELECT * FROM USUARIO_DT_GNR WHERE EMBARAZADA = 'Si' ")

				datos_Devueltos = cursor_embarazada.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_lactantes(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_lactantes = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_lactantes = cur_lactantes.cursor()
				cursor_lactantes.execute("SELECT * FROM USUARIO_DT_GNR WHERE LACTANTE = 'Si' ")
				
				datos_Devueltos = cursor_lactantes.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_inscritosRep(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_inscritos = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_inscritos = cur_inscritos.cursor()
				cursor_inscritos.execute("SELECT * FROM USUARIO_DT_GNR WHERE INSCRITO_REP = 'Si' ")

				datos_Devueltos = cursor_inscritos.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_jefe_de_familia(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_jf = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_jf = cur_jf.cursor()

				cursor_jf.execute("SELECT * FROM USUARIO_DT_GNR WHERE PARENTESCO = 'Jefe/a de familia' ORDER BY EDAD ")
				
				datos_Devueltos = cursor_jf.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_femenino(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_femenino = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_femenino = cur_femenino.cursor()
				cursor_femenino.execute("SELECT * FROM USUARIO_DT_GNR WHERE GENERO = 'Femenino' ORDER BY EDAD")
				
				datos_Devueltos = cursor_femenino.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_masculino(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_masculino = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_masculino = cur_masculino.cursor()
				cursor_masculino.execute("SELECT * FROM USUARIO_DT_GNR WHERE GENERO = 'Masculino' ORDER BY EDAD ")
				
				datos_Devueltos = cursor_masculino.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

	def Mostrar_edad(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				cur_estudiante = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor_estudiante = cur_estudiante.cursor()

				cursor_estudiante.execute("SELECT * FROM USUARIO_DT_GNR WHERE EDAD != '' ORDER BY EDAD ")
				
				datos_Devueltos = cursor_estudiante.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)
				if datos_Devueltos:
					row = 0
					print("EDAD: ",datos_Devueltos)
					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[3]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[5]))
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[10]))
						self.QTableWidget_contenido.setItem(row, 5, QTableWidgetItem(datos[53]))
						row +=1
				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontró la base de datos.   ",
								 QMessageBox.Ok)

# Clase  Visualizar usuario
class Window_visualizar_users(QDialog):
	def __init__(self,dato, parent = None):
		super(Window_visualizar_users, self).__init__()

		self.parent = parent
		self.datos = dato

		self.setObjectName("Dialog")
		self.setWindowTitle("Datos de usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.setFixedSize(920, 514)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()
		self.Mostrar_Datos()


	def initUi(self):		
		# Datos generales
		self.groupBox_datosGnr = QGroupBox(self)
		self.groupBox_datosGnr.setGeometry(QRect(170, 10, 341, 493))
		self.groupBox_datosGnr.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		
		self.groupBox_datosGnr.setObjectName("groupBox_datosGnr")
		self.groupBox_datosGnr.setTitle("               Datos Generales")
		self.groupBox_datosGnr.setAlignment(Qt.AlignHCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosGnr.setGraphicsEffect(self.shadow)

		# 1ºNombre =====================================================================================================    
		self.label_1_nombre = QLabel(self.groupBox_datosGnr)
		self.label_1_nombre.setGeometry(QRect(40, 20, 78, 16))
		self.label_1_nombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_1_nombre.setObjectName("label_1_nombre")
		self.label_1_nombre.setText("<font color='#FF3300'>*</font>1ºNombre:")

		self.lineEdit_1_nombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_nombre.setGeometry(QRect(10, 40, 141, 20))
		self.lineEdit_1_nombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid #113384;\n"
		"}")
		self.lineEdit_1_nombre.setText("")
		self.lineEdit_1_nombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_nombre.setObjectName("lineEdit_1_nombre")
		self.lineEdit_1_nombre.setPlaceholderText("Primer nombre")
		self.lineEdit_1_nombre.setToolTip("Ingresa aquí el primer nombre")

		self.lineEdit_1_nombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1_nombre))

		# 2ºNombre =====================================================================================================
		self.label_2_nombre = QLabel(self.groupBox_datosGnr)
		self.label_2_nombre.setGeometry(QRect(215, 20, 71, 16))
		self.label_2_nombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_2_nombre.setObjectName("label_2_nombre")
		self.label_2_nombre.setText("2ºNombre:")

		self.lineEdit_2_nombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_nombre.setGeometry(QRect(180, 40, 141, 20))
		self.lineEdit_2_nombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_nombre.setText("")
		self.lineEdit_2_nombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_nombre.setObjectName("lineEdit_2_nombre")
		self.lineEdit_2_nombre.setPlaceholderText("Segundo nombre")
		self.lineEdit_2_nombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2_nombre))
		self.lineEdit_2_nombre.setToolTip("Ingresa aquí el segundo nombre")


		# 1º Apellido =====================================================================================================     
		self.label_1_Apellido = QLabel(self.groupBox_datosGnr)
		self.label_1_Apellido.setGeometry(QRect(40, 70, 78, 16))
		self.label_1_Apellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1_Apellido.setAlignment(Qt.AlignCenter)
		self.label_1_Apellido.setObjectName("label_1_Apellido")
		self.label_1_Apellido.setText("<font color='#FF3300'>*</font>1ºApellido:")


		self.lineEdit_1_Apellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_Apellido.setGeometry(QRect(10, 90, 141, 20))
		self.lineEdit_1_Apellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1_Apellido.setText("")        
		self.lineEdit_1_Apellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_Apellido.setObjectName("lineEdit_1ºApellido")
		self.lineEdit_1_Apellido.setPlaceholderText("Primer apellido")
		self.lineEdit_1_Apellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1_Apellido))
		self.lineEdit_1_Apellido.setToolTip("Ingresa aquí el primer apellido")

		# 2º Apellido =====================================================================================================     
		self.lineEdit_2_Apellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_Apellido.setGeometry(QRect(180, 90, 141, 20))
		self.lineEdit_2_Apellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_Apellido.setText("")
		self.lineEdit_2_Apellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_Apellido.setObjectName("lineEdit_2ºApellido")
		self.lineEdit_2_Apellido.setToolTip("Ingresa aquí el segundo apellido")


		self.label_2_Apellido = QLabel(self.groupBox_datosGnr)
		self.label_2_Apellido.setGeometry(QRect(215, 70, 71, 16))
		self.label_2_Apellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2_Apellido.setAlignment(Qt.AlignCenter)
		self.label_2_Apellido.setObjectName("label_2_Apellido")
		self.label_2_Apellido.setText("2ºApellido:")
		self.lineEdit_2_Apellido.setPlaceholderText("Segundo apellido")
		self.lineEdit_2_Apellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2_Apellido))
	   
		# Cedula de identidad =====================================================================================================     
		self.label_cedula = QLabel(self.groupBox_datosGnr)
		self.label_cedula.setGeometry(QRect(10, 125, 140, 16))
		self.label_cedula.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_cedula.setAlignment(Qt.AlignCenter)
		self.label_cedula.setObjectName("label_cedula")
		self.label_cedula.setText("<font color='#FF3300'>*</font>Cedula de intentidad:")

		self.lineEdit_cedula = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_cedula.setGeometry(QRect(10, 145, 141, 20))
		self.lineEdit_cedula.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid #113384;\n"
		"}")
		self.lineEdit_cedula.setText("")
		self.lineEdit_cedula.setAlignment(Qt.AlignCenter)
		self.lineEdit_cedula.setObjectName("lineEdit_cedula")
		self.lineEdit_cedula.setPlaceholderText("Ingresa la cedula")
		self.lineEdit_cedula.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_cedula))
		self.lineEdit_cedula.setToolTip("Ingresa aquí la cedula de identidad")

		# Telefono =====================================================================================================        
		self.label_tlf = QLabel(self.groupBox_datosGnr)
		self.label_tlf.setGeometry(QRect(215, 125, 71, 16))
		self.label_tlf.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_tlf.setAlignment(Qt.AlignCenter)
		self.label_tlf.setObjectName("label_tlf")
		self.label_tlf.setText("<font color='#FF3300'>*</font>Telefonos:")

		self.lineEdit_1_tlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_tlf.setGeometry(QRect(180, 145, 141, 20))
		self.lineEdit_1_tlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1_tlf.setText("")
		self.lineEdit_1_tlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_tlf.setObjectName("lineEdit_1_tlf")
		self.lineEdit_1_tlf.setPlaceholderText("Principal")
		self.lineEdit_1_tlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_1_tlf))
		self.lineEdit_1_tlf.setToolTip("Ingresa aquí el numero telefónico principal")


		self.lineEdit_2_tlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_tlf.setGeometry(QRect(180, 170, 141, 20))
		self.lineEdit_2_tlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_tlf.setText("")
		self.lineEdit_2_tlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_tlf.setObjectName("lineEdit_2_tlf")
		self.lineEdit_2_tlf.setPlaceholderText("Secundario")
		self.lineEdit_2_tlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_2_tlf))
		self.lineEdit_2_tlf.setToolTip("Ingresa aquí el numero de telefónico secundario")

		# Genero ========================================================================================================         
		self.comboBox_genero = QComboBox(self.groupBox_datosGnr)
		self.comboBox_genero.setGeometry(QRect(10, 200, 141, 21))
		self.comboBox_genero.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius:3px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_genero.setEditable(False)
		self.comboBox_genero.setObjectName("comboBox_genero")


		self.items_list_genero = ["Masculino", "Femenino"]
		self.comboBox_genero.addItems(self.items_list_genero)
		self.comboBox_genero.setToolTip("Selecciona el genero ")

		self.label_genero = QLabel(self.groupBox_datosGnr)
		self.label_genero.setGeometry(QRect(45, 180, 71, 16))
		self.label_genero.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_genero.setAlignment(Qt.AlignCenter)
		self.label_genero.setObjectName("label_genero")
		self.label_genero.setText("<font color='#FF3300'>*</font>Genero:")
				
		# Edad ========================================================================================================       
		self.label_edad = QLabel(self.groupBox_datosGnr)
		self.label_edad.setGeometry(QRect(225, 205, 51, 16))
		self.label_edad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_edad.setAlignment(Qt.AlignCenter)
		self.label_edad.setObjectName("label_edad")
		self.label_edad.setText("<font color='#FF3300'>*</font>Edad:")

		self.lineEdit_edad = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_edad.setGeometry(QRect(180, 225, 141, 20))
		self.lineEdit_edad.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_edad.setText("")
		self.lineEdit_edad.setAlignment(Qt.AlignCenter)
		self.lineEdit_edad.setObjectName("lineEdit_edad")
		self.lineEdit_edad.setPlaceholderText("Ingresa la edad")
		self.lineEdit_edad.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_edad))
		self.lineEdit_edad.setToolTip("Ingresa aquí la edad")
	  
		# Fecha de nacimiento ========================================================================================================          
		self.dateEdit_nacimiento = QDateEdit(self.groupBox_datosGnr)
		self.dateEdit_nacimiento.setGeometry(QRect(10, 255, 141, 22))
		self.dateEdit_nacimiento.setStyleSheet("QDateEdit{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"\n"
		"}")
		self.dateEdit_nacimiento.setObjectName("dateEdit_nacimiento")
		self.dateEdit_nacimiento.setDate(QDate.currentDate())
		self.dateEdit_nacimiento.setMaximumDate(QDate.currentDate())
		self.dateEdit_nacimiento.setDisplayFormat("dd/MM/yyyy")
		self.dateEdit_nacimiento.setCalendarPopup(True)
		self.dateEdit_nacimiento.setCursor(Qt.PointingHandCursor)
		self.dateEdit_nacimiento.setToolTip("Selecciona la fecha de nacimiento")

		self.label_fch_nacimiento = QLabel(self.groupBox_datosGnr)
		self.label_fch_nacimiento.setGeometry(QRect(20, 235, 131, 16))
		self.label_fch_nacimiento.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_fch_nacimiento.setAlignment(Qt.AlignCenter)
		self.label_fch_nacimiento.setObjectName("label_fch_nacimiento")
		self.label_fch_nacimiento.setText("Fecha de nacimiento:")

		# Opciones checkbox datos generales ========================================================================================================       
		self.label_opciones = QLabel(self.groupBox_datosGnr)
		self.label_opciones.setGeometry(QRect(180, 260, 141, 19))
		self.label_opciones.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 10px")
		self.label_opciones.setAlignment(Qt.AlignCenter)
		self.label_opciones.setObjectName("label_opciones")
		self.label_opciones.setText("Posee alguna de las opciones:")

		self.checkBox_1_pensionado = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_1_pensionado.setGeometry(QRect(200, 290, 100, 17))
		self.checkBox_1_pensionado.setObjectName("checkBox_1_pensionado")
		self.checkBox_1_pensionado.setText("Pensionado")
		self.checkBox_1_pensionado.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")        

		self.checkBox_4_Embarazada = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_4_Embarazada.setGeometry(QRect(200, 310, 100, 17))
		self.checkBox_4_Embarazada.setObjectName("checkBox_4_Embarazada")
		self.checkBox_4_Embarazada.setText("Embarazada")
		self.checkBox_4_Embarazada.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_5_lactante = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_5_lactante.setGeometry(QRect(200, 330, 100, 17))
		self.checkBox_5_lactante.setObjectName("checkBox_5_lactante")
		self.checkBox_5_lactante.setText("Lactante")
		self.checkBox_5_lactante.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		# Profesion u oficio =================================================================================================
		self.label_profesion = QLabel(self.groupBox_datosGnr)
		self.label_profesion.setGeometry(QRect(30, 290, 101, 16))
		self.label_profesion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_profesion.setAlignment(Qt.AlignCenter)
		self.label_profesion.setObjectName("label_profesion")
		self.label_profesion.setText("Profesión u oficio:")

		self.comboBox_profesion = QComboBox(self.groupBox_datosGnr)
		self.comboBox_profesion.setGeometry(QRect(10, 310, 141, 21))
		self.comboBox_profesion.setToolTip("Selecciona la profesión")
		self.comboBox_profesion.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_profesion.setEditable(False)
		self.comboBox_profesion.setObjectName("comboBox_profesion")

		self.items_list_profesion = ['Contador', 'Albañil', 'Conductor de autobús', 'Carnicero', 'Carpintero',
		'Cocinero','Médico','Enfermero', 'Mecánico','Herrero','Abogado','Trabajador social','Funcionario público',
		'Profesor','Veterinario','Estudiante','Otro...'
		'']

		self.comboBox_profesion.addItems(self.items_list_profesion)

		# Nivel de instruccion ========================================================================================================       
		self.label_nvl_instruccion = QLabel(self.groupBox_datosGnr)
		self.label_nvl_instruccion.setGeometry(QRect(20, 345, 121, 16))
		self.label_nvl_instruccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_nvl_instruccion.setAlignment(Qt.AlignCenter)
		self.label_nvl_instruccion.setObjectName("label_nvl_instruccion")
		self.label_nvl_instruccion.setText("Nivel de instrucción:")

		self.comboBox_nvl_instruccion = QComboBox(self.groupBox_datosGnr)
		self.comboBox_nvl_instruccion.setGeometry(QRect(10, 365, 141, 21))
		self.comboBox_nvl_instruccion.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_nvl_instruccion.setEditable(False)
		self.comboBox_nvl_instruccion.setToolTip("Selecciona el nivel de instrucción")
		self.comboBox_nvl_instruccion.setObjectName("comboBox_nvl_instruccion")

		self.Items_list_instruccion = ['Primaria', 'Bachillerato', 'Técnico superior', 
		'Universitario', 'Especialización', 'Postgrado', 'Doctorado']
		self.comboBox_nvl_instruccion.addItems(self.Items_list_instruccion)

		# Parentesco ========================================================================================================         
		self.label_parentesco = QLabel(self.groupBox_datosGnr)
		self.label_parentesco.setGeometry(QRect(210, 370, 81, 16))
		self.label_parentesco.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_parentesco.setAlignment(Qt.AlignCenter)
		self.label_parentesco.setObjectName("label_parentesco")
		self.label_parentesco.setText("<font color='#FF3300'>*</font>Parentesco:")

		self.comboBox_parentesco = QComboBox(self.groupBox_datosGnr)
		self.comboBox_parentesco.setGeometry(QRect(180, 390, 141, 21))
		self.comboBox_parentesco.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")

		self.comboBox_parentesco.setEditable(False)
		self.comboBox_parentesco.setObjectName("comboBox_parentesco")
		self.comboBox_parentesco.setToolTip("Selecciona el parentesco")

		self.items_list_parentesco = ['Jefe/a de familia', 'Padre', 'Madre', 'Hijo/a', 'Yerno', 'Nuera', 
		'Abuelo/a', 'Nieto/a', 'Hermano/a', 'Cuñado/a', 'Bisabuelo/a', 'Biznieto/a', 'Tío/a', 'Sobrino/a']
		self.comboBox_parentesco.addItems(self.items_list_parentesco)
		
		# Estado civil ========================================================================================================       
		self.label_estadocivil = QLabel(self.groupBox_datosGnr)
		self.label_estadocivil.setGeometry(QRect(45, 400, 71, 16))
		self.label_estadocivil.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_estadocivil.setAlignment(Qt.AlignCenter)
		self.label_estadocivil.setObjectName("label_estadocivil")
		self.label_estadocivil.setText("<font color='#FF3300'>*</font>Estado civil:")

		self.comboBox_estadocivil = QComboBox(self.groupBox_datosGnr)
		self.comboBox_estadocivil.setGeometry(QRect(10, 420, 141, 21))
		self.comboBox_estadocivil.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")

		self.comboBox_estadocivil.setEditable(False)
		self.comboBox_estadocivil.setToolTip("Selecciona el estado civil actual")
		self.comboBox_estadocivil.setObjectName("comboBox_estadocivil")
		self.items_list_estadocivil = ['Soltero', 'Casado']
		self.comboBox_estadocivil.addItems(self.items_list_estadocivil)

		# Inscrito en el REP ========================================================================================================         
		self.label_inscritoREP = QLabel(self.groupBox_datosGnr)
		self.label_inscritoREP.setGeometry(QRect(25, 455, 111, 16))
		self.label_inscritoREP.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_inscritoREP.setAlignment(Qt.AlignCenter)
		self.label_inscritoREP.setObjectName("label_inscritoREP")
		self.label_inscritoREP.setText("Esta inscrito en REP:")

		self.radiobutton_si_inscrito = QRadioButton(self.groupBox_datosGnr)
		self.radiobutton_si_inscrito.setGeometry(QRect(30, 471, 38, 17))
		"color:#000000\n"
		self.radiobutton_si_inscrito.setToolTip("Selecciona 'Si' si está inscrito\n"
												"en el registro electoral permanente")
		self.radiobutton_si_inscrito.setObjectName("radiobutton_si_inscrito")
		self.radiobutton_si_inscrito.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  
		self.radiobutton_si_inscrito.setText("Si")

		self.radiobutton_no_inscrito = QRadioButton(self.groupBox_datosGnr)
		self.radiobutton_no_inscrito.setGeometry(QRect(85, 471, 45, 17))
		self.radiobutton_no_inscrito.setObjectName("radiobutton_no_inscrito")
		self.radiobutton_no_inscrito.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  
		self.radiobutton_no_inscrito.setText("No")
		self.radiobutton_no_inscrito.setToolTip("Selecciona 'No' si no está inscrito\n"
												"en el registro electoral permanente")

		# Ingresar el correo ========================================================================================================         
		self.label_correo = QLabel(self.groupBox_datosGnr)
		self.label_correo.setGeometry(QRect(195, 440, 111, 16))
		self.label_correo.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_correo.setAlignment(Qt.AlignCenter)
		self.label_correo.setObjectName("label_correo")
		self.label_correo.setText("Correo electronico: ")

		self.lineEdit_correo = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_correo.setGeometry(QRect(180, 460, 141, 20))
		self.lineEdit_correo.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_correo.setText("")
		self.lineEdit_correo.setAlignment(Qt.AlignCenter)
		self.lineEdit_correo.setObjectName("lineEdit_correo")
		self.lineEdit_correo.setPlaceholderText("Ingresa el correo")
		self.lineEdit_correo.setToolTip("Ingresa un correo electrónico vigente")

		# Ubicación geográfica
		self.groupBox_datosUb = QGroupBox(self)
		self.groupBox_datosUb.setGeometry(QRect(530, 10, 371, 181))
		self.groupBox_datosUb.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosUb.setAlignment(Qt.AlignCenter)
		self.groupBox_datosUb.setObjectName("groupBox_datosUb")
		self.groupBox_datosUb.setTitle("                        Ubicación geográfica")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosUb.setGraphicsEffect(self.shadow)

		# Estado ========================================================================================================         
		self.label_estado = QLabel(self.groupBox_datosUb)
		self.label_estado.setGeometry(QRect(60, 20, 61, 16))
		self.label_estado.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_estado.setAlignment(Qt.AlignCenter)
		self.label_estado.setObjectName("label_estado")
		self.label_estado.setText("Estado:")

		self.lineEdit_estado = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_estado.setGeometry(QRect(20, 40, 141, 20))
		self.lineEdit_estado.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_estado.setText("")
		self.lineEdit_estado.setAlignment(Qt.AlignCenter)
		self.lineEdit_estado.setObjectName("lineEdit_estado")
		self.lineEdit_estado.setToolTip("Ingresa el estado donde se residencia")
		self.lineEdit_estado.setPlaceholderText("Ingresa el estado")
		self.lineEdit_estado.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_estado))

		# Municipio ========================================================================================================          
		self.label_municipio = QLabel(self.groupBox_datosUb)
		self.label_municipio.setGeometry(QRect(55, 70, 71, 16))
		self.label_municipio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_municipio.setAlignment(Qt.AlignCenter)
		self.label_municipio.setObjectName("label_municipio")
		self.label_municipio.setText("Municipio:")

		self.lineEdit_municipio = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_municipio.setGeometry(QRect(20, 90, 141, 20))
		self.lineEdit_municipio.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_municipio.setText("")
		self.lineEdit_municipio.setAlignment(Qt.AlignCenter)
		self.lineEdit_municipio.setObjectName("lineEdit_municipio")
		self.lineEdit_municipio.setToolTip("Ingresa el municipio donde se residencia")
		self.lineEdit_municipio.setPlaceholderText("Ingresa el municipio")
		self.lineEdit_municipio.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_municipio))


		# Parroquia ========================================================================================================          
		self.label_parroquia = QLabel(self.groupBox_datosUb)
		self.label_parroquia.setGeometry(QRect(55, 120, 71, 16))
		self.label_parroquia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_parroquia.setAlignment(Qt.AlignCenter)
		self.label_parroquia.setObjectName("label_parroquia")
		self.label_parroquia.setText("Parroquia:")

		self.lineEdit_parroquia = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_parroquia.setGeometry(QRect(20, 140, 141, 20))
		self.lineEdit_parroquia.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_parroquia.setText("")
		self.lineEdit_parroquia.setAlignment(Qt.AlignCenter)
		self.lineEdit_parroquia.setObjectName("lineEdit_parroquia")
		self.lineEdit_parroquia.setToolTip("Ingresa la parroquia donde se residencia")
		self.lineEdit_parroquia.setPlaceholderText("Ingresa la parroquia")
		self.lineEdit_parroquia.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_parroquia))

		# Nº de vivienda ========================================================================================================         
		self.label_N_vivienda = QLabel(self.groupBox_datosUb)
		self.label_N_vivienda.setGeometry(QRect(220, 130, 111, 16))
		self.label_N_vivienda.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_N_vivienda.setAlignment(Qt.AlignCenter)
		self.label_N_vivienda.setObjectName("label_N_vivienda")
		self.label_N_vivienda.setText("<font color='#FF3300'>*</font>Nº de vivienda:")

		self.lineEdit_N_vivienda = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_N_vivienda.setGeometry(QRect(205, 150, 141, 20))
		self.lineEdit_N_vivienda.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_N_vivienda.setText("")
		self.lineEdit_N_vivienda.setAlignment(Qt.AlignCenter)
		self.lineEdit_N_vivienda.setObjectName("lineEdit_N_vivienda")
		self.lineEdit_N_vivienda.setToolTip("Ingresa el numero de la vivienda")
		self.lineEdit_N_vivienda.setPlaceholderText("Numero de vivienda")
		self.lineEdit_N_vivienda.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_N_vivienda))


		# Direccion ========================================================================================================          
		self.label_direccion = QLabel(self.groupBox_datosUb) 
		self.label_direccion.setGeometry(QRect(193, 20, 161, 16))
		self.label_direccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_direccion.setAlignment(Qt.AlignCenter)
		self.label_direccion.setObjectName("label_direccion")
		self.label_direccion.setText("<font color='#FF3300'>*</font>Dirección y donde vota:")
		self.textEdit_direccion = QTextEdit(self.groupBox_datosUb)
		self.textEdit_direccion.setGeometry(QRect(193, 40, 161, 71))
		self.textEdit_direccion.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_direccion.setObjectName("textEdit_direccion")
		self.textEdit_direccion.setPlaceholderText("Ingresa la dirección\n"
													"Y lugar donde vota...")
		self.textEdit_direccion.setToolTip("Ingresa la dirección donde se residencia\n"
										   "Y lugar donde vota ")

		# Datos de vivienda---------------------------------------------
		self.groupBox_datos_Vv = QGroupBox(self)
		self.groupBox_datos_Vv.setGeometry(QRect(530, 200, 371, 171))
		self.groupBox_datos_Vv.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datos_Vv.setAlignment(Qt.AlignCenter)
		self.groupBox_datos_Vv.setObjectName("groupBox_datosGnr_Vv")
		self.groupBox_datos_Vv.setTitle("                      Datos de la vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_Vv.setGraphicsEffect(self.shadow)
		# Metros cuadrados ========================================================================================================       
		self.label_M2 = QLabel(self.groupBox_datos_Vv)
		self.label_M2.setGeometry(QRect(25, 20, 121, 16))
		self.label_M2.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_M2.setAlignment(Qt.AlignCenter)
		self.label_M2.setObjectName("label_M2")
		self.label_M2.setText("Metros cuadrados:")

		self.lineEdit_M2 = QLineEdit(self.groupBox_datos_Vv)
		self.lineEdit_M2.setGeometry(QRect(15, 40, 141, 20))
		self.lineEdit_M2.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_M2.setText("")
		self.lineEdit_M2.setAlignment(Qt.AlignCenter)
		self.lineEdit_M2.setObjectName("lineEdit_M2")
		self.lineEdit_M2.setPlaceholderText("Ingresa los metros")
		self.lineEdit_M2.setToolTip("Ejemplo: Si la vivienda posee 12 metro cuadrados,\n"
									"escribirlo de esta manera: 12m^2")
		
		# Servivcios que posee ========================================================================================================            
		self.label_servicios = QLabel(self.groupBox_datos_Vv)
		self.label_servicios.setGeometry(QRect(195, 20, 151, 16))
		self.label_servicios.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_servicios.setAlignment(Qt.AlignCenter)
		self.label_servicios.setObjectName("label_servicios")
		self.label_servicios.setText("Servicios que posee:")

		self.checkBox_aguapotable = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguapotable.setGeometry(QRect(175 ,40, 98, 17))
		self.checkBox_aguapotable.setObjectName("checkBox_aguapotable")
		self.checkBox_aguapotable.setText("Agua potable")
		self.checkBox_aguapotable.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  
		
		self.checkBox_aguasservidas = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguasservidas.setGeometry(QRect(175, 60, 100, 17))
		self.checkBox_aguasservidas.setObjectName("checkBox_aguasservidas")
		self.checkBox_aguasservidas.setText("Aguas servidas")
		self.checkBox_aguasservidas.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_gasdirecto = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasdirecto.setGeometry(QRect(175, 80, 91, 17))
		self.checkBox_gasdirecto.setObjectName("checkBox_gasdirecto")
		self.checkBox_gasdirecto.setText("Gas directo")
		self.checkBox_gasdirecto.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_gasbombona = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasbombona.setGeometry(QRect(175, 100, 111, 17))
		self.checkBox_gasbombona.setObjectName("checkBox_gasbombona")
		self.checkBox_gasbombona.setText("Gas bombona")
		self.checkBox_gasbombona.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")


		self.checkBox_internet = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_internet.setGeometry(QRect(175, 120, 111, 17))
		self.checkBox_internet.setObjectName("checkBox_internet")
		self.checkBox_internet.setText("Internet")
		self.checkBox_internet.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_electricidad = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_electricidad.setGeometry(QRect(175, 140, 111, 17))
		self.checkBox_electricidad.setObjectName("checkBox_electricidad")
		self.checkBox_electricidad.setText("Electricidad")
		self.checkBox_electricidad.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_tlf_fijo = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_tlf_fijo.setGeometry(QRect(270,40, 101, 17))
		self.checkBox_tlf_fijo.setObjectName("checkBox_tlf_fijo")
		self.checkBox_tlf_fijo.setText("Telefono fijo")
		self.checkBox_tlf_fijo.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		# Descripcion de la vivienda ========================================================================================================              
		self.label_dcrp_vv = QLabel(self.groupBox_datos_Vv)
		self.label_dcrp_vv.setGeometry(QRect(10, 80, 151, 16))
		self.label_dcrp_vv.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_dcrp_vv.setAlignment(Qt.AlignCenter)
		self.label_dcrp_vv.setObjectName("label_dcrp_vv")
		self.label_dcrp_vv.setText("Descripción de vivienda:")
		self.textEdit_dcrp_vv = QTextEdit(self.groupBox_datos_Vv)
		self.textEdit_dcrp_vv.setGeometry(QRect(10, 100, 151, 51))
		self.textEdit_dcrp_vv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_vv.setObjectName("textEdit_dcrp_vv")
		self.textEdit_dcrp_vv.setPlaceholderText("Describa la vivienda...")
		self.textEdit_dcrp_vv.setToolTip("Describa la vivienda si es una casa de una planta o dos,\n"
										"si es un apartamento o quinta, entre otras... ")

		# Proteccion Social	 ===================================================
		self.groupBox_beneficios = QGroupBox(self)
		self.groupBox_beneficios.setGeometry(QRect(530, 380, 371, 123))
		self.groupBox_beneficios.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_beneficios.setAlignment(Qt.AlignCenter)
		self.groupBox_beneficios.setObjectName("groupBox_beneficios")
		self.groupBox_beneficios.setTitle("                  Proteccion social")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_beneficios.setGraphicsEffect(self.shadow)

		# Posee algun beneficio ========================================================================================================               
		self.label_beneficio = QLabel(self.groupBox_beneficios)
		self.label_beneficio.setGeometry(QRect(10, 20, 161, 16))
		self.label_beneficio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_beneficio.setAlignment(Qt.AlignCenter)
		self.label_beneficio.setObjectName("label_beneficio")
		self.label_beneficio.setText("Posee algun beneficio:")

		self.checkBox_hogarespatria = QCheckBox(self.groupBox_beneficios)
		self.checkBox_hogarespatria.setGeometry(QRect(10, 40, 151, 17))
		self.checkBox_hogarespatria.setObjectName("checkBox_hogarespatria")
		self.checkBox_hogarespatria.setText("Hogares de la patria")
		self.checkBox_hogarespatria.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"        
		"}")  

		self.checkBox_partohumanizado = QCheckBox(self.groupBox_beneficios)
		self.checkBox_partohumanizado.setGeometry(QRect(10, 100, 141, 20))
		self.checkBox_partohumanizado.setObjectName("checkBox_partohumanizado")
		self.checkBox_partohumanizado.setText("Parto humanizado")
		self.checkBox_partohumanizado.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_amormayor = QCheckBox(self.groupBox_beneficios)
		self.checkBox_amormayor.setGeometry(QRect(10, 60, 101, 17))
		self.checkBox_amormayor.setObjectName("checkBox_amormayor")
		self.checkBox_amormayor.setText("Amor mayor")
		self.checkBox_amormayor.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_joseGregorio  = QCheckBox(self.groupBox_beneficios)
		self.checkBox_joseGregorio.setGeometry(QRect(10, 80, 181, 17))
		self.checkBox_joseGregorio.setObjectName("checkBox_joseGregorio")
		self.checkBox_joseGregorio.setText("Dr. José Gregorio Hernández")
		self.checkBox_joseGregorio.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.label_grpsociales = QLabel(self.groupBox_beneficios)
		self.label_grpsociales.setGeometry(QRect(185,20,171,16))
		self.label_grpsociales.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_grpsociales.setAlignment(Qt.AlignCenter)
		self.label_grpsociales.setObjectName("label_grpsociales")
		self.label_grpsociales.setText("Esta en algun grupo social:")


		self.checkBox_somosvenezuela = QCheckBox(self.groupBox_beneficios)
		self.checkBox_somosvenezuela.setGeometry(QRect(200, 60, 131, 17))
		self.checkBox_somosvenezuela.setObjectName("checkBox_somosvenezuela")
		self.checkBox_somosvenezuela.setText("Somos Venezuela")
		self.checkBox_somosvenezuela.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_chambajuvenil = QCheckBox(self.groupBox_beneficios)
		self.checkBox_chambajuvenil.setGeometry(QRect(200, 40, 121, 17))
		self.checkBox_chambajuvenil.setObjectName("checkBox_chambajuvenil")
		self.checkBox_chambajuvenil.setText("Chamba juvenil")
		self.checkBox_chambajuvenil.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_FrenteMiranda = QCheckBox(self.groupBox_beneficios)
		self.checkBox_FrenteMiranda.setGeometry(QRect(200, 80, 191, 17))
		self.checkBox_FrenteMiranda.setObjectName("checkBox_FrenteMiranda")
		self.checkBox_FrenteMiranda.setText("Frente Francisco Miranda")
		self.checkBox_FrenteMiranda.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_jpsuv = QCheckBox(self.groupBox_beneficios)
		self.checkBox_jpsuv.setGeometry(QRect(200, 100, 141, 17))
		self.checkBox_jpsuv.setObjectName("checkBox_jpsuv")
		self.checkBox_jpsuv.setText("JPSUV")
		self.checkBox_jpsuv.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		# Lines
		# Line bajo Nombre-Apellido =====================================================================================   
		self.line = QFrame(self.groupBox_datosGnr)
		self.line.setGeometry(QRect(10, 110, 311, 16))
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)
		self.line.setObjectName("line")
		
		# Line bajo cedula ==============================================================================================       
		self.line_5 = QFrame(self.groupBox_datosGnr)
		self.line_5.setGeometry(QRect(10, 165, 141, 16))
		self.line_5.setFrameShape(QFrame.HLine)
		self.line_5.setFrameShadow(QFrame.Sunken)
		self.line_5.setObjectName("line_5")            

		# Line bajo telefono ===========================================================================================         
		self.line_3 = QFrame(self.groupBox_datosGnr)
		self.line_3.setGeometry(QRect(180, 190, 141, 16))
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)
		self.line_3.setObjectName("line_3")

		# Line bajo genero ========================================================================================================       
		self.line_2 = QFrame(self.groupBox_datosGnr)
		self.line_2.setGeometry(QRect(10, 220, 141, 16))
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)
		self.line_2.setObjectName("line_2")
	   
		# Line bajo edad ========================================================================================================         
		self.line_8 = QFrame(self.groupBox_datosGnr)
		self.line_8.setGeometry(QRect(180, 245, 141, 16))
		self.line_8.setFrameShape(QFrame.HLine)
		self.line_8.setFrameShadow(QFrame.Sunken)
		self.line_8.setObjectName("line_8")

		# Line bajo fecha de nacimiento ==========================================================================================      
		self.line_4 = QFrame(self.groupBox_datosGnr)
		self.line_4.setGeometry(QRect(10, 275, 141, 16))
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)
		self.line_4.setObjectName("line_4")
	   
		# Line bajo profesion u oficio ==========================================================================================      
		self.line_6 = QFrame(self.groupBox_datosGnr)
		self.line_6.setGeometry(QRect(10, 330, 141, 16))
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)
		self.line_6.setObjectName("line_6")

		# Line bajo nivel de instruccion ==========================================================================================      
		self.line_7 = QFrame(self.groupBox_datosGnr)
		self.line_7.setGeometry(QRect(10, 385, 141, 16))
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)
		self.line_7.setObjectName("line_7")       
		
		# Line bajo opciones checkbox ==========================================================================================      
		self.line_9 = QFrame(self.groupBox_datosGnr)
		self.line_9.setGeometry(QRect(180, 350, 141, 16))
		self.line_9.setFrameShape(QFrame.HLine)
		self.line_9.setFrameShadow(QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		
		# Line bajo estado civil ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(10, 440, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")

		# Line bajo parentesco ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(180, 420, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")


		# Line bajo direccion ==========================================================================================      
		self.line_10 = QFrame(self.groupBox_datosUb)
		self.line_10.setGeometry(QRect(193, 110, 161, 16))
		self.line_10.setFrameShape(QFrame.HLine)
		self.line_10.setFrameShadow(QFrame.Sunken)
		self.line_10.setObjectName("line_10")

		# Line bajo metros cuadrados ==========================================================================================      
		self.line_11 = QFrame(self.groupBox_datos_Vv)
		self.line_11.setGeometry(QRect(15, 63, 141, 16))
		self.line_11.setFrameShape(QFrame.HLine)
		self.line_11.setFrameShadow(QFrame.Sunken)
		self.line_11.setObjectName("line_11")		

		self.frame_nv_user = QFrame(self)
		self.frame_nv_user.setGeometry(QRect(20, 10, 121, 493))
		self.frame_nv_user.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"\n"
		"}")
		self.frame_nv_user.setFrameShape(QFrame.StyledPanel)
		self.frame_nv_user.setFrameShadow(QFrame.Raised)
		self.frame_nv_user.setObjectName("frame_nv_user")

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_nv_user.setGraphicsEffect(self.shadow)

		self.label_13 = QLabel(self.frame_nv_user)
		self.label_13.setGeometry(QRect(25, 10, 141,20))
		self.label_13.setText("USUARIO")    
		self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"border-radius:6px\n"
		"")

		# Botones de ventana registro de usuario
		# Boton educacion ==========================================================================================            
		self.Button_educacion = QPushButton(self.frame_nv_user)
		self.Button_educacion.setGeometry(QRect(-20,320, 151, 31))
		self.Button_educacion.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_educacion.setText("Educación")
		self.Button_educacion.setIcon(QIcon(":/Icono_edicacion/Imagenes-iconos/educacion.png"))
		self.Button_educacion.setIconSize(QSize(19,19))

		# Boton datos vivienda==========================================================================================            
		self.Button_vivienda = QPushButton(self.frame_nv_user)
		self.Button_vivienda.setGeometry(QRect(-25,290, 151, 31))
		self.Button_vivienda.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_vivienda.setText("Vivienda")
		self.Button_vivienda.setIcon(QIcon(":/Icono_casa/Imagenes-iconos/casa_blanco.png"))
		self.Button_vivienda.setIconSize(QSize(16,16))

		# Boton Enfermedad ==========================================================================================           
		self.Button_enfermedad = QPushButton(self.frame_nv_user)
		self.Button_enfermedad.setGeometry(QRect(0,260, 121, 31))
		self.Button_enfermedad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_enfermedad.setText("Enfermedad")
		self.Button_enfermedad.setIcon(QIcon(":/Icono_enfermedad/Imagenes-iconos/Enfermedad.png"))
		self.Button_enfermedad.setIconSize(QSize(18,18))

		# Boton Discapacidad ==========================================================================================             
		self.Button_discapacidad = QPushButton(self.frame_nv_user)
		self.Button_discapacidad.setGeometry(QRect(0,230, 121, 31))
		self.Button_discapacidad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_discapacidad.setText("Discapacidad")
		self.Button_discapacidad.setIcon(QIcon(":/Icono_Discapacidad/Imagenes-iconos/discapacidad_blanco.png"))
		self.Button_discapacidad.setIconSize(QSize(20,20))
		
		# Boton registrar ==========================================================================================            
		self.Button_guardar_user = QPushButton(self.frame_nv_user)
		self.Button_guardar_user.setGeometry(QRect(0, 130, 121, 30))
		self.Button_guardar_user.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_guardar_user.setText("Guardar")
		self.Button_guardar_user.setIcon(QIcon(":/Icono_guardar/Imagenes-iconos/Guardar_blanco.png"))
		self.Button_guardar_user.setIconSize(QSize(20,20))

		# Boton cancelar ==========================================================================================             
		self.Button_cancel_user = QPushButton(self.frame_nv_user)
		self.Button_cancel_user.setGeometry(QRect(0, 160, 121, 31))
		self.Button_cancel_user.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_cancel_user.setText("Cancelar") 
		self.Button_cancel_user.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancel_user.setIconSize(QSize(17,17))   

		# Ventana de discapacidad
		self.frame_principal_discapacidad = QFrame(self)
		self.frame_principal_discapacidad.setGeometry(QRect(20, 20, 600, 300))
		self.frame_principal_discapacidad.setObjectName("frame_principal_discapacidad")
		self.frame_principal_discapacidad.setStyleSheet("QFrame#frame_principal_discapacidad{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius:22px"
		"}\n"
		"")

		self.frame_principal_discapacidad.setFrameShape(QFrame.StyledPanel)
		self.frame_principal_discapacidad.setFrameShadow(QFrame.Raised)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_principal_discapacidad.setGraphicsEffect(self.shadow)
		self.frame_principal_discapacidad.move(210,1000)

		self.frame_2 = QFrame(self.frame_principal_discapacidad)
		self.frame_2.setGeometry(QRect(20, 20, 121, 250))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"}")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Discapacidad")

		# Group de discapacidad ========================================================================================================               
		self.groupBox_datosdiscapacidad = QGroupBox(self.frame_principal_discapacidad)
		self.groupBox_datosdiscapacidad.setGeometry(QRect(160, 20, 410, 251))
		self.groupBox_datosdiscapacidad.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosdiscapacidad.setAlignment(Qt.AlignCenter)
		self.groupBox_datosdiscapacidad.setObjectName("groupBox_datosdiscapacidad")
		self.groupBox_datosdiscapacidad.setTitle("Discapacidad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosdiscapacidad.setGraphicsEffect(self.shadow)
		
		# Descripcion de discapacidad ========================================================================================================             
		self.textEdit_dcrp_discapacidad = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_dcrp_discapacidad.setGeometry(QRect(250, 40, 141, 91))
		self.textEdit_dcrp_discapacidad.setStyleSheet("QTextEdit#textEdit_dcrp_discapacidad{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_discapacidad.setObjectName("textEdit_dcrp_discapacidad")
		self.textEdit_dcrp_discapacidad.setPlaceholderText("Describa la discapacidad...")
		
		self.dcrp_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.dcrp_discapacidad.setGeometry(QRect(245, 20, 151, 16))
		self.dcrp_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_discapacidad.setAlignment(Qt.AlignCenter)
		self.dcrp_discapacidad.setObjectName("dcrp_discapacidad")
		self.dcrp_discapacidad.setText("Describa la discapacidad:")

		# Opciones de discapacidad ========================================================================================================            
		self.label_opciones_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.label_opciones_discapacidad.setGeometry(QRect(10, 20, 221, 16))
		self.label_opciones_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")
		self.label_opciones_discapacidad.setAlignment(Qt.AlignCenter)
		self.label_opciones_discapacidad.setObjectName("label_opciones_discapacidad")
		self.label_opciones_discapacidad.setText("Posee alguna de estas discapacidades:")

		self.checkBox_27_Dscp_motriz =QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_27_Dscp_motriz.setGeometry(QRect(10, 120, 200, 17))
		self.checkBox_27_Dscp_motriz.setText("Discapacidad Motriz")
		self.checkBox_27_Dscp_motriz.setToolTip("Implica una disminución de la movilidad total o parcial \n" 
									"de uno o más miembros del cuerpo, la cual dificulta la realización\n"
									"de actividades motoras convencionales.")
		self.checkBox_27_Dscp_motriz.setObjectName("checkBox_27_Dscp_motriz")
		self.checkBox_27_Dscp_motriz.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_Dscp_auditiva = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_26_Dscp_auditiva.setGeometry(QRect(10, 80, 200, 17))
		self.checkBox_26_Dscp_auditiva.setText("Discapacidad Auditiva")
		self.checkBox_26_Dscp_auditiva.setToolTip("Es un déficit total o parcial en la percepción que se evalúa\n" 
									"por el grado de pérdida de la audición en cada oído")
		self.checkBox_26_Dscp_auditiva.setObjectName("checkBox_26_Dscp_auditiva")
		self.checkBox_26_Dscp_auditiva.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_Dscp_visual = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_25_Dscp_visual.setGeometry(QRect(10, 60, 200, 17))
		self.checkBox_25_Dscp_visual.setText("Discapacidad Visual")
		self.checkBox_25_Dscp_visual.setObjectName("checkBox_25_Dscp_visual")
		self.checkBox_25_Dscp_visual.setToolTip("Es de acuerdo al grado de limitación de la visión, se suele distinguir entre personas ciegas,\n" 
									"que no obtienen información a través del canal visual; y personas con disminución visual,\n"
									"quienes en cambio sí la adquieren mediante dicho canal pero con algún déficit.")
		self.checkBox_25_Dscp_visual.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_Dscp_mental = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_23_Dscp_mental.setGeometry(QRect(10, 40, 220, 17))
		self.checkBox_23_Dscp_mental.setText("Discapacidad Intelectual o mental")
		self.checkBox_23_Dscp_mental.setObjectName("checkBox_23_Dscp_mental")
		self.checkBox_23_Dscp_mental.setToolTip("Las personas con discapacidad intelectual tienen algunas limitaciones\n"
									"para funcionar en su vida diaria; les cuesta más aprender habilidades\n"
									"sociales e intelectuales para acutar en diferentes situaciones.")
		self.checkBox_23_Dscp_mental.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_Dscp_viceral = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_24_Dscp_viceral.setGeometry(QRect(10, 100, 200, 17))
		self.checkBox_24_Dscp_viceral.setText("Discapacidad visceral")
		self.checkBox_24_Dscp_viceral.setObjectName("checkBox_24_Dscp_viceral")
		self.checkBox_24_Dscp_viceral.setToolTip("Las personas con discapacidad visceral son aquellos individuos que, debido a alguna deficiencia \n"
									"en la función de órganos internos, por ejemplo, el cardíaco o el diabético, se encuentran impedidas de \n"
									"desarrollar su vida con total plenitud (aunque no tengan complicaciones en el campo intelectual, \n"
									"en sus funciones sensoriales o motoras)")
		self.checkBox_24_Dscp_viceral.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_otras = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otras.setGeometry(QRect(10, 140, 200, 17))
		self.checkBox_otras.setText("Otra...")
		self.checkBox_otras.setObjectName("checkBox_otras")
		self.checkBox_otras.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# Opciones de medicamentos ========================================================================================================            
		self.label_medicamentos = QLabel(self.groupBox_datosdiscapacidad)
		self.label_medicamentos.setGeometry(QRect(240, 140, 161, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos_dscp = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_si_medicamentos_dscp.setGeometry(QRect(270, 160, 45, 17))
		self.radioButton_si_medicamentos_dscp.setObjectName("radioButton_si_medicamentos_dscp")
		self.radioButton_si_medicamentos_dscp.setText("Si")
		self.radioButton_si_medicamentos_dscp.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos_dscp = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_no_medicamentos_dscp.setGeometry(QRect(330, 160, 45, 17))
		self.radioButton_no_medicamentos_dscp.setObjectName("radioButton_no_medicamentos_dscp")
		self.radioButton_no_medicamentos_dscp.setText("No")
		self.radioButton_no_medicamentos_dscp.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento_dscp = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_medicamento_dscp.setGeometry(QRect(250, 180, 141, 61))
		self.textEdit_medicamento_dscp.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento_dscp.setObjectName("textEdit_medicamento_dscp")
		self.textEdit_medicamento_dscp.setPlaceholderText("Escriba el medicamento...")

		self.label_insumomedico = QLabel(self.groupBox_datosdiscapacidad)
		self.label_insumomedico.setGeometry(QRect(20, 160, 190, 16))
		self.label_insumomedico.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_insumomedico.setAlignment(Qt.AlignCenter)
		self.label_insumomedico.setObjectName("label_insumomedico")
		self.label_insumomedico.setText("Necesita algún insumo medico:")

		self.checkBox_sillarueda = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_sillarueda.setGeometry(QRect(10, 180, 200, 17))
		self.checkBox_sillarueda.setText("Silla de rueda")
		self.checkBox_sillarueda.setObjectName("checkBox_sillarueda")
		self.checkBox_sillarueda.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_muletas = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_muletas.setGeometry(QRect(10, 200, 200, 17))
		self.checkBox_muletas.setText("Muletas")
		self.checkBox_muletas.setObjectName("checkBox_muletas")
		self.checkBox_muletas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_protesis = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_protesis.setGeometry(QRect(10, 220, 200, 17))
		self.checkBox_protesis.setText("Prótesis")
		self.checkBox_protesis.setObjectName("checkBox_protesis")
		self.checkBox_protesis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_otros = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otros.setGeometry(QRect(130, 180, 90, 17))
		self.checkBox_otros.setText("Otros...")
		self.checkBox_otros.setObjectName("checkBox_otros")
		self.checkBox_otros.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		# Botones ventana discapacidad		
		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_discapacidad = QPushButton(self.frame_2)
		self.pushButton_aceptar_discapacidad.setGeometry(QRect(-12, 80, 141, 31))
		self.pushButton_aceptar_discapacidad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_discapacidad.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_discapacidad.setText("Aceptar")
		self.pushButton_aceptar_discapacidad.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_discapacidad.setIconSize(QSize(15,15))
		
		# Boton Cancelar ==========================================================================================             
		self.pushButton_cancelar_discapacidad = QPushButton(self.frame_2)
		self.pushButton_cancelar_discapacidad.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar_discapacidad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_discapacidad.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_discapacidad.setText("Cancelar")
		self.pushButton_cancelar_discapacidad.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_discapacidad.setIconSize(QSize(15,15))

		# Ventana Enfermedad
		self.frame_principal_Enfermedad = QFrame(self)
		self.frame_principal_Enfermedad.setGeometry(QRect(190,200,600,294))
		self.frame_principal_Enfermedad.setStyleSheet("QFrame#frame_principal_Enfermedad{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_Enfermedad.move(220,1000)
		self.frame_principal_Enfermedad.setObjectName("frame_principal_Enfermedad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_Enfermedad.setGraphicsEffect(self.shadow)

		# Group de enfermedad ========================================================================================================             
		self.groupBox_datos_enfermedad = QGroupBox(self.frame_principal_Enfermedad)
		self.groupBox_datos_enfermedad.setGeometry(QRect(160, 20, 421, 251))
		self.groupBox_datos_enfermedad.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datos_enfermedad.setAlignment(Qt.AlignCenter)
		self.groupBox_datos_enfermedad.setObjectName("groupBox_datos_enfermedad")
		self.groupBox_datos_enfermedad.setTitle("Enfermedad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_enfermedad.setGraphicsEffect(self.shadow)
		
		# Descripcion de enfermedad ========================================================================================================               
		self.textEdit_dcrp_enfermedad = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_dcrp_enfermedad.setGeometry(QRect(265, 40, 141, 91))
		self.textEdit_dcrp_enfermedad.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_enfermedad.setObjectName("textEdit_dcrp_enfermedad")
		self.textEdit_dcrp_enfermedad.setPlaceholderText("Describa la enfermedad...")

		self.dcrp_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.dcrp_enfermedad.setGeometry(QRect(260, 20, 151, 16))
		self.dcrp_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_enfermedad.setAlignment(Qt.AlignCenter)
		self.dcrp_enfermedad.setObjectName("dcrp_enfermedad")
		self.dcrp_enfermedad.setText("Describa la enfermedad:")

		# Opciones de enfermedad ========================================================================================================              
		self.label_opciones_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.label_opciones_enfermedad.setGeometry(QRect(10, 20, 241, 16))
		self.label_opciones_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opciones_enfermedad.setAlignment(Qt.AlignCenter)
		self.label_opciones_enfermedad.setObjectName("label_opciones_enfermedad")
		self.label_opciones_enfermedad.setText("Posee alguna de estas enfermedades:")

		self.checkBox_27_cancer = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_27_cancer.setGeometry(QRect(40, 120, 70, 17))
		self.checkBox_27_cancer.setText("Cáncer")
		self.checkBox_27_cancer.setObjectName("checkBox_27_cancer")
		self.checkBox_27_cancer.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_diabetes = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_26_diabetes.setGeometry(QRect(40, 80, 100, 17))
		self.checkBox_26_diabetes.setText("Diabetes")
		self.checkBox_26_diabetes.setObjectName("checkBox_26_diabetes")
		self.checkBox_26_diabetes.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_hp_arterial = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_25_hp_arterial.setGeometry(QRect(40, 60, 200, 17))
		self.checkBox_25_hp_arterial.setText("Hipertensión arterial")
		self.checkBox_25_hp_arterial.setObjectName("checkBox_25_hp_arterial")
		self.checkBox_25_hp_arterial.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_asma = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_23_asma.setGeometry(QRect(40, 40, 70, 17))
		self.checkBox_23_asma.setText("Asma")
		self.checkBox_23_asma.setObjectName("checkBox_23_asma")
		self.checkBox_23_asma.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_vascular = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_24_vascular.setGeometry(QRect(40, 100, 200, 17))
		self.checkBox_24_vascular.setText("Cardio Vascular")
		self.checkBox_24_vascular.setObjectName("checkBox_24_vascular")
		self.checkBox_24_vascular.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_28_gastritis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_28_gastritis.setGeometry(QRect(40, 140, 70, 17))
		self.checkBox_28_gastritis.setText("Gastritis")
		self.checkBox_28_gastritis.setObjectName("checkBox_28_gastritis")
		self.checkBox_28_gastritis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_29_bronquitis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_29_bronquitis.setGeometry(QRect(40, 160, 100, 17))
		self.checkBox_29_bronquitis.setText("Bronquitis")
		self.checkBox_29_bronquitis.setObjectName("checkBox_29_bronquitis")
		self.checkBox_29_bronquitis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_30_calcu_rinon = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_30_calcu_rinon.setGeometry(QRect(40, 180, 200, 17))
		self.checkBox_30_calcu_rinon.setText("Cálculos de riñón")
		self.checkBox_30_calcu_rinon.setObjectName("checkBox_30_calcu_riñon")
		self.checkBox_30_calcu_rinon.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_31_sinusitis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_31_sinusitis.setGeometry(QRect(40, 200, 70, 17))
		self.checkBox_31_sinusitis.setText("Sinusitis")
		self.checkBox_31_sinusitis.setObjectName("checkBox_31_sinusitis")
		self.checkBox_31_sinusitis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_32_otra_enf = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_32_otra_enf.setGeometry(QRect(40, 220, 70, 17))
		self.checkBox_32_otra_enf.setText("Otra...")
		self.checkBox_32_otra_enf.setObjectName("checkBox_32_otra_enf")
		self.checkBox_32_otra_enf.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# Opciones de medicamentos ========================================================================================================            
		self.label_medicamentos = QLabel(self.groupBox_datos_enfermedad)
		self.label_medicamentos.setGeometry(QRect(255, 140, 160, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos_enfer = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_si_medicamentos_enfer.setGeometry(QRect(280, 160, 41, 17))
		self.radioButton_si_medicamentos_enfer.setObjectName("radioButton_si_medicamentos_enfer")
		self.radioButton_si_medicamentos_enfer.setText("Si")
		self.radioButton_si_medicamentos_enfer.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos_enfer = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_no_medicamentos_enfer.setGeometry(QRect(350, 160, 51, 17))
		self.radioButton_no_medicamentos_enfer.setObjectName("radioButton_no_medicamentos_enfer")
		self.radioButton_no_medicamentos_enfer.setText("No")
		self.radioButton_no_medicamentos_enfer.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento_enfer = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_medicamento_enfer.setGeometry(QRect(265, 180, 141, 61))
		self.textEdit_medicamento_enfer.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento_enfer.setObjectName("textEdit_medicamento_enfer")
		self.textEdit_medicamento_enfer.setPlaceholderText("Escriba el medicamento...")

		self.frame_2_enfer = QFrame(self.frame_principal_Enfermedad)
		self.frame_2_enfer.setGeometry(QRect(20, 20, 121, 251))
		self.frame_2_enfer.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px;\n"
		"}")
		self.frame_2_enfer.setFrameShape(QFrame.StyledPanel)
		self.frame_2_enfer.setFrameShadow(QFrame.Raised)
		self.frame_2_enfer.setObjectName("frame_2_enfer")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2_enfer)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Enfermedad")

		# + BOTONES DE LA VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+        
		
		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_Enfermedad = QPushButton(self.frame_2_enfer)
		self.pushButton_aceptar_Enfermedad.setGeometry(QRect(-12, 80, 141, 31))
		self.pushButton_aceptar_Enfermedad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_Enfermedad.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_Enfermedad.setText("Aceptar")
		self.pushButton_aceptar_Enfermedad.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_Enfermedad.setIconSize(QSize(15,15))
		
		# Boton Cancelar ==========================================================================================             
		self.pushButton_cancelar_Enfermedad = QPushButton(self.frame_2_enfer)
		self.pushButton_cancelar_Enfermedad.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar_Enfermedad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_Enfermedad.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_Enfermedad.setText("Cancelar")
		self.pushButton_cancelar_Enfermedad.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_Enfermedad.setIconSize(QSize(15,15))

		# Ventana de Reparacion vivienda
		self.frame_principal_rpr_vv = QFrame(self)
		self.frame_principal_rpr_vv.setGeometry(QRect(190,-200,675,450))
		self.frame_principal_rpr_vv.setStyleSheet("QFrame#frame_principal_rpr_vv{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_rpr_vv.move(180,1000)
		self.frame_principal_rpr_vv.setObjectName("frame_principal_rpr_vv")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_rpr_vv.setGraphicsEffect(self.shadow)


		# GroupBox detalle de reparacion de vivienda ==========================================================================================             
		self.groupBox_dcrp_reparacionvv = QGroupBox(self.frame_principal_rpr_vv)
		self.groupBox_dcrp_reparacionvv.setGeometry(QRect(170, 20, 481, 410))
		self.groupBox_dcrp_reparacionvv.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_dcrp_reparacionvv.setAlignment(Qt.AlignCenter)
		self.groupBox_dcrp_reparacionvv.setObjectName("groupBox_dcrp_reparacionvv")
		self.groupBox_dcrp_reparacionvv.setTitle("Detalles de reparación de vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_dcrp_reparacionvv.setGraphicsEffect(self.shadow)

		# Descripcion de la reparacion de vivienda ==========================================================================================           
		self.textEdit_dcrp_reparacionvv = QTextEdit(self.groupBox_dcrp_reparacionvv)
		self.textEdit_dcrp_reparacionvv.setGeometry(QRect(260, 50, 211, 90))
		self.textEdit_dcrp_reparacionvv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_reparacionvv.setObjectName("textEdit_dcrp_reparacionvv")
		self.textEdit_dcrp_reparacionvv.setPlaceholderText("Describa la reparación...")

		self.label_26 = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_26.setGeometry(QRect(290, 30, 151, 16))
		self.label_26.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_26.setAlignment(Qt.AlignCenter)
		self.label_26.setObjectName("label_26")
		self.label_26.setText("Describa la reparacion:")


		self.label_linea_blanca = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_linea_blanca.setGeometry(QRect(290, 150, 151, 16))
		self.label_linea_blanca.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_linea_blanca.setAlignment(Qt.AlignCenter)
		self.label_linea_blanca.setObjectName("label_linea_blanca")
		self.label_linea_blanca.setText("Necesita linea blanca:")

		self.checkBox_Lavadora = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Lavadora.setGeometry(QRect(280, 170,100,16))
		self.checkBox_Lavadora.setText("Lavadora")
		self.checkBox_Lavadora.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_Nevera = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Nevera.setGeometry(QRect(380, 170,100,16))
		self.checkBox_Nevera.setText("Nevera")
		self.checkBox_Nevera.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_Cocina = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Cocina.setGeometry(QRect(280, 190,100,16))
		self.checkBox_Cocina.setText("Cocina")
		self.checkBox_Cocina.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")


		self.checkBox_Aireacondicionado = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Aireacondicionado.setGeometry(QRect(280, 210,160,16))
		self.checkBox_Aireacondicionado.setText("Aire acondicionado")
		self.checkBox_Aireacondicionado.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")
		
		# Opciones de reparacion de vivienda ==========================================================================================             
		self.label_opc_reparacion = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_opc_reparacion.setGeometry(QRect(10, 30, 238, 16))
		self.label_opc_reparacion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opc_reparacion.setAlignment(Qt.AlignCenter)
		self.label_opc_reparacion.setObjectName("label_opc_reparacion")
		self.label_opc_reparacion.setText("Necesita alguna de estas reparaciones:")

		self.checkBox_arreglo_techos = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_arreglo_techos.setGeometry(QRect(20, 60, 180, 17))
		self.checkBox_arreglo_techos.setText("Arreglo o falta de techos")
		self.checkBox_arreglo_techos.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_2_friso = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_2_friso.setGeometry(QRect(20, 80, 180, 17))
		self.checkBox_2_friso.setText("Friso de pared")
		self.checkBox_2_friso.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_3_pintura = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_3_pintura.setGeometry(QRect(20, 100, 180, 17))
		self.checkBox_3_pintura.setText("Falta de pintura ")
		self.checkBox_3_pintura.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_4_arreglo_Pisos = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_4_arreglo_Pisos.setGeometry(QRect(20, 120, 180, 17))
		self.checkBox_4_arreglo_Pisos.setText("Arreglo de pisos")
		self.checkBox_4_arreglo_Pisos.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_5_sistema_electrico = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_5_sistema_electrico.setGeometry(QRect(20, 140, 180, 17))
		self.checkBox_5_sistema_electrico.setText("Sistema eléctrico")
		self.checkBox_5_sistema_electrico.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_6_sistema_agua = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_6_sistema_agua.setGeometry(QRect(20, 160, 180, 17))
		self.checkBox_6_sistema_agua.setText("Sistema de agua")
		self.checkBox_6_sistema_agua.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_7_aguas_servidas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_7_aguas_servidas.setGeometry(QRect(20, 180, 180, 17))
		self.checkBox_7_aguas_servidas.setText("Sistema de aguas servida")
		self.checkBox_7_aguas_servidas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_8_fatla_ventanas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_8_fatla_ventanas.setGeometry(QRect(20, 200, 180, 17))
		self.checkBox_8_fatla_ventanas.setText("Falta de ventanas")
		self.checkBox_8_fatla_ventanas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_9_falta_puertas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_9_falta_puertas.setGeometry(QRect(20, 220, 180, 17))
		self.checkBox_9_falta_puertas.setText("Falta de puertas")
		self.checkBox_9_falta_puertas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_10_otras_rpr = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_10_otras_rpr.setGeometry(QRect(20, 240, 180, 17))
		self.checkBox_10_otras_rpr.setText("Otras...")
		self.checkBox_10_otras_rpr.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")
		
		# Datos de bombona ==========================================================================================           
		self.label_tipo_cilindro = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_tipo_cilindro.setGeometry(QRect(20, 270, 160, 16))
		self.label_tipo_cilindro.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")
		self.label_tipo_cilindro.setAlignment(Qt.AlignCenter)
		self.label_tipo_cilindro.setText("Tipo de cilindro que posee: ")

		self.checkBox_27_pdvsa_gas =QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_27_pdvsa_gas.setGeometry(QRect(20, 290, 200, 17))
		self.checkBox_27_pdvsa_gas.setText("PDVSA Gas")
		self.checkBox_27_pdvsa_gas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_tropiven = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_26_tropiven.setGeometry(QRect(20, 310, 200, 17))
		self.checkBox_26_tropiven.setText("Tropiven")
		self.checkBox_26_tropiven.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_dani_gas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_25_dani_gas.setGeometry(QRect(20, 330, 200, 17))
		self.checkBox_25_dani_gas.setText("Dani el gas")
		self.checkBox_25_dani_gas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_hermagas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_23_hermagas.setGeometry(QRect(20, 350, 220, 17))
		self.checkBox_23_hermagas.setText("Hermagas")
		self.checkBox_23_hermagas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_autogas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_24_autogas.setGeometry(QRect(20, 370, 200, 17))
		self.checkBox_24_autogas.setText("Autogas")

		self.checkBox_24_autogas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# QSpinBox de cantidad de bombonas  ==========================================================================================              

		self.label_num_bombonas = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_num_bombonas.setGeometry(QRect(290,290,160,16))
		self.label_num_bombonas.setText("Cuantas bombonas posee:")
		self.label_num_bombonas.setAlignment(Qt.AlignCenter)
		self.label_num_bombonas.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")

		self.num_bombonas = QSpinBox(self.groupBox_dcrp_reparacionvv)
		self.num_bombonas.setGeometry(QRect(345,320,51,31))
		self.num_bombonas.setMaximum(15)
		self.num_bombonas.setStyleSheet("QSpinBox{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"border-radius: 5px;\n}")
		
		# Botones guardar /ver fotos  ==========================================================================================              
		self.pushButton_ver_fotos = QPushButton(self.frame_principal_rpr_vv)
		self.pushButton_ver_fotos.setGeometry(QRect(490, 255, 101, 31))
		self.pushButton_ver_fotos.setStyleSheet(
		"QPushButton{\n"
		"border:0px;\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: #ffffff;\n"
		"border-radius: 5px;\n"
		"}\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:#ffffff;\n"
		"font-size: 12px;\n"
		"}")        
		self.pushButton_ver_fotos.setObjectName("pushButton_ver_fotos")
		self.pushButton_ver_fotos.setText("Ver fotos")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_ver_fotos.setGraphicsEffect(self.shadow)

		self.frame_2 = QFrame(self.frame_principal_rpr_vv)
		self.frame_2.setGeometry(QRect(20, 20, 121, 410))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius: 45px\n"
		"}")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Vivienda")


		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_rpr_vv = QPushButton(self.frame_2)
		self.pushButton_aceptar_rpr_vv.setGeometry(QRect(-12, 70, 141, 31))
		self.pushButton_aceptar_rpr_vv.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_rpr_vv.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_rpr_vv.setText("Aceptar")
		self.pushButton_aceptar_rpr_vv.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_rpr_vv.setIconSize(QSize(15,15))

		# Boton cancelar ==========================================================================================             
		self.pushButton_cancelar_rpr_vv = QPushButton(self.frame_2)
		self.pushButton_cancelar_rpr_vv.setGeometry(QRect(-10, 110, 141, 31))
		self.pushButton_cancelar_rpr_vv.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_rpr_vv.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_rpr_vv.setText("Cancelar")
		self.pushButton_cancelar_rpr_vv.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_rpr_vv.setIconSize(QSize(15,15))
		

		# Ventana Reparacion vivienda
		self.frame_principal_visualizador = QFrame(self)
		self.frame_principal_visualizador.setGeometry(QRect(100,-200,770,410))
		self.frame_principal_visualizador.setStyleSheet("QFrame#frame_principal_visualizador{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"border: 5px solid #ffffff;\n"
		"}\n"
		"")
		self.frame_principal_visualizador.move(145,1000)
		self.frame_principal_visualizador.setObjectName("frame_principal_visualizador")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_visualizador.setGraphicsEffect(self.shadow)

		self.frame_3 = QFrame(self.frame_principal_visualizador)
		self.frame_3.setGeometry(QRect(20, 20, 121, 370))
		self.frame_3.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px;\n"
		"}")
		self.frame_3.setFrameShape(QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_3.setGraphicsEffect(self.shadow)

		self.label_28 = QLabel(self.frame_3)
		self.label_28.setGeometry(QRect(-10, 10, 141, 20))
		self.label_28.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"")
		self.label_28.setAlignment(Qt.AlignCenter)
		self.label_28.setObjectName("label_28")
		self.label_28.setText("Cargar Foto")

		# Parte del visualizador donde se mostrara la imagen ==========================================================================================             
		self.frame_visualizador = QFrame(self.frame_principal_visualizador)
		self.frame_visualizador.setGeometry(QRect(160, 20, 591, 371))
		self.frame_visualizador.setStyleSheet("QFrame{\n"
		"background-color:#E5E7EE;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.frame_visualizador.setFrameShape(QFrame.StyledPanel)
		self.frame_visualizador.setFrameShadow(QFrame.Raised)
		self.frame_visualizador.setObjectName("frame")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_visualizador.setGraphicsEffect(self.shadow)

		# Label de la miniatura de imagen ==========================================================================================            
		# Miniatura_1
		self.label_miniatura_1 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_1.setGeometry(QRect(20, 20, 171, 121))
		self.label_miniatura_1.setStyleSheet("QLabel{\n"
		"background-color: #12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_1.setText("Click para anexar")
		self.label_miniatura_1.setObjectName("label_miniatura_1")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_1.setGraphicsEffect(self.shadow)
		self.label_miniatura_1.setToolTip("Click para anexar foto")
		self.label_miniatura_1.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_1_nombre.setGeometry(QRect(180,140,170,16))
		self.label_miniatura_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_2
		self.label_miniatura_2 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_2.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2.setGeometry(QRect(210, 20, 171, 121))
		self.label_miniatura_2.setStyleSheet("QLabel{\n"
		"background-color: #12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_2.setText("Click para anexar")
		self.label_miniatura_2.setObjectName("label_miniatura_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_2.setGraphicsEffect(self.shadow)
		self.label_miniatura_2.setToolTip("Click para anexar foto")
		self.label_miniatura_2_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_2_nombre.setGeometry(QRect(370,140,170,16))
		self.label_miniatura_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_3
		self.label_miniatura_3 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_3.setGeometry(QRect(400, 20, 171, 121))
		self.label_miniatura_3.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_3.setText("Click para anexar")
		self.label_miniatura_3.setObjectName("label_miniatura_3")
		self.label_miniatura_3.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_3.setGraphicsEffect(self.shadow)
		self.label_miniatura_3.setToolTip("Click para anexar foto")     
		self.label_miniatura_3_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_3_nombre.setGeometry(QRect(560,140,171,16))
		self.label_miniatura_3_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_3_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")


		# Miniatura_4
		self.label_miniatura_4 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_4.setGeometry(QRect(20, 200, 171, 121))
		self.label_miniatura_4.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_4.setText("Click para anexar")
		self.label_miniatura_4.setObjectName("label_miniatura_4")
		self.label_miniatura_4.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_4.setGraphicsEffect(self.shadow)
		self.label_miniatura_4.setToolTip("Click para anexar foto")
		self.label_miniatura_4_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_4_nombre.setGeometry(QRect(180,320,171,16))
		self.label_miniatura_4_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_4_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		
		# Miniatura_5
		self.label_miniatura_5 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_5.setGeometry(QRect(210, 200, 171, 121))
		self.label_miniatura_5.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_5.setText("Click para anexar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_5.setGraphicsEffect(self.shadow)
		self.label_miniatura_5.setObjectName("label_miniatura_5")
		self.label_miniatura_5.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5.setToolTip("Click para anexar foto")

		self.label_miniatura_5_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_5.setObjectName("label_miniatura_5_nombre")
		self.label_miniatura_5_nombre.setGeometry(QRect(370,320,171,16))
		self.label_miniatura_5_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_6
		self.label_miniatura_6 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_6.setGeometry(QRect(400, 200, 171, 121))
		self.label_miniatura_6.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_6.setText("Click para anexar")
		self.label_miniatura_6.setObjectName("label_miniatura_6")
		self.label_miniatura_6.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_6.setGraphicsEffect(self.shadow)
		self.label_miniatura_6.setToolTip("Click para anexar foto")

		self.label_miniatura_6_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_6_nombre.setGeometry(QRect(560,320,171,16))
		self.label_miniatura_6_nombre.setAlignment(Qt.AlignCenter)

		self.label_miniatura_6_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Boton eliminar de miniatura_1  ==========================================================================================             
		self.pushButton_eliminar = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar.setGeometry(QRect(70, 150, 71, 21))
		self.pushButton_eliminar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar.setObjectName("pushButton_eliminar")
		self.pushButton_eliminar.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_2 ==========================================================================================             
		self.pushButton_eliminar_2 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_2.setGeometry(QRect(260, 150, 71, 21))
		self.pushButton_eliminar_2.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_2.setObjectName("pushButton_eliminar_2")
		self.pushButton_eliminar_2.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_2.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_3  ==========================================================================================             
		self.pushButton_eliminar_3 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_3.setGeometry(QRect(450, 150, 71, 21))
		self.pushButton_eliminar_3.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_3.setObjectName("pushButton_eliminar_3")
		self.pushButton_eliminar_3.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_3.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_4 ==========================================================================================             
		self.pushButton_eliminar_4 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_4.setGeometry(QRect(70, 330, 71, 21))
		self.pushButton_eliminar_4.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_4.setObjectName("pushButton_eliminar_4")
		self.pushButton_eliminar_4.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_4.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_5  ==========================================================================================             
		self.pushButton_eliminar_5 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_5.setGeometry(QRect(260, 330, 71, 21))
		self.pushButton_eliminar_5.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_5.setObjectName("pushButton_eliminar_5")
		self.pushButton_eliminar_5.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_5.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_6  ==========================================================================================             
		self.pushButton_eliminar_6 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_6.setGeometry(QRect(450, 330, 71, 21))
		self.pushButton_eliminar_6.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_6.setObjectName("pushButton_eliminar_6")
		self.pushButton_eliminar_6.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_6.setGraphicsEffect(self.shadow)

		# Boton aceptar  ==========================================================================================              
		self.pushButton_visualizador_aceptar = QPushButton(self.frame_3)
		self.pushButton_visualizador_aceptar.setGeometry(QRect(-2, 70, 121, 31))
		self.pushButton_visualizador_aceptar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_visualizador_aceptar.setText("Guardar")
		self.pushButton_visualizador_aceptar.setIcon(QIcon(":/Icono_guardar/Imagenes-iconos/Guardar_blanco.png"))
		self.pushButton_visualizador_aceptar.setIconSize(QSize(18,18))

		# Boton cancelar  ==========================================================================================             
		self.pushButton_visualizador_cancelar = QPushButton(self.frame_3)
		self.pushButton_visualizador_cancelar.setGeometry(QRect(0, 100, 121, 31))
		self.pushButton_visualizador_cancelar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_visualizador_cancelar.setText("Cancelar")
		self.pushButton_visualizador_cancelar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_visualizador_cancelar.setIconSize(QSize(15,15))

		# Buttons para ver imagenes==========================================================================================             
		# Ver foto 1
		self.pushButton_ver_foto1 = QPushButton(self.frame_3)
		self.pushButton_ver_foto1.setGeometry(QRect(0, 150, 121, 31))
		self.pushButton_ver_foto1.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto1.setObjectName("pushButton_ver_foto1")
		self.pushButton_ver_foto1.setText("Ver foto 1")
		self.pushButton_ver_foto1.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto1.setIconSize(QSize(17,17))

		# Ver foto 2
		self.pushButton_ver_foto2 = QPushButton(self.frame_3)
		self.pushButton_ver_foto2.setGeometry(QRect(0, 181, 121, 31))
		self.pushButton_ver_foto2.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto2.setObjectName("pushButton_ver_foto2")
		self.pushButton_ver_foto2.setText("Ver foto 2")
		self.pushButton_ver_foto2.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto2.setIconSize(QSize(17,17))         

		# Ver foto 3
		self.pushButton_ver_foto3 = QPushButton(self.frame_3)
		self.pushButton_ver_foto3.setGeometry(QRect(0, 211, 121, 31))
		self.pushButton_ver_foto3.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto3.setObjectName("pushButton_ver_foto3")
		self.pushButton_ver_foto3.setText("Ver foto 3")
		self.pushButton_ver_foto3.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto3.setIconSize(QSize(17,17))

		# Ver foto 4
		self.pushButton_ver_foto4 = QPushButton(self.frame_3)
		self.pushButton_ver_foto4.setGeometry(QRect(0, 241, 121, 31))
		self.pushButton_ver_foto4.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto4.setObjectName("pushButton_ver_foto4")
		self.pushButton_ver_foto4.setText("Ver foto 4")
		self.pushButton_ver_foto4.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto4.setIconSize(QSize(17,17))

		# Ver foto 5
		self.pushButton_ver_foto5 = QPushButton(self.frame_3)
		self.pushButton_ver_foto5.setGeometry(QRect(0, 271, 121, 31))
		self.pushButton_ver_foto5.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto5.setObjectName("pushButton_ver_foto5")
		self.pushButton_ver_foto5.setText("Ver foto 5")
		self.pushButton_ver_foto5.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto5.setIconSize(QSize(17,17))

		# Ver foto 6
		self.pushButton_ver_foto6 = QPushButton(self.frame_3)
		self.pushButton_ver_foto6.setGeometry(QRect(0, 301, 121, 31))
		self.pushButton_ver_foto6.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_ver_foto6.setObjectName("pushButton_ver_foto6")
		self.pushButton_ver_foto6.setText("Ver foto 6")
		self.pushButton_ver_foto6.setIcon(QIcon(":/Icono_buscar/Imagenes-iconos/Buscar.png"))
		self.pushButton_ver_foto6.setIconSize(QSize(17,17))
		
		# Frame contenedor de foto 
		self.frame_contenedor_foto = QFrame(self)   
		self.frame_contenedor_foto.setGeometry(280,30,501,430)
		self.frame_contenedor_foto.setStyleSheet("QFrame{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius:30px"
		"}\n"
		"\n"
		"")
		self.frame_contenedor_foto.move(280,1000)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_contenedor_foto.setGraphicsEffect(self.shadow)

		# Mostrador de fotos
		self.label_mostrar_foto = QLabel(self.frame_contenedor_foto)
		self.label_mostrar_foto.setGeometry(QRect(10,10,481, 410))
		self.label_mostrar_foto.setStyleSheet("QLabel{\n"
		"background-color:#E5E7EE;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.label_mostrar_foto.setAlignment(Qt.AlignCenter)

		self.pushButton_cerrar = QPushButton(self.frame_contenedor_foto)
		self.pushButton_cerrar.setGeometry(QRect(467,210,20,20))
		self.pushButton_cerrar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_negro.png"))
		self.pushButton_cerrar.setIconSize(QSize(16,16))
		self.pushButton_cerrar.setStyleSheet("QPushButton{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
									"border-radIus: 3px\n"
									"}\n"
									"QPushButton:hover{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 204, 204, 129));\n"
									"border-radius:10px;\n"
									"}")

		self.pushButton_cerrar.clicked.connect(self.Bajar_foto_label)

		# Eventos==========================================================================================             
		self.label_miniatura_1.clicked.connect(self.Cargar)
		self.label_miniatura_2.clicked.connect(self.Cargar_1)
		self.label_miniatura_3.clicked.connect(self.Cargar_2)
		self.label_miniatura_4.clicked.connect(self.Cargar_3)
		self.label_miniatura_5.clicked.connect(self.Cargar_4)
		self.label_miniatura_6.clicked.connect(self.Cargar_5)

		self.pushButton_eliminar.clicked.connect(self.Eliminar)
		self.pushButton_eliminar_2.clicked.connect(self.Eliminar_1)
		self.pushButton_eliminar_3.clicked.connect(self.Eliminar_2)
		self.pushButton_eliminar_4.clicked.connect(self.Eliminar_3)
		self.pushButton_eliminar_5.clicked.connect(self.Eliminar_4)
		self.pushButton_eliminar_6.clicked.connect(self.Eliminar_5)


		self.frame_principal_estudiante = QFrame(self)
		self.frame_principal_estudiante.setGeometry(QRect(200,100,613,303))
		self.frame_principal_estudiante.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477,\n"
		"stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius:30px}")
		self.frame_principal_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_estudiante.move(200,1000)

		# Menu ========================================================================================================            
		self.frame_menu_estudiante = QFrame(self.frame_principal_estudiante)
		self.frame_menu_estudiante.setGeometry(QRect(20,20,121,261))
		self.frame_menu_estudiante.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius: 45px;\n"
		"}")
		self.frame_menu_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)

		self.label_estudiante = QLabel(self.frame_menu_estudiante)
		self.label_estudiante.setGeometry(QRect(20,10,81,20))
		self.label_estudiante.setText("Estudiante")
		self.label_estudiante.setStyleSheet("QLabel{\n"
		"color:rgb(255, 255, 255);\n"
		"font: 11pt Comic Sans MS;\n"
		"border-radius: 6px;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
		"}")

		self.label_estudiante.setAlignment(Qt.AlignHCenter)
		
		# Buttons de menu
		self.Button_aceptar_estudiante = QPushButton(self.frame_menu_estudiante)
		self.Button_aceptar_estudiante.setGeometry(QRect(0,80,121,31))
		self.Button_aceptar_estudiante.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px\n"
		"}\n"

		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"}")
		self.Button_aceptar_estudiante.setText("Aceptar")
		self.Button_aceptar_estudiante.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.Button_aceptar_estudiante.setIconSize(QSize(15,15))

		self.Button_cancelar_estudiante = QPushButton(self.frame_menu_estudiante)
		self.Button_cancelar_estudiante.setGeometry(QRect(2,110,121,31))
		self.Button_cancelar_estudiante.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px\n"
		"}\n"

		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"}")
		self.Button_cancelar_estudiante.setText("Cancelar")
		self.Button_cancelar_estudiante.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancelar_estudiante.setIconSize(QSize(15,15))


		self.frame_contenido_estudiante = QFrame(self.frame_principal_estudiante)
		self.frame_contenido_estudiante.setGeometry(QRect(170,20,421,261))
		self.frame_contenido_estudiante.setStyleSheet("color:#1b231f;\n"
		"background-color: #E5E7EE;\n"
		"font: 75 10pt Comic Sans MS;\n"
		"border-radius: 22px;")
		self.frame_contenido_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		# Nivel de instruccion ========================================================================================================            

		# label nivel de estudio:
		self.label_nivel_de_estudio = QLabel(self.frame_contenido_estudiante)
		self.label_nivel_de_estudio.setGeometry(QRect(70,10,125,16))
		self.label_nivel_de_estudio.setText("Nivel de estudio:")
		self.label_nivel_de_estudio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_nivel_de_estudio.setAlignment(Qt.AlignHCenter)

		# CheckBox de niveles de estudio primaria
		self.checkbox_primaria = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_primaria.setGeometry(QRect(20,30,121,21))
		self.checkbox_primaria.setText("Primaria")

		# CheckBox de niveles de estudio bachillerato
		self.checkbox_bachillerato = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_bachillerato.setGeometry(QRect(20,50,121,21))
		self.checkbox_bachillerato.setText("Bachillerato")

		# CheckBox de niveles de estudio tecnico superior
		self.checkbox_tcn_superior = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_tcn_superior.setGeometry(QRect(20,70,221,21))
		self.checkbox_tcn_superior.setText("Técnico superior universitario")

		# CheckBox de niveles de estudio universitario
		self.checkbox_universitario = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_universitario.setGeometry(QRect(20,90,111,21))
		self.checkbox_universitario.setText("Universitario")

		# CheckBox de niveles de estudio especializacion
		self.checkbox_especializacion = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_especializacion.setGeometry(QRect(20,110,131,21))
		self.checkbox_especializacion.setText("Especialización ")
		
		# Carrera que estudia ========================================================================================================             
		# Label de tipo de carrera
		self.label_carrera_que_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_carrera_que_estudia.setGeometry(QRect(255,10,145,16))
		self.label_carrera_que_estudia.setText("Carrera que estudia:")
		self.label_carrera_que_estudia.setAlignment(Qt.AlignHCenter)
		self.label_carrera_que_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")

		# QTextEdit de carrera que estudia
		self.texedit_carrera = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_carrera.setGeometry(QRect(250,30,161,81))
		self.texedit_carrera.setPlaceholderText("Carrera que cursa...")
		self.texedit_carrera.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")

		# Donde estudia ========================================================================================================               
		# Qlabel de donde estudia
		self.label_donde_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_donde_estudia.setGeometry(QRect(160,140,111,16))
		self.label_donde_estudia.setText("Donde estudia:")
		self.label_donde_estudia.setAlignment(Qt.AlignHCenter)
		self.label_donde_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")

		# QTextEdit de donde estudia
		self.texedit_donde_estudia = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_donde_estudia.setGeometry(QRect(40,160,341,81))
		self.texedit_donde_estudia.setPlaceholderText("Dirección y universidad donde estudia...")
		self.texedit_donde_estudia.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")

		self.label_imagen_1_1 = QLabel(self)
		self.label_imagen_1_1.setGeometry(QRect(150,1000,100,100))

		self.label_imagen_2_2 = QLabel(self)
		self.label_imagen_2_2.setGeometry(QRect(150,1000,100,100))

		self.label_imagen_3_3 = QLabel(self)
		self.label_imagen_3_3.setGeometry(QRect(150,1000,100,100))

		self.label_imagen_4_4 = QLabel(self)
		self.label_imagen_4_4.setGeometry(QRect(150,1000,100,100))

		self.label_imagen_5_5 = QLabel(self)
		self.label_imagen_5_5.setGeometry(QRect(150,1000,100,100))

			
		self.label_imagen_6_6 = QLabel(self)
		self.label_imagen_6_6.setGeometry(QRect(150,1000,100,100))

		# Eventos ========================================================================================================             
		self.Button_cancel_user.clicked.connect(self.cancelar_viz_user)
		
		self.Button_guardar_user.clicked.connect(self.Actualizar_datos)


		self.Button_discapacidad.clicked.connect(self.Mostrar_Discapacidad)
		self.pushButton_cancelar_discapacidad.clicked.connect(self.Cancelar_Discapacidad)
		self.pushButton_aceptar_discapacidad.clicked.connect(self.Aceptar_discapacidad)
		self.Button_discapacidad.clicked.connect(self.Bloquear_buttons)


		self.Button_enfermedad.clicked.connect(self.Mostrar_Enfermedad)
		self.pushButton_cancelar_Enfermedad.clicked.connect(self.Cancelar_enfermedad)
		self.pushButton_aceptar_Enfermedad.clicked.connect(self.Aceptar_enfermedad)
		self.Button_enfermedad.clicked.connect(self.Bloquear_buttons)


		self.Button_vivienda.clicked.connect(self.Mostrar_rpr_vv)
		self.pushButton_cancelar_rpr_vv.clicked.connect(self.Cancelar_rpr_vv)
		self.pushButton_aceptar_rpr_vv.clicked.connect(self.Aceptar_reparacion_vv)
		self.Button_vivienda.clicked.connect(self.Bloquear_buttons)


		self.pushButton_ver_fotos.clicked.connect(self.Mostrar_visualizador)
		self.pushButton_visualizador_cancelar.clicked.connect(self.Cancelar_visualizador)
		self.pushButton_visualizador_aceptar.clicked.connect(self.Aceptar_visualizador)
		self.pushButton_ver_fotos.clicked.connect(self.Bloquear_buttons)


		self.Button_educacion.clicked.connect(self.Mostrar_estudiante)
		self.Button_cancelar_estudiante.clicked.connect(self.Cancelar_estudiante)
		self.Button_aceptar_estudiante.clicked.connect(self.Aceptar_estudiante)
		self.Button_educacion.clicked.connect(self.Bloquear_buttons)


		self.pushButton_ver_foto1.clicked.connect(self.Mostrar_foto_label_1_1)
		self.pushButton_ver_foto1.clicked.connect(self.Subir_foto_label)

		self.pushButton_ver_foto2.clicked.connect(self.Mostrar_foto_label_1)
		self.pushButton_ver_foto2.clicked.connect(self.Subir_foto_label)    

		self.pushButton_ver_foto3.clicked.connect(self.Mostrar_foto_label_2)
		self.pushButton_ver_foto3.clicked.connect(self.Subir_foto_label)

		self.pushButton_ver_foto4.clicked.connect(self.Mostrar_foto_label_3)
		self.pushButton_ver_foto4.clicked.connect(self.Subir_foto_label)

		self.pushButton_ver_foto5.clicked.connect(self.Mostrar_foto_label_4)
		self.pushButton_ver_foto5.clicked.connect(self.Subir_foto_label)

		self.pushButton_ver_foto6.clicked.connect(self.Mostrar_foto_label_5)

	def Desbloquear_buttons(self):
		self.Button_discapacidad.setEnabled(True)
		self.Button_enfermedad.setEnabled(True)
		self.Button_vivienda.setEnabled(True)
		self.Button_educacion.setEnabled(True)

	def Bloquear_buttons(self):
		self.Button_discapacidad.setEnabled(False)
		self.Button_enfermedad.setEnabled(False)
		self.Button_vivienda.setEnabled(False)
		self.Button_educacion.setEnabled(False)

	# Eventos mostrar datos de la base de datos  ========================================================================================================              
	def Mostrar_Datos(self):
		# datos generales
		self.lineEdit_1_nombre.setText(str(self.datos[1]))

		self.lineEdit_2_nombre.setText(str(self.datos[2]))

		self.lineEdit_1_Apellido.setText(str(self.datos[3]))

		self.lineEdit_2_Apellido.setText(str(self.datos[4]))

		self.lineEdit_cedula.setText(str(self.datos[5]))

		self.comboBox_genero.setCurrentText(self.datos[6])

		self.lineEdit_1_tlf.setText(self.datos[7])

		self.lineEdit_2_tlf.setText(self.datos[8])

		self.dateEdit_nacimiento.setDate(QDate.fromString(self.datos[9], "dd/MM/yyyy"))

		self.lineEdit_edad.setText(self.datos[10])

		self.comboBox_profesion.setCurrentText(self.datos[11])

		self.comboBox_nvl_instruccion.setCurrentText(self.datos[12])

		self.comboBox_parentesco.setCurrentText(self.datos[13])

		self.comboBox_estadocivil.setCurrentText(self.datos[14])

		if self.datos[15] == "Si":
			self.radiobutton_si_inscrito.setChecked(True)
		elif self.datos[15] == "No":
			self.radiobutton_no_inscrito.setChecked(True)
		else:
			None

		self.lineEdit_correo.setText(self.datos[16])


		if self.datos[17] == "No esta pensionado":
			None
		else:   
			self.checkBox_1_pensionado.setChecked(True)


		if self.datos[45] == "No esta en estado de embarazo":
			None
		else:
			self.checkBox_4_Embarazada.setChecked(True)

		if self.datos[46] == "No esta en estado de lactancia":
			None
		else:
			self.checkBox_5_lactante.setChecked(True)

		# Ventana de discapacidad

		if self.datos[19] == "Discapacidad Motriz":
			self.checkBox_27_Dscp_motriz.setChecked(True)
		else:
			None
		if self.datos[20] == "Discapacidad Auditiva":
			self.checkBox_26_Dscp_auditiva.setChecked(True)
		else:
			None
		if self.datos[21] == "Discapacidad Visual":
			self.checkBox_25_Dscp_visual.setChecked(True)
		else:
			None
		if self.datos[22] == "Discapacidad Intelectual o Mental":
			self.checkBox_23_Dscp_mental.setChecked(True)
		else:
			None
		if self.datos[23] == "Discapacidad Visceral":
			self.checkBox_24_Dscp_viceral.setChecked(True)
		else:
			None
		if self.datos[24] == "Otras...":
			self.checkBox_otras.setChecked(True)
		else:
			None

		if self.datos[25] ==  "Necesita silla de rueda":
			self.checkBox_sillarueda.setChecked(True)
		else:
			None

		if self.datos[26] == "Necesita muletas":
			self.checkBox_muletas.setChecked(True)
		else:
			None
		if self.datos[27] == "Necesita protesis":
			self.checkBox_protesis.setChecked(True)
		else:
			None

		if self.datos[28] == "Otros...":
			self.checkBox_otros.setChecked(True)
		else:
			None

		self.textEdit_dcrp_discapacidad.setText(self.datos[29])

		if self.datos[30] == "Si":
			self.radioButton_si_medicamentos_dscp.setChecked(True)
		elif self.datos[30] == "No necesita medicamento":
			self.radioButton_no_medicamentos_dscp.setChecked(True)

		self.textEdit_medicamento_dscp.setText(self.datos[31])

		# Ventana de enfermedad

		if self.datos[32] == "Cáncer":
			self.checkBox_27_cancer.setChecked(True)
		else:
			None
			 
		if self.datos[33] == "Diabetes":
			self.checkBox_26_diabetes.setChecked(True)
		else:
			None

		if self.datos[34] == "Hipertensión arterial":
			self.checkBox_25_hp_arterial.setChecked(True)
		else:
			None

		if self.datos[35] == "Asma":
			self.checkBox_23_asma.setChecked(True)
		else:
			None

		if self.datos[36] == "Cardio Vascular":
			self.checkBox_24_vascular.setChecked(True)
		else:
			None

		if self.datos[37] ==  "Gastritis":
			self.checkBox_28_gastritis.setChecked(True)
		else:
			None

		if self.datos[38] ==  "Bronquitis":
			self.checkBox_29_bronquitis.setChecked(True)
		else:
			None

		if self.datos[39] == "Cálculos de riñón":
			self.checkBox_30_calcu_rinon.setChecked(True)
		else:
			None

		if self.datos[40] == "Sinusitis":
			self.checkBox_31_sinusitis.setChecked(True)
		else:
			None

		if self.datos[41] == "Otra...":
			self.checkBox_32_otra_enf.setChecked(True)
		else:
			None

		self.textEdit_dcrp_enfermedad.setText(self.datos[42])

		if self.datos[43] == "Si":
			self.radioButton_si_medicamentos_enfer.setChecked(True)
		else:
			self.radioButton_no_medicamentos_enfer.setChecked(True)

		self.textEdit_medicamento_enfer.setText(self.datos[44])

		if self.datos[0]:
			sql = "SELECT * FROM USUARIO_UBCGEOG WHERE ID LIKE ?", (self.datos[0],)
			print("Si")
		else:
			print("NO")

		if QFile.exists("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db"):
			conexion = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")
			cursor = conexion.cursor()
			try:
				cursor.execute(sql[0],sql[1])
				datosdevueltos = cursor.fetchall()
				for dato in datosdevueltos:
					self.estado = dato[1]
					self.municipio = dato[2]
					self.parroquia = dato[3]
					self.direccion = dato[4]

				conexion.close()
			except Exception as e:
				print("a:",e)

		self.lineEdit_estado.setText(self.estado)
		self.lineEdit_municipio.setText(self.municipio)
		self.lineEdit_parroquia.setText(self.parroquia)
		self.textEdit_direccion.setText(self.direccion)

		if self.datos[0]:
			sql = "SELECT * FROM USUARIO_DT_VV WHERE ID LIKE ?", (self.datos[0],)
			print("Si")
		else:
			print("NO")

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):
			conexion = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOS_VV.db")
			cursor = conexion.cursor()
			try:
				cursor.execute(sql[0],sql[1])
				datosdevueltos = cursor.fetchall()
				for dato in datosdevueltos:
					self.metrosdevivieda = dato[1]
					self.descripciondecasa = dato[2]
					self.reparacionvivienda = dato[3]
					self.reparaciondetechos = dato[4]
					self.reparaciondepared = dato[5]
					self.reparaciondepintura = dato[6]
					self.reparaciondepisos = dato[7]
					self.reparaciondeelectricidad = dato[8]
					self.reparaciondeaguas = dato[9]
					self.reparaciondeaguasservidas = dato[10]
					self.reparaciondeventanas= dato[11]
					self.reparaciondepuertas = dato[12]
					self.reparacionotras = dato[13]
					self.aguapotable= dato[14]
					self.aguaservida = dato[15]
					self.gasdirecto = dato[16]
					self.gasbombona = dato[17]
					self.tipodecilindro = dato[18]
					self.cantidaddebombona = dato[19]
					self.internet = dato[20]
					self.electricidad = dato[21]
					self.telefonofijo = dato[22]
					self.tiporeparaciondcrp = dato[23]
					self.necesitalineablanca = dato[24]
					self.foto1 = dato[25]
					self.foto2 = dato[26]
					self.foto3 = dato[27]
					self.foto4 = dato[28]
					self.foto5 = dato[29]
					self.foto6 = dato[30]
				conexion.close()
			except Exception as e:
				print("b: ",e)

		if self.foto1:
			imagen1 = QPixmap()
			imagen1.loadFromData(self.foto1, "PNG", Qt.AutoColor)
			self.label_imagen_1_1.setPixmap(imagen1)
			self.label_miniatura_1_nombre.setText("Foto_1 " +self.datos[1]+ " " +self.datos[3])
			
			if imagen1.width() > 171 or imagen1.height() > 121:
				imagen1 = imagen1.scaled(169, 119)
				self.label_miniatura_1.setPixmap(imagen1)
				self.Mostrar_foto_label_1_1(imagen1)
		else:
			self.label_miniatura_1.setText("No hay fotos")
			self.label_miniatura_1_nombre.setText("No hay fotos")

		if self.foto2:
			imagen2 = QPixmap()
			imagen2.loadFromData(self.foto2, "PNG", Qt.AutoColor)
			self.label_imagen_2_2.setPixmap(imagen2)

			self.label_miniatura_2_nombre.setText("Foto_2 " +self.datos[1]+ " " +self.datos[3])
			if imagen2.width() > 171 or imagen2.height() > 121:
				imagen2 = imagen2.scaled(169, 119)
				self.label_miniatura_2.setPixmap(imagen2)
				self.Mostrar_foto_label_1(imagen2)
		else:
			self.label_miniatura_2.setText("No hay fotos")
			self.label_miniatura_2_nombre.setText("No hay fotos")

		if self.foto3:
			imagen3 = QPixmap()
			imagen3.loadFromData(self.foto3, "PNG", Qt.AutoColor)
			self.label_miniatura_3_nombre.setText("Foto_3 " +self.datos[1]+ " " +self.datos[3])
			self.label_imagen_3_3.setPixmap(imagen3)

			if imagen3.width() > 171 or imagen3.height() > 121:
				imagen3 = imagen3.scaled(169, 119)
				self.label_miniatura_3.setPixmap(imagen3)
				self.Mostrar_foto_label_2(imagen3)

		else:
			self.label_miniatura_3.setText("No hay fotos")
			self.label_miniatura_3_nombre.setText("No hay fotos")

		if self.foto4:
			imagen4 = QPixmap()
			imagen4.loadFromData(self.foto4, "PNG", Qt.AutoColor)
			self.label_miniatura_4_nombre.setText("Foto_4 " +self.datos[1]+ " " +self.datos[3])
			self.label_imagen_4_4.setPixmap(imagen4)

			if imagen4.width() > 171 or imagen4.height() > 121:
				imagen4 = imagen4.scaled(169, 119)
				self.label_miniatura_4.setPixmap(imagen4)
				self.Mostrar_foto_label_3(imagen4)

		else:
			self.label_miniatura_4.setText("No hay fotos")
			self.label_miniatura_4_nombre.setText("No hay fotos")

		if self.foto5:
			imagen5 = QPixmap()
			imagen5.loadFromData(self.foto5, "PNG", Qt.AutoColor)
			self.label_miniatura_5_nombre.setText("Foto_5 " +self.datos[1]+ " " +self.datos[3])
			self.label_imagen_5_5.setPixmap(imagen5)
			self.Mostrar_foto_label_4(imagen5)

			if imagen5.width() > 171 or imagen5.height() > 121:
				imagen5 = imagen5.scaled(169, 119)
				self.label_miniatura_5.setPixmap(imagen5)
		else:
			self.label_miniatura_5.setText("No hay fotos")
			self.label_miniatura_5_nombre.setText("No hay fotos")

		if self.foto6:
			imagen6 = QPixmap()
			imagen6.loadFromData(self.foto6, "PNG", Qt.AutoColor)
			self.label_miniatura_6_nombre.setText("Foto_6 " +self.datos[1]+ " " +self.datos[3])
			self.label_imagen_6_6.setPixmap(imagen6)
			self.Mostrar_foto_label_5(imagen6)

			if imagen6.width() > 171 or imagen6.height() > 121:
				imagen6 = imagen6.scaled(169, 119)
				self.label_miniatura_6.setPixmap(imagen6)
		else:
			self.label_miniatura_6.setText("No hay fotos")
			self.label_miniatura_6_nombre.setText("No hay fotos")

		self.lineEdit_M2.setText(self.metrosdevivieda)

		self.textEdit_dcrp_vv.setText(self.descripciondecasa)

		if self.aguapotable == "Si":

			self.checkBox_aguapotable.setChecked(True)
		else:
			None

		if self.aguaservida == "Si":
			self.checkBox_aguasservidas.setChecked(True)
		else:
			None

		if self.gasdirecto == "Si":
			self.checkBox_gasdirecto.setChecked(True)
		else:
			None

		if self.gasbombona == "Si":
			self.checkBox_gasbombona.setChecked(True)
		else:
			None

		if self.internet == "Si":
			self.checkBox_internet.setChecked(True)
		else:
			None

		if self.electricidad == "Si":
			self.checkBox_electricidad.setChecked(True)
		else:
			None
		if self.telefonofijo == "Si":
			self.checkBox_tlf_fijo.setChecked(True)
		else:
			None

		# Tipo de reparaciones 
		if self.reparaciondetechos == "Arreglo o falta de techos":
			self.checkBox_arreglo_techos.setChecked(True)
		else:
			None
		if self.reparaciondepared == "Friso de pared":
			self.checkBox_2_friso.setChecked(True)
		else:
			None
		if self.reparaciondepintura == " Falta de pintura":
			self.checkBox_3_pintura.setChecked(True)
		else:
			None
		if self.reparaciondepisos == "Arreglo de pisos":
			self.checkBox_4_arreglo_Pisos.setChecked(True)
		else:
			None
		if self.reparaciondeelectricidad == "Sistema eléctrico":
			self.checkBox_5_sistema_electrico.setChecked(True)
		else:
			None
		if self.reparaciondeaguas ==  "Sistema de agua":
			self.checkBox_6_sistema_agua.setChecked(True)
		else:
			None
		if self.reparaciondeaguasservidas == "Sistema de aguas servida":
			self.checkBox_7_aguas_servidas.setChecked(True)
		else:
			None
		if self.reparaciondeventanas == "Falta de Ventanas":
			self.checkBox_8_fatla_ventanas.setChecked(True)
		else:
			None
		if self.reparaciondepuertas == "Falta de puertas":
			self.checkBox_9_falta_puertas.setChecked(True)
		else:
			None
		if self.reparacionotras == "Otras...":
			self.checkBox_10_otras_rpr.setChecked(True)
		else:
			None

		if self.tipodecilindro == "PDVSA Gas":
			self.checkBox_27_pdvsa_gas.setChecked(True)
		elif self.tipodecilindro == "Tropiven":
			self.checkBox_26_tropiven.setChecked(True)
		elif self.tipodecilindro == "Dani el gas": 
			self.checkBox_25_dani_gas.setChecked(True)
		elif self.tipodecilindro == "Hermagas":
			self.checkBox_23_hermagas.setChecked(True)
		elif self.tipodecilindro == "Autogas":
			self.checkBox_24_autogas.setChecked(True)
		else:
			None

		self.num_bombonas.setValue(self.cantidaddebombona)

		if self.necesitalineablanca == "Lavadora":
			self.checkBox_Lavadora.setChecked(True)
		elif self.necesitalineablanca == "Nevera":
			self.checkBox_Nevera.setChecked(True)
		elif self.necesitalineablanca == "Cocina":
		 self.checkBox_Cocina.setChecked(True)
		elif self.necesitalineablanca == "Aire Acondicionado":
			self.checkBox_Aireacondicionado.setChecked(True)
		else:
			None

		self.textEdit_dcrp_reparacionvv.setText(self.tiporeparaciondcrp)

		# Ventana de estudiante
		if self.datos[47] == "Primaria":
			self.checkbox_primaria.setChecked(True)
		elif self.datos[47] == "Bachillerato":
			self.checkbox_bachillerato.setChecked(True)
		elif self.datos[47] == "Universitario":
			self.checkbox_universitario.setChecked(True)
		elif self.datos[47] == "Técnico Superior universitario ":
			self.checkbox_tcn_superior.setChecked(True)
		elif self.datos[47] == "Especialización":
			self.checkbox_especializacion.setChecked(True)
		else:
			None

		self.texedit_carrera.setText(self.datos[48])
		self.texedit_donde_estudia.setText(self.datos[49])
		self.lineEdit_N_vivienda.setText(self.datos[53])

		if self.datos[0]:
			sql = "SELECT * FROM USUARIO_PROT_SOCIAL WHERE ID LIKE ?", (self.datos[0],)
			print("Si")
		else:
			print("NO")

		if QFile.exists("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db"):
			conexion = sqlite3.connect("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db")
			cursor = conexion.cursor()
			try:
				cursor.execute(sql[0],sql[1])
				datosdevueltos = cursor.fetchall()
				for dato in datosdevueltos:
					self._hogaresdelapatria = dato[1]
					self._amormayor = dato[2]
					self._josegregorio = dato[3]
					self._partohumanizado = dato[4]
					self._chambajuvenil = dato[5]
					self._somosvenezuela = dato[6]
					self._frentemiranda = dato[7]
					self._jpsuv = dato[8]
				conexion.close()
			except Exception as e:
				print("c: ",e)

		if self._hogaresdelapatria == "Si":
			self.checkBox_hogarespatria.setChecked(True)
		else:
			None
		if self._amormayor == "Si":
			self.checkBox_amormayor.setChecked(True)
		else:
			None
		if self._josegregorio == "Si":
			self.checkBox_joseGregorio.setChecked(True)
		else:
			None
		if self._partohumanizado == "Si":
			self.checkBox_partohumanizado.setChecked(True)
		else:
			None
		if self._chambajuvenil == "Si":
			self.checkBox_chambajuvenil.setChecked(True)
		else:
			None
		if self._somosvenezuela == "Si":
			self.checkBox_somosvenezuela.setChecked(True)
		else:
			None
		if self._frentemiranda == "Si":
			self.checkBox_FrenteMiranda.setChecked(True)
		else:
			None
		if self._jpsuv == "Si":
			self.checkBox_jpsuv.setChecked(True)
		else:
			None

	def Actualizar_datos(self):
		# Datos Generales
		nombre_1 = self.lineEdit_1_nombre.text() 
		nombre_2 = self.lineEdit_2_nombre.text()
		apellido_1 = self.lineEdit_1_Apellido.text()
		apellido_2 = self.lineEdit_2_Apellido.text()
		cedula_identidad = self.lineEdit_cedula.text()
		telefono_princ = self.lineEdit_1_tlf.text()
		telefono_secund = self.lineEdit_2_tlf.text()
		genero = self.comboBox_genero.currentText()
		edad = self.lineEdit_edad.text()
		fecha_Nacimiento = self.dateEdit_nacimiento.text()
		profesion_oficio = self.comboBox_profesion.currentText()
		nivel_instruccion = self.comboBox_nvl_instruccion.currentText()
		parentesco = self.comboBox_parentesco.currentText()
		opcion_pensionado = self.pensionado()
		opcion_embarazada = self.opcion_de_embarazada()
		opcion_lactante = self.opcion_de_lactante()
		estado_civil = self.comboBox_estadocivil.currentText()
		inscrito_rep = self.RadioButton_rep()
		correo_electronico = self.lineEdit_correo.text()

		# Ubicacion geografica          
		estado = self.lineEdit_estado.text()
		municipio = self.lineEdit_municipio.text()
		parroquia = self.lineEdit_parroquia.text()
		numero_vivienda = self.lineEdit_N_vivienda.text()
		direccion = self.textEdit_direccion.toPlainText()

		# Datos de la vivienda
		metros_cuadrados = self.lineEdit_M2.text()
		descripcion_vivienda = self.textEdit_dcrp_vv.toPlainText()

		# reparaciones = self.RadioButton_reparacion()
		servicio_aguapotable = self.CheckBox_aguapotable()
		servicio_aguaservidas = self.CheckBox_aguaservidas()
		servicio_gasdirecto = self.CheckBox_gasdirecto()
		servicio_gasbombona = self.gas_bombona_servicio()
		servicio_internet = self.CheckBox_internet()
		servicio_electricidad = self.CheckBox_electricidad()
		servicio_tlf_fijo = self.CheckBox_telefonofijo()

		# Proteccion Social
		hogaresdelapatria = self.CheckBox_hogaresdelapatria()
		amormayor = self.CheckBox_amormayor()
		josegregorio = self.CheckBox_josegregorio()
		partohumanizado = self.CheckBox_partohumanizado()

		chambajuvenil = self.CheckBox_chambajuvenil()
		somosvenezuela = self.CheckBox_somosvenezuela()
		frentemiranda = self.CheckBox_frentemiranda()
		jpsuv = self.CheckBox_jpsuv()

		# Ventana de discapacidad
		descripcion_discapacidad = self.textEdit_dcrp_discapacidad.toPlainText()
		discapacidad_motriz = self.Discapacidad_Motriz()
		discapacidad_auditiva = self.Discapacidad_Auditiva()
		discapacidad_visual = self.Discapacidad_Visual()
		discapacidad_intelectual = self.Discapacidad_Intelectual_Mental()
		discapacidad_viceral = self.Discapacidad_Visceral()
		discapacidad_otras = self.Discapacidad_Otras()

		insumomedico_silla_de_reudas = self.Necesita_silla_de_rueda()
		insumomedico_muletas = self.Necesita_muletas()
		insumomedico_protesis = self.Necesita_protesis()
		insumomedico_otros = self.Necesita_Otros()
		descripcion_medicamento_dscp= self.textEdit_medicamento_dscp.toPlainText()
		necesita_algun_medicamento_dscp = self.necesita_algun_medicamento_dscp()

		# Ventana de enfermedad
		enfermedad_de_cancer = self.Tipo_Enfer_Cancer()
		enfermedad_de_diabetes = self.Tipo_Enfer_Diabetes()
		enfermedad_de_hipertension = self.Tipo_Enfer_Hipertension_arterial()
		enfermedad_de_asma = self.Tipo_Enfer_Asma()
		enfermedad_de_cardio = self.Tipo_Enfer_Cardio_Vascula()
		enfermedad_de_gastritis = self.Tipo_Enfer_Gastritis()
		enfermedad_de_bronquitis = self.Tipo_Enfer_Bronquitis()
		enfermedad_de_calculos = self.Tipo_Enfer_Calculos_rinon()
		enfermedad_de_sinusitis = self.Tipo_Enfer_Sinusitis()
		enfermedad_de_otras = self.Tipo_Enfer_Otras()

		descripcion_enfermedad=  self.textEdit_dcrp_enfermedad.toPlainText()
		necesita_algun_medicamento_enfer = self.necesita_medicamento_enfer()
		descripcion_medicamento_enfer = self.textEdit_medicamento_enfer.toPlainText()

		# Ventana de reparacion de vivienda:
		Descripcion_de_reparacion = self.textEdit_dcrp_reparacionvv.toPlainText()
		reparacion_de_techos = self.Reparacion_de_Techos()
		reparacion_de_pared = self.Reparacion_de_Pared()
		reparacion_de_pintura = self.Reparacion_de_Pintura()
		reparacion_de_pisos = self.Reparacion_de_Pisos()
		reparacion_de_electrico = self.Reparacion_de_Electrico()
		reparacion_de_agua = self.Reparacion_de_Agua()
		reparacion_de_agua_servidas = self.Reparacion_de_Agua_servidas()
		reparacion_de_ventanas = self.Reparacion_de_Ventanas()
		reparacion_de_puertas = self.Reparacion_de_Puertas()
		reparacion_de_otras = self.Reparacion_de_otras()
		Linea_blanca = self.Linea_blanca()

		# Ventana bombona 
		tipo_de_cilindro = self.Tipo_de_cilindro()
		cantidad_de_bombonas = int(self.num_bombonas.value())

		# Ventana estudiante
		nivel_estudio = self.nivel_estudio()
		carrera_cursando = self.texedit_carrera.toPlainText()
		donde_estudia = self.texedit_donde_estudia.toPlainText()

		# Venta de visualizador de fotos 
		foto_1 = self.label_imagen_1_1.pixmap()
		foto_2 = self.label_imagen_2_2.pixmap()
		foto_3 = self.label_imagen_3_3.pixmap()
		foto_4 = self.label_imagen_4_4.pixmap()
		foto_5 = self.label_imagen_5_5.pixmap()
		foto_6 = self.label_imagen_6_6.pixmap()

		if foto_1:
			bArray_1 = QByteArray()
			bufer = QBuffer(bArray_1)
			bufer.open(QIODevice.WriteOnly)
			bufer.close()
			foto_1.save(bufer,"PNG")
		else:
			bArray_1 = ""

		if foto_2:
				bArray_2 = QByteArray()
				bufer = QBuffer(bArray_2)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_2.save(bufer,"PNG")
		else:
				bArray_2 = ""

		if foto_3:
				bArray_3 = QByteArray()
				bufer = QBuffer(bArray_3)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_3.save(bufer,"PNG")
		else:
				bArray_3 = ""

		if foto_4:
				bArray_4 = QByteArray()
				bufer = QBuffer(bArray_4)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_4.save(bufer,"PNG")
		else:
				bArray_4 = ""

		if foto_5:
				bArray_5 = QByteArray()
				bufer = QBuffer(bArray_5)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_5.save(bufer,"PNG")
		else:
				bArray_5 = ""

		if foto_6:
				bArray_6 = QByteArray()
				bufer = QBuffer(bArray_6)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_6.save(bufer,"PNG")
		else:
				bArray_6 = ""

		if not nombre_1:
			self.lineEdit_1_nombre.setFocus()
		elif not apellido_1:
			self.lineEdit_1_Apellido.setFocus()
		elif not cedula_identidad:
			self.lineEdit_cedula.setFocus()
		elif not telefono_princ:
			self.lineEdit_1_tlf.setFocus()
		elif not genero:
			self.comboBox_genero.setFocus()
		elif not numero_vivienda:
			self.lineEdit_N_vivienda.setFocus()
		elif not direccion:
			self.textEdit_direccion.setFocus()  
		elif not edad:
			self.lineEdit_edad.setFocus()
		elif not parentesco:
			self.comboBox_parentesco.setFocus()
		elif not estado_civil:
			self.comboBox_estadocivil.setFocus()
		else:       
			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db')
				cursor = conexion.cursor()
				try:
					fecha_actual = time.strftime("%d/%m/%y")

					datos_insertar_Gnr = [nombre_1, nombre_2, apellido_1, apellido_2,
									cedula_identidad, genero, telefono_princ, telefono_secund,
									fecha_Nacimiento, edad, profesion_oficio, nivel_instruccion,
									parentesco, estado_civil, inscrito_rep, correo_electronico,
									opcion_pensionado,discapacidad_motriz, discapacidad_auditiva, discapacidad_visual,
									discapacidad_intelectual, discapacidad_viceral, discapacidad_otras,
									descripcion_discapacidad,necesita_algun_medicamento_dscp,
									descripcion_medicamento_dscp, insumomedico_silla_de_reudas,
									insumomedico_muletas, insumomedico_protesis,insumomedico_otros,
									enfermedad_de_cancer,enfermedad_de_diabetes, enfermedad_de_hipertension, enfermedad_de_asma,
									enfermedad_de_cardio, enfermedad_de_gastritis, enfermedad_de_bronquitis, enfermedad_de_calculos,
									enfermedad_de_sinusitis, enfermedad_de_otras,descripcion_enfermedad,
									necesita_algun_medicamento_enfer,descripcion_medicamento_enfer, opcion_embarazada,opcion_lactante,
									nivel_estudio,carrera_cursando,donde_estudia, fecha_actual, numero_vivienda,self.datos[0]]

					cursor.execute("UPDATE USUARIO_DT_GNR SET PRIMER_NOMBRE = ?,"
																			"SEGUNDO_NOMBRE = ?, PRIMER_APELLIDO = ?, SEGUNDO_APELLIDO = ?,"

																			"CEDULA = ? , GENERO = ? , TELEFONO_PRINCIPAL = ? ," 

																			"TELEFONO_SECUNDARIO = ?, FECHA_NACIMIENTO = ?, EDAD = ?,"

																			"PROFESION_OFICIO = ?, NIVEL_INSTRUCCION = ?, PARENTESCO = ?,"

																			"ESTADO_CIVIL = ?, INSCRITO_REP = ?, CORREO_ELECTRONICO = ?,"

																			"PENSIONADO = ?,DISCAPACIDAD_MOTRIZ = ?, DISCAPACIDAD_AUDITIVA = ?,"
																			
																			"DISCAPACIDAD_VISUAL = ?, DISCAPACIDAD_INTELECTUAL = ?, DISCAPACIDAD_VISCERAL = ?,"
																			
																			"DISCAPACIDAD_OTRAS = ?, DESCRIBA_DISCAPACIDAD = ?,"

																			"TOMA_MEDICAMENTO = ?,DESCRIBA_MEDICAMENTO = ?, SILLA_DE_RUEDA = ?, MULETAS = ?, PROTESIS = ?, INSUMO_OTROS = ?,"
																			
																			"ENFERMEDAD_CANCER = ?, ENFERMEDAD_DIABETES = ?, ENFERMEDAD_HIPERTENSION = ?, ENFERMEDAD_ASMA = ?,"

																			"ENFERMEDAD_CARDIO = ?, ENFERMEDAD_GASTRITIS = ?, ENFERMEDAD_BRONQUITIS = ?, ENFERMEDAD_CALCULOS = ?,"

																			"ENFERMEDAD_SINUSITIS = ?, ENFERMEDAD_OTRAS = ?,"

																			"DESCRIBA_ENFERMEDAD = ?,TOMA_MEDICAMENTO_ENF = ?, DESCRIBA_MEDICAMENTO_ENF = ?,"  

																			"EMBARAZADA = ?, LACTANTE = ?, NIVEL_DE_ESTUDIO = ?,CARRERA_CURSANDO = ?,DONDE_ESTUDIA = ?, MODIFICACION = ?, N_VIVIENDA = ? WHERE ID = ?", datos_insertar_Gnr)

					idusuario = cursor.lastrowid

					conexion.commit()        
					cursor.close()
					conexion.close()
					if QFile.exists("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db"):
						conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db')
						cursor = conexion.cursor()
			
						datos_insertar_Ubc = [estado, municipio,parroquia,direccion,self.datos[0]]

						cursor.execute("UPDATE USUARIO_UBCGEOG SET ESTADO = ?, MUNICIPIO = ?,"
										"PARROQUIA = ?, DIRECCION = ? WHERE ID = ?", datos_insertar_Ubc)
						conexion.commit()       
						cursor.close()
						conexion.close()

						if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):
							conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db')
							cursor = conexion.cursor()
				
							datos_insertar_Vv = [metros_cuadrados, descripcion_vivienda,Descripcion_de_reparacion,
												reparacion_de_techos,reparacion_de_pared,reparacion_de_pintura, reparacion_de_pisos,
												reparacion_de_electrico,reparacion_de_agua, reparacion_de_agua_servidas, reparacion_de_ventanas,
												reparacion_de_puertas, reparacion_de_otras,
												Linea_blanca, servicio_aguapotable, servicio_aguaservidas, 
												servicio_gasdirecto, servicio_gasbombona, tipo_de_cilindro,cantidad_de_bombonas,
												servicio_internet,servicio_electricidad,
												servicio_tlf_fijo,bArray_1, bArray_2, bArray_3, bArray_4, bArray_5, bArray_6,self.datos[0]]
							
							cursor.execute("UPDATE USUARIO_DT_VV SET METROS_CUADRADOS = ?, DESCRIPCION = ?,DESCRIPCION_REPARACION = ?,"
												"REPARACION_TECHOS = ?, REPARACION_PARED = ?, REPARACION_PINTURA = ?, REPARACION_PISOS = ?, REPARACION_ELECTRICO = ?,"
												"REPARACION_AGUA = ?, REPARACION_AGUA_SERVIDAS = ?, REPARACION_VENTANAS = ?, REPARACION_PUERTARS = ?,"
												"REPARACION_OTRAS = ?,"
												"NECESITA_LINEBLANCA = ?, AGUA_POTABLE = ?, AGUA_SERVIDAS = ?,"
												"GAS_DIRECTO = ?, GAS_BOMBONA = ?,"
												"TIPO_DE_CILINDRO = ? , CANTIDAD_DE_BOMBONAS = ?,"
												"INTERNET = ?, ElECTRICIDAD = ?,"
												"TELEFONO_FIJO = ?,"
												"FOTO_ANEXADA1 = ?, FOTO_ANEXADA2 = ?, FOTO_ANEXADA3 = ?, FOTO_ANEXADA4 = ?, FOTO_ANEXADA5 = ?,FOTO_ANEXADA6 = ? WHERE ID = ?", datos_insertar_Vv)

							conexion.commit()       
							cursor.close()
							conexion.close()


							if QFile.exists("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db"):
								conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_PROT_SOCIAL.db')
								cursor = conexion.cursor()

						
								datos_insertar_Prot = [hogaresdelapatria, amormayor,josegregorio,partohumanizado,
														chambajuvenil, somosvenezuela,frentemiranda, jpsuv,self.datos[0]]

								cursor.execute("UPDATE USUARIO_PROT_SOCIAL SET HOGARES_PATRIA = ?, AMOR_MAYOR = ?,"
													"JOSE_GREGORIO = ?, PARTO_HUMANIZADO = ?, CHAMBA_JUVENIL = ?, SOMOS_VENEZUELA = ?,"
													"FRENTE_MIRANDA = ?, JPSUV = ? WHERE ID = ?", datos_insertar_Prot)
								conexion.commit()       
								cursor.close()
								conexion.close()

								QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",QMessageBox.Ok)

							else:
								QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)
						else:
							QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)
					else:

						QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)
				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
											QMessageBox.Ok)
			else:
				QMessageBox.information(self, "Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
												   QMessageBox.Ok)
		self.close()

		# Funciones ========================================================================================================               

	# funcion mostar imagen en label =======================================================================================
	def Mostrar_foto_label_1_1(self,imagen1):
		self.foto1
		if self.foto1:

			label_imagen1 = QPixmap()
			label_imagen1.loadFromData(self.foto1, "PNG", Qt.AutoColor)
			if label_imagen1.width() > 481 or label_imagen1.height() > 410:
				label_imagen1 = label_imagen1.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen1)
			else:
				pass
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)
			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None

	def Subir_foto_label(self):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_contenedor_foto,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_contenedor_foto))
		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(280,1000,501,430))
		self.animacionMostar.setEndValue(QRect(280,30,501,430))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Bajar_foto_label(self):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_contenedor_foto,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_contenedor_foto))
		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(280,30,501,430))
		self.animacionMostar.setEndValue(QRect(280,1000,501,430))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_foto_label_1(self, imagen2):
		self.foto2
		if self.foto2:
			label_imagen2 = QPixmap()
			label_imagen2.loadFromData(self.foto2, "PNG", Qt.AutoColor)
			if label_imagen2.width() > 481 or label_imagen2.height() > 410:
				label_imagen2 = label_imagen2.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen2)
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)

			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None

	def Mostrar_foto_label_2(self,imagen3):
		self.foto3
		if self.foto3:
			label_imagen3 = QPixmap()
			label_imagen3.loadFromData(self.foto3, "PNG", Qt.AutoColor)
			if label_imagen3.width() > 481 or label_imagen3.height() > 410:
				label_imagen3 = label_imagen3.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen3)
			else:
				pass
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)
			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None

	def Mostrar_foto_label_3(self,imagen4):
		self.foto4
		if self.foto4:
			label_imagen4 = QPixmap()
			label_imagen4.loadFromData(self.foto4, "PNG", Qt.AutoColor)
			if label_imagen4.width() > 481 or label_imagen4.height() > 410:
				label_imagen4 = label_imagen4.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen4)
			else:
				pass
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)
			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None

	def Mostrar_foto_label_4(self, imagen5):
		self.foto5
		if self.foto5:
			label_imagen5 = QPixmap()
			label_imagen5.loadFromData(self.foto5, "PNG", Qt.AutoColor)
			if label_imagen5.width() > 481 or label_imagen5.height() > 410:
				label_imagen5 = label_imagen5.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen5)
			else:
				pass
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)
			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None

	def Mostrar_foto_label_5(self,imagen6):
		self.foto6
		if self.foto6:
			label_imagen6 = QPixmap()
			label_imagen6.loadFromData(self.foto6, "PNG", Qt.AutoColor)
			if label_imagen6.width() > 481 or label_imagen6.height() > 410:
				label_imagen6 = label_imagen6.scaled(481, 410, Qt.KeepAspectRatio, Qt.SmoothTransformation)
				self.label_mostrar_foto.setPixmap(label_imagen6)
			else:
				pass
		else:
			msg = QMessageBox.information(self, "Buscar foto", "No se encuentra ninguna foto "
											, QMessageBox.Ok)
			if msg == QMessageBox.Ok:
				self.Bajar_foto_label()
			else:
				None
	
	# funcion de estudiante nivel de estudio =======================================================================================
	def nivel_estudio(self):
		if self.checkbox_primaria.isChecked():
			return "Primaria"
		elif self.checkbox_bachillerato.isChecked():
			return "Bachillerato"
		elif self.checkbox_universitario.isChecked():
			return "Universitario"
		elif self.checkbox_tcn_superior.isChecked():
			return "Técnico Superior universitario "
		elif self.checkbox_especializacion.isChecked():
			return "Especialización"
		else:
			return "Ningún"

	# funcion de estudiante =======================================================================================
	def Estudiante(self,i):
			if i == 15:
				self.Mostrar_estudiante()
			else:
				return "No esta estudiando"

	# opcion de lactante =======================================================================================	
	def opcion_de_lactante(self):
		if self.checkBox_5_lactante.isChecked():
			return "Si"
		else: 
			return "No está en estado de lactancia"
	# opcion de embarazada =======================================================================================
	def opcion_de_embarazada(self):
		if self.checkBox_4_Embarazada.isChecked():
			return "Si"

		else:
			return "No esta en estado de embarazo"

	# opcion de servicio gas bombona =======================================================================================
	def gas_bombona_servicio(self):
		if self.checkBox_gasbombona.isChecked():
			return "Si"
		else:
			return "No"

	# opcion pensionado  =======================================================================================c
	def pensionado(self):
		if self.checkBox_1_pensionado.isChecked():
			return "Pensionado"
		else:
			return "No esta pensionado"

	# Ventana reparacion de vivienda  =======================================================================================
	def Linea_blanca(self):
		if self.checkBox_Lavadora.isChecked():
			return "Lavadora"
		elif self.checkBox_Nevera.isChecked():
			return "Nevera"
		elif self.checkBox_Cocina.isChecked():
			return "Cocina"
		elif self.checkBox_Aireacondicionado.isChecked():
			return "Aire Acondicionado"
		else:
			return "No necesita linea blanca"

	# TIPOS DE REPARACION
	def Reparacion_de_Techos(self):
		if self.checkBox_arreglo_techos.isChecked():
			return "Arreglo o falta de techos"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pared(self):
		if self.checkBox_2_friso.isChecked():
			return "Friso de pared"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pintura(self):
		if self.checkBox_3_pintura.isChecked():
			return " Falta de pintura"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pisos(self):
		if self.checkBox_4_arreglo_Pisos.isChecked():
			return "Arreglo de pisos"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Electrico(self):
		if self.checkBox_5_sistema_electrico.isChecked():
			return "Sistema eléctrico"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Agua(self):
		if self.checkBox_6_sistema_agua.isChecked():
			return "Sistema de agua"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Agua_servidas(self):
		if self.checkBox_7_aguas_servidas.isChecked():
			return "Sistema de aguas servida"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Ventanas(self):
		if self.checkBox_8_fatla_ventanas.isChecked():
			return "Falta de Ventanas"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Puertas(self):
		if self.checkBox_9_falta_puertas.isChecked():
			return "Falta de puertas"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_otras(self):
		if self.checkBox_10_otras_rpr.isChecked():
			return "Otras..."
		else:
			"No necesita este arreglo"

	# Ventana de Enfermedad =======================================================================================
	def Tipo_Enfer_Cancer(self):    
		if self.checkBox_27_cancer.isChecked():
			return "Cáncer"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Diabetes(self):
		if self.checkBox_26_diabetes.isChecked():
			return "Diabetes"
		else:
			return "No posee esta enfermedad" 

	def Tipo_Enfer_Hipertension_arterial(self):
		if self.checkBox_25_hp_arterial.isChecked():
			return "Hipertensión arterial"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Asma(self):
		if self.checkBox_23_asma.isChecked():
			return "Asma"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Cardio_Vascula(self):
		if self.checkBox_24_vascular.isChecked():
			return "Cardio Vascular"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Gastritis(self):
		if self.checkBox_28_gastritis.isChecked():
			return "Gastritis"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Bronquitis(self):
		if self.checkBox_29_bronquitis.isChecked():
			return "Bronquitis"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Calculos_rinon(self):
		if self.checkBox_30_calcu_rinon.isChecked():
			return "Cálculos de riñón"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Sinusitis(self):
		if self.checkBox_31_sinusitis.isChecked():
			return "Sinusitis"
		else:
			return "No posee esta enfermedad"
			
	def Tipo_Enfer_Otras(self):
		if self.checkBox_32_otra_enf.isChecked():
			return "Otra..."
		else:
			"No posee esta enfermedad"

	def necesita_medicamento_enfer(self):
			if self.radioButton_si_medicamentos_enfer.isChecked():
				return "Si"
			elif self.radioButton_no_medicamentos_enfer.isChecked():
				return "No"
			else:
				return "No necesita medicamento"

	# Ventana de discapacidad =======================================================================================
	def Necesita_silla_de_rueda(self):
		if self.checkBox_sillarueda.isChecked():
			return "Necesita silla de rueda"
		else:
			return "No necesita este insumo medico"

	def Necesita_muletas(self):
		if self.checkBox_muletas.isChecked():
			return "Necesita muletas"
		else:
			return "No necesita este insumo medico"

	def Necesita_protesis(self):
		if self.checkBox_protesis.isChecked():
			return "Necesita protesis"
		else:
			return "No necesita este insumo medico"

	def Necesita_Otros(self):
		if self.checkBox_otros.isChecked():
			return "Otros..."
		else:
			return "No necesita este insumo medico"

	# Ojo con esta funcion (identado sospechozo)
	def necesita_algun_medicamento_dscp(self):
			if self.radioButton_si_medicamentos_dscp.isChecked():
				return "Si"
			elif self.radioButton_no_medicamentos_dscp.isChecked():
				return "No"
			else:
				return "No necesita medicamento"

	# Tipo de discapacidades        
	def Discapacidad_Motriz(self):
		if self.checkBox_27_Dscp_motriz.isChecked():
			return "Discapacidad Motriz"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Auditiva(self):
		if self.checkBox_26_Dscp_auditiva.isChecked():
			return "Discapacidad Auditiva"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Visual(self):
		if self.checkBox_25_Dscp_visual.isChecked():
			return "Discapacidad Visual"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Intelectual_Mental(self):
		if self.checkBox_23_Dscp_mental.isChecked():
			return "Discapacidad Intelectual o Mental"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Visceral(self):
		if self.checkBox_24_Dscp_viceral.isChecked():
				return "Discapacidad Visceral"
		else: 
			return " No posee esta discapacidad"

	def Discapacidad_Otras(self):
		if self.checkBox_otras.isChecked():
			return "Otras..."
		else:
			return "No posee esta discapacidad"

	# Funcion si esta inscrito en el REP o no =============================================================================================
	def RadioButton_rep(self):
		if self.radiobutton_si_inscrito.isChecked():
			return "Si"
		elif self.radiobutton_no_inscrito.isChecked():
			return "No esta inscrito"
		else:
			return "No"

	# CheckBox de servicios que posee ==================================================================================================
	def CheckBox_aguapotable(self):
		if self.checkBox_aguapotable.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_aguaservidas(self):
		if self.checkBox_aguasservidas.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_gasdirecto(self):
		if self.checkBox_gasdirecto.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_gasbombona(self):
		if self.checkBox_gasbombona.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_internet(self):
		if self.checkBox_internet.isChecked():
			return "Si"

		else:
			return "No"

	def CheckBox_electricidad(self):
		if self.checkBox_electricidad.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_telefonofijo(self):
		if self.checkBox_tlf_fijo.isChecked():
			return "Si"
		else:
			return "No"

	# Proteccion Social =======================================================================================
	def CheckBox_hogaresdelapatria(self):
		if self.checkBox_hogarespatria.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_amormayor(self):
		if self.checkBox_amormayor.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_josegregorio(self):
		if self.checkBox_joseGregorio.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_partohumanizado(self):
		if self.checkBox_partohumanizado.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_somosvenezuela(self):
		if self.checkBox_somosvenezuela.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_chambajuvenil(self):
		if self.checkBox_chambajuvenil.isChecked():
			return "Si"

		else:
			return "No"

	def CheckBox_frentemiranda(self):
		if self.checkBox_FrenteMiranda.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_jpsuv(self):
		if self.checkBox_jpsuv.isChecked():
			return "Si"
		else:
			return "No"

	def Tipo_de_cilindro(self):
		if self.checkBox_27_pdvsa_gas.isChecked():
			return "PDVSA Gas"
		elif self.checkBox_26_tropiven.isChecked():
			return "Tropiven"

		elif self.checkBox_25_dani_gas.isChecked():
			return "Dani el gas" 

		elif self.checkBox_23_hermagas.isChecked():
			return "Hermagas" 

		elif self.checkBox_24_autogas.isChecked():
			return "Autogas" 

		else:
			return "No"
 
	# Funciones para discapacidad
	def Aceptar_discapacidad(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Discapacidad()
			self.Desbloquear_buttons()
		else:
			pass

	def Cancelar_Discapacidad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Discapacidad()
			self.Desbloquear_buttons()
		else:
			pass

	def Mostrar_Discapacidad(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_discapacidad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_discapacidad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(210, 600, 590, 294))
		self.animacionMostar.setEndValue(QRect(210, 100, 590, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_Discapacidad(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_discapacidad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_discapacidad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(210, 100, 590, 294))
		self.animacionMostar.setEndValue(QRect(210, 600, 590, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	# Funciones para enfermedad
	def Aceptar_enfermedad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Enfermedad()
			self.Desbloquear_buttons()
		else:
			pass

	def Cancelar_enfermedad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Enfermedad()
			self.Desbloquear_buttons()
		else:
			pass    

	def Mostrar_Enfermedad(self):

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_Enfermedad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Enfermedad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(210, 600, 600, 294))
		self.animacionMostar.setEndValue(QRect(210, 100, 600, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_Enfermedad(self):

		self.animacionMostar = QPropertyAnimation(self.frame_principal_Enfermedad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Enfermedad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(210, 100, 600, 294))
		self.animacionMostar.setEndValue(QRect(210, 600, 600, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	# Funciones vivienda
	def Aceptar_reparacion_vv(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_rpr_vv()
			self.Desbloquear_buttons()
		else:
			pass

	def Cancelar_rpr_vv(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_rpr_vv()
			self.Desbloquear_buttons()
		else:
			pass

	def Mostrar_rpr_vv(self):

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_rpr_vv,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_rpr_vv))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(180, 600, 675,450))
		self.animacionMostar.setEndValue(QRect(180, 20, 675,450))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_rpr_vv(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_rpr_vv,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_rpr_vv))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(180, 20, 675,450))
		self.animacionMostar.setEndValue(QRect(180,600, 675,450))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

		###

	# Funcion parte de ver imagenes
	def Aceptar_visualizador(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_visualizador()
			self.Desbloquear_buttons()
		else:
			pass

	def Cancelar_visualizador(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_visualizador()
			self.Desbloquear_buttons()
		else:
			pass    

	def Mostrar_visualizador(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_visualizador,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_visualizador))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(145, 600, 770,410))
		self.animacionMostar.setEndValue(QRect(145, 60, 770,410))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_visualizador(self):

		self.animacionMostar = QPropertyAnimation(self.frame_principal_visualizador,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_visualizador))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(145, 60, 770,410))
		self.animacionMostar.setEndValue(QRect(145,600, 770,410))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	# Funcion para estudiante
	def Aceptar_estudiante(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_estudiante()
			self.Desbloquear_buttons()
		else:
			pass

	def Cancelar_estudiante(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_estudiante()
			self.Desbloquear_buttons()
		else:
			pass    

	def Mostrar_estudiante(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_estudiante,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_estudiante))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(200, 1000, 613,303))
		self.animacionMostar.setEndValue(QRect(200, 100, 613,303))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_estudiante(self):

		self.animacionMostar = QPropertyAnimation(self.frame_principal_estudiante,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_estudiante))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(200, 100, 613,303))
		self.animacionMostar.setEndValue(QRect(200, 1000, 613,303))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Eliminar(self):
		def establecerValores():
			labelConImagen.clear()
			label_imagen1.clear()
		if self.label_imagen_1_1.pixmap():
			label_imagen1 = self.label_imagen_1_1
		if label_imagen1:
			label_imagen1.clear()
			self.label_imagen_1_1.clear()
					
		# Verificar que QLabel tiene imagen
		labelConNombre = self.label_miniatura_1_nombre
		if labelConNombre:
			labelConNombre.clear()

		labelConImagen = ""
		if self.label_miniatura_1.pixmap():
			labelConImagen = self.label_miniatura_1                     
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_1(self):
		def establecerValores():
			labelConImagen.clear()
			label_imagen2.clear()
			self.label_imagen_2_2.clear()

		if self.label_imagen_2_2.pixmap():
			label_imagen2 = self.label_imagen_2_2
		if label_imagen2:
			label_imagen2.clear()
			self.label_imagen_2_2.clear()

		labelConNombre = self.label_miniatura_2_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_2.pixmap():
			labelConImagen = self.label_miniatura_2
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_2(self):
		def establecerValores():
			labelConImagen.clear()
			self.label_imagen_3_3.clear()
			label_imagen3.clear()

		if self.label_imagen_3_3.pixmap():
			label_imagen3 = self.label_imagen_3_3
		if label_imagen3:
			label_imagen3.clear()
			self.label_imagen_3_3.clear()

		labelConNombre = self.label_miniatura_3_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_3.pixmap():
			labelConImagen = self.label_miniatura_3
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_3(self):
		def establecerValores():
			labelConImagen.clear()
			self.label_imagen_4_4.clear()
			label_imagen4.clear()

		if self.label_imagen_4_4.pixmap():
			label_imagen4 = self.label_imagen_4_4
		if label_imagen4:
			label_imagen4.clear()
			self.label_imagen_4_4.clear()

		labelConNombre = self.label_miniatura_4_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_4.pixmap():
			labelConImagen = self.label_miniatura_4
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_4(self):
		def establecerValores():
			labelConImagen.clear()
			self.label_imagen_5_5.clear()
			label_imagen5.clear()

		if self.label_imagen_5_5.pixmap():
			label_imagen5 = self.label_imagen_5_5
		if label_imagen5:
			label_imagen5.clear()
			self.label_imagen_5_5.clear()

		labelConNombre = self.label_miniatura_5_nombre
		if labelConNombre:
			labelConNombre.clear()

		if self.label_miniatura_5.pixmap():
			labelConImagen = self.label_miniatura_5
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_5(self):
		def establecerValores():
			labelConImagen.clear()
			self.label_imagen_6_6.clear()

			label_imagen6.clear()

		if self.label_imagen_6_6.pixmap():
			label_imagen6 = self.label_imagen_6_6
		if label_imagen6:
			label_imagen6.clear()
			self.label_imagen_6_6.clear()

		labelConNombre = self.label_miniatura_6_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_6.pixmap():
			labelConImagen = self.label_miniatura_6
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")
					
	def Cargar_5(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_5(self.label_miniatura_6, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_6 = imagen
		else:
			None

	def Mostrar_5(self, label, imagen, nombre, posicionX= 400):
		imagen = QPixmap.fromImage(imagen)
		self.label_imagen_6_6.setPixmap(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_6_nombre.setText(nombre)))
													   
		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(400, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_4(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_4(self.label_miniatura_5, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_5 = imagen
		else:
			None

	def Mostrar_4 (self, label, imagen, nombre, posicionX= 210):
		imagen = QPixmap.fromImage(imagen)
		self.label_imagen_5_5.setPixmap(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_5_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(210, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_3(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_3(self.label_miniatura_4, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_4 = imagen
		else:
			None

	def Mostrar_3 (self, label, imagen, nombre, posicionX= 20):
		imagen = QPixmap.fromImage(imagen)
		self.label_imagen_4_4.setPixmap(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_4_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(20, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_2(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")

		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_2(self.label_miniatura_3, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_3 = imagen
		else:
			None

	def Mostrar_2 (self, label, imagen, nombre, posicionX= 400):
		imagen = QPixmap.fromImage(imagen)

		self.label_imagen_3_3.setPixmap(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_3_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(400, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_1(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:               
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_1(self.label_miniatura_2, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_2 = imagen
		else:
			None

	def Mostrar_1 (self, label, imagen, nombre, posicionX= 210):
		imagen = QPixmap.fromImage(imagen)
		self.label_imagen_2_2.setPixmap(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_2_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(210, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  getcwd(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)",
													   options = QFileDialog.Options())

		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar(self.label_miniatura_1, imagen, nombre)
				self.foto_1(imagen)
		else:
			None	

	def foto_1(self,imagen):
		Ver_fotos(imagen,self).exec_()

	def Mostrar(self,label, imagen,nombre, posicionX=20):
		imagen = QPixmap.fromImage(imagen)
		self.label_imagen_1_1.setPixmap(imagen)
	
		# Escalar imagen a 169x119 si el ancho es mayor a 171 o el alto mayor a 121
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119)

		# Mostrar imagen
		label.setPixmap(imagen)
	
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_1_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(20, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def cancelar_viz_user(self):
		cancelar_user = QMessageBox(self)
		cancelar_user.setWindowTitle("Cancelar")
		cancelar_user.setIcon(QMessageBox.Question)
		cancelar_user.setText("¿Estás seguro que desea cancelar?")
		botonSalir_user = cancelar_user.addButton("Si", QMessageBox.YesRole)
		botonCancelar_user = cancelar_user.addButton("No", QMessageBox.NoRole)

		cancelar_user.exec_()

		if cancelar_user.clickedButton() == botonSalir_user:
			self.close()
		else:
			pass

class Ver_fotos(QDialog):
	def __init__(self,imagen, parent=None):
		super(Ver_fotos, self).__init__()

		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		self.parent = parent
		self.imagen = imagen
		self.setWindowTitle("Foto")
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))

		self.setObjectName("Dialog")
		self.resize(521, 401)
		self.move(790,95)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"\n"
		"")
		self.labelimagen = QLabel(self)
		self.labelimagen.setGeometry(QRect(10, 10, 501, 381))
		self.labelimagen.setStyleSheet("QFrame{\n"
		"background-color:#E5E7EE;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.labelimagen.setObjectName("labelimagen")
		self.labelimagen.setAlignment(Qt.AlignCenter)
		pixmap = QPixmap(imagen).scaled(491, 371, Qt.KeepAspectRatio, Qt.SmoothTransformation)
		self.labelimagen.setPixmap(pixmap)

		# Clase de ventana de estatus

# Clase status usuario
class Window_status_user(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Editar usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(783, 460)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)

		self.initUi()

	def initUi(self):
		# Style del frame principal
		Style_frame_principal = ("QFrame#frame{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")

		Style_label_menu = ("QLabel{\n"
							"color:rgb(255, 255, 255);\n"
							"font: 10pt 'Comic Sans MS';\n"
							"border-radius: 6px;\n"
							"text-align: center;"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							"}")

		# Style de frame menu
		Style_frame_menu = ("QFrame{\n"
							"background-color:#12191D;\n"
							"border-radius: 45px\n"
							"}")
		# Style actualizar 
		Style_actualizar_button =("QPushButton{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
									"border-radIus: 3px\n"
									"}\n"
									"QPushButton:hover{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 204, 204, 129));\n"
									"border-radius:10px;\n"
									"}")

		Style_qtable_contenido = ("QTableWidget::item{\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget::item:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget{\n"
									"background-color:#ced4da;\n"
									"border:5px solid #000000;\n"
									"border-radius:10px;\n"
									"color:#000000;\n"
									"}\n"
									"QHeaderView::section{\n"
									"background-color:#12191D;\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000;\n"
									"}\n"
									"QHeaderView::section:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000\n"                                   
									"}\n"
									"QHeaderView::section:checked{\n"
									"background-color: rgb(0, 170, 255);\n"
									"}")

		# Style buttons
		Style_buttons = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"color:rgb(255, 255, 255);\n"
						"font-size: 12px\n"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:rgb(0, 170, 255);\n"
						"color:rgb(255, 255, 255);\n"
						"}")

		# Frame principal contenido
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(180,20,581,411))
		self.frame_principal_contenido.setObjectName("frame")
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)
		self.frame_principal_contenido.setGraphicsEffect(self.shadow)

		# Frame menu
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(30,20,121,411))
		self.frame_menu.setStyleSheet(Style_frame_menu)
		self.frame_menu.setGraphicsEffect(self.shadow)

		# Label de Título
		self.Label_titulo = QLabel(self)
		self.Label_titulo.setText("ESTATUS \nDE \nUSUARIO")
		self.Label_titulo.setGeometry(QRect(60,20,70,100))
		self.Label_titulo.setStyleSheet(Style_label_menu)
		self.Label_titulo.setAlignment(QtCore.Qt.AlignCenter)  

		# Botones
		# Buttons actualizar            
		self.actualizar = QPushButton(self.frame_menu)
		self.actualizar.setGeometry(QRect(50, 120, 23, 21))
		self.actualizar.setStyleSheet(Style_actualizar_button)
		self.actualizar.setIcon(QIcon(":/Icono_recargar/Imagenes-iconos/Recargar.png"))
		self.actualizar.setIconSize(QSize(26,26))
		self.actualizar.setToolTip("Click para actualizar\nla lista de usuarios")

		# Buttons aceptar
		self.aceptar_status = QPushButton(self.frame_menu)
		self.aceptar_status.setText("Aceptar")
		self.aceptar_status.setGeometry(QRect(0, 150, 121, 31))
		self.aceptar_status.setStyleSheet(Style_buttons)
		self.aceptar_status.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.aceptar_status.setIconSize(QSize(15,15))

		# Buttons cancelar
		self.cancelar_stat = QPushButton(self.frame_menu)
		self.cancelar_stat.setText("Cancelar")
		self.cancelar_stat.setGeometry(QRect(0, 190, 121, 31))
		self.cancelar_stat.setStyleSheet(Style_buttons)
		self.cancelar_stat.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.cancelar_stat.setIconSize(QSize(15,15))

		# QTableWidget ==========================================================================================           
		nombreColumnas = ("Usuario", "Cedula", "Fecha", "Hora",
		 "Modificación")
		self.Tabla_contenido = QTableWidget(self.frame_principal_contenido)
		self.Tabla_contenido.setToolTip("Click para ver usuario")
		self.Tabla_contenido.setGeometry(QRect(15,11,551,391))
		self.Tabla_contenido.setStyleSheet(Style_qtable_contenido)
		self.Tabla_contenido.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.Tabla_contenido.setDragDropOverwriteMode(False)
		self.Tabla_contenido.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.Tabla_contenido.setSelectionMode(QAbstractItemView.SingleSelection)
		self.Tabla_contenido.setTextElideMode(Qt.ElideRight)
		self.Tabla_contenido.setWordWrap(False)
		self.Tabla_contenido.setSortingEnabled(False)
		self.Tabla_contenido.setColumnCount(5)
		self.Tabla_contenido.setRowCount(0)
		self.Tabla_contenido.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.Tabla_contenido.horizontalHeader().setHighlightSections(False)
		self.Tabla_contenido.horizontalHeader().setStretchLastSection(True)
		self.Tabla_contenido.verticalHeader().setVisible(False)
		self.Tabla_contenido.setAlternatingRowColors(False)
		self.Tabla_contenido.verticalHeader().setDefaultSectionSize(20)
		self.Tabla_contenido.setHorizontalHeaderLabels(nombreColumnas)

		for indice, ancho in enumerate((110, 110, 110, 110, 130), start=0):
			self.Tabla_contenido.setColumnWidth(indice, ancho)

		# EVENTOS ==========================================================================================            
		self.actualizar.clicked.connect(self.mostrar_datos)
		self.cancelar_stat.clicked.connect(self.Cancelar_status)
		self.aceptar_status.clicked.connect(self.Aceptar_status_user)

	def Aceptar_status_user(self):
		aceptar_status = QMessageBox(self)
		aceptar_status.setWindowTitle("Aceptar")
		aceptar_status.setIcon(QMessageBox.Question)
		aceptar_status.setText("¿Estás seguro de guardar los datos existentes?")
		botonaceptar_status = aceptar_status.addButton("Si", QMessageBox.YesRole)
		botonCancelar_status = aceptar_status.addButton("No", QMessageBox.NoRole)

		aceptar_status.exec_()
		if aceptar_status.clickedButton() == botonaceptar_status:
			self.close()
		else:
			pass

	def mostrar_datos(self):
		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				self.cursor = self.con.cursor()
				self.cursor.execute("SELECT PRIMER_NOMBRE, CEDULA, FECHA, HORA, MODIFICACION FROM USUARIO_DT_GNR")

				datos_Devueltos = self.cursor.fetchall()
				self.Tabla_contenido.clearContents()
				self.Tabla_contenido.setRowCount(0)

				if datos_Devueltos:
					row = 0

					for datos in datos_Devueltos:
						self.Tabla_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.Tabla_contenido.setItem(row, 0, idDato)
						self.Tabla_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.Tabla_contenido.setItem(row, 2, QTableWidgetItem(datos[2]))
						self.Tabla_contenido.setItem(row, 3, QTableWidgetItem(datos[3]))
						self.Tabla_contenido.setItem(row, 4, QTableWidgetItem(datos[4]))
					
						row +=1

				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios "
											"información.   ", QMessageBox.Ok)
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontro la base de datos.   ",
								 QMessageBox.Ok)

	def Cancelar_status(self):
		cerrar_status = QMessageBox(self)
		cerrar_status.setWindowTitle("Cancelar")
		cerrar_status.setIcon(QMessageBox.Question)
		cerrar_status.setText("¿Estás seguro que desea cancelar?")
		botonSalir_status = cerrar_status.addButton("Si", QMessageBox.YesRole)
		botonCancelar_status = cerrar_status.addButton("No", QMessageBox.NoRole)

		cerrar_status.exec_()
		if cerrar_status.clickedButton() == botonSalir_status:
			self.close()
		else:
			pass

# Clase ventana de usuario nuevo
class Window_nv_users(QDialog):
	def __init__(self, parent = None):
		super(Window_nv_users, self).__init__()
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))

		self.setWindowTitle("Nuevo usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(920, 514)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()
		self.centrar()

	def initUi(self):
		
		# Datos generales
		self.groupBox_datosGnr = QGroupBox(self)
		self.groupBox_datosGnr.setGeometry(QRect(170, 10, 341, 493))
		self.groupBox_datosGnr.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		
		self.groupBox_datosGnr.setObjectName("groupBox_datosGnr")
		self.groupBox_datosGnr.setTitle("               Datos Generales")
		self.groupBox_datosGnr.setAlignment(Qt.AlignHCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosGnr.setGraphicsEffect(self.shadow)

		# 1ºNombre =====================================================================================================    
		self.label_1_nombre = QLabel(self.groupBox_datosGnr)
		self.label_1_nombre.setGeometry(QRect(40, 20, 78, 16))
		self.label_1_nombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_1_nombre.setObjectName("label_1_nombre")
		self.label_1_nombre.setText("<font color='#FF3300'>*</font>1ºNombre:")

		self.lineEdit_1_nombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_nombre.setGeometry(QRect(10, 40, 141, 20))
		self.lineEdit_1_nombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid #113384;\n"
		"}")
		self.lineEdit_1_nombre.setText("")
		self.lineEdit_1_nombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_nombre.setObjectName("lineEdit_1_nombre")
		self.lineEdit_1_nombre.setPlaceholderText("Primer nombre")
		self.lineEdit_1_nombre.setToolTip("Ingresa aquí el primer nombre")

		self.lineEdit_1_nombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1_nombre))

			
		# 2ºNombre =====================================================================================================
		self.label_2_nombre = QLabel(self.groupBox_datosGnr)
		self.label_2_nombre.setGeometry(QRect(215, 20, 71, 16))
		self.label_2_nombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_2_nombre.setObjectName("label_2_nombre")
		self.label_2_nombre.setText("2ºNombre:")

		self.lineEdit_2_nombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_nombre.setGeometry(QRect(180, 40, 141, 20))
		self.lineEdit_2_nombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_nombre.setText("")
		self.lineEdit_2_nombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_nombre.setObjectName("lineEdit_2_nombre")
		self.lineEdit_2_nombre.setPlaceholderText("Segundo nombre")
		self.lineEdit_2_nombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2_nombre))
		self.lineEdit_2_nombre.setToolTip("Ingresa aquí el segundo nombre")

		# 1º Apellido =====================================================================================================     
		self.label_1_Apellido = QLabel(self.groupBox_datosGnr)
		self.label_1_Apellido.setGeometry(QRect(40, 70, 78, 16))
		self.label_1_Apellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1_Apellido.setAlignment(Qt.AlignCenter)
		self.label_1_Apellido.setObjectName("label_1_Apellido")
		self.label_1_Apellido.setText("<font color='#FF3300'>*</font>1ºApellido:")


		self.lineEdit_1_Apellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_Apellido.setGeometry(QRect(10, 90, 141, 20))
		self.lineEdit_1_Apellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1_Apellido.setText("")        
		self.lineEdit_1_Apellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_Apellido.setObjectName("lineEdit_1ºApellido")
		self.lineEdit_1_Apellido.setPlaceholderText("Primer apellido")
		self.lineEdit_1_Apellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1_Apellido))
		self.lineEdit_1_Apellido.setToolTip("Ingresa aquí el primer apellido")

		# 2º Apellido =====================================================================================================     
		self.lineEdit_2_Apellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_Apellido.setGeometry(QRect(180, 90, 141, 20))
		self.lineEdit_2_Apellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_Apellido.setText("")
		self.lineEdit_2_Apellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_Apellido.setObjectName("lineEdit_2ºApellido")
		self.lineEdit_2_Apellido.setToolTip("Ingresa aquí el segundo apellido")

		self.label_2_Apellido = QLabel(self.groupBox_datosGnr)
		self.label_2_Apellido.setGeometry(QRect(215, 70, 71, 16))
		self.label_2_Apellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2_Apellido.setAlignment(Qt.AlignCenter)
		self.label_2_Apellido.setObjectName("label_2_Apellido")
		self.label_2_Apellido.setText("2ºApellido:")
		self.lineEdit_2_Apellido.setPlaceholderText("Segundo apellido")
		self.lineEdit_2_Apellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2_Apellido))
	   
		# Cedula de identidad =====================================================================================================     
		self.label_cedula = QLabel(self.groupBox_datosGnr)
		self.label_cedula.setGeometry(QRect(10, 125, 140, 16))
		self.label_cedula.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_cedula.setAlignment(Qt.AlignCenter)
		self.label_cedula.setObjectName("label_cedula")
		self.label_cedula.setText("<font color='#FF3300'>*</font>Cedula de intentidad:")

		self.lineEdit_cedula = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_cedula.setGeometry(QRect(10, 145, 141, 20))
		self.lineEdit_cedula.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid #113384;\n"
		"}")
		self.lineEdit_cedula.setText("")
		self.lineEdit_cedula.setAlignment(Qt.AlignCenter)
		self.lineEdit_cedula.setObjectName("lineEdit_cedula")
		self.lineEdit_cedula.setPlaceholderText("Ingresa la cedula")
		self.lineEdit_cedula.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_cedula))
		self.lineEdit_cedula.setToolTip("Ingresa aquí la cedula de identidad")

		# Telefono =====================================================================================================        
		self.label_tlf = QLabel(self.groupBox_datosGnr)
		self.label_tlf.setGeometry(QRect(215, 125, 71, 16))
		self.label_tlf.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_tlf.setAlignment(Qt.AlignCenter)
		self.label_tlf.setObjectName("label_tlf")
		self.label_tlf.setText("<font color='#FF3300'>*</font>Telefonos:")

		self.lineEdit_1_tlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1_tlf.setGeometry(QRect(180, 145, 141, 20))
		self.lineEdit_1_tlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1_tlf.setText("")
		self.lineEdit_1_tlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_1_tlf.setObjectName("lineEdit_1_tlf")
		self.lineEdit_1_tlf.setPlaceholderText("Principal")
		self.lineEdit_1_tlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_1_tlf))
		self.lineEdit_1_tlf.setToolTip("Ingresa aquí el numero telefónico principal")

		self.lineEdit_2_tlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2_tlf.setGeometry(QRect(180, 170, 141, 20))
		self.lineEdit_2_tlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2_tlf.setText("")
		self.lineEdit_2_tlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_2_tlf.setObjectName("lineEdit_2_tlf")
		self.lineEdit_2_tlf.setPlaceholderText("Secundario")
		self.lineEdit_2_tlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_2_tlf))
		self.lineEdit_2_tlf.setToolTip("Ingresa aquí el numero de telefónico secundario")

		# Genero ========================================================================================================         
		self.comboBox_genero = QComboBox(self.groupBox_datosGnr)
		self.comboBox_genero.setGeometry(QRect(10, 200, 141, 21))
		self.comboBox_genero.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius:3px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_genero.setEditable(False)
		self.comboBox_genero.setObjectName("comboBox_genero")

		self.items_list_genero = ["Masculino", "Femenino"]
		self.comboBox_genero.addItems(self.items_list_genero)
		self.comboBox_genero.setToolTip("Selecciona el genero ")

		self.label_genero = QLabel(self.groupBox_datosGnr)
		self.label_genero.setGeometry(QRect(45, 180, 71, 16))
		self.label_genero.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_genero.setAlignment(Qt.AlignCenter)
		self.label_genero.setObjectName("label_genero")
		self.label_genero.setText("<font color='#FF3300'>*</font>Genero:")
				
		# Edad ========================================================================================================       
		self.label_edad = QLabel(self.groupBox_datosGnr)
		self.label_edad.setGeometry(QRect(225, 205, 51, 16))
		self.label_edad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_edad.setAlignment(Qt.AlignCenter)
		self.label_edad.setObjectName("label_edad")
		self.label_edad.setText("<font color='#FF3300'>*</font>Edad:")

		self.lineEdit_edad = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_edad.setGeometry(QRect(180, 225, 141, 20))
		self.lineEdit_edad.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_edad.setText("")
		self.lineEdit_edad.setAlignment(Qt.AlignCenter)
		self.lineEdit_edad.setObjectName("lineEdit_edad")
		self.lineEdit_edad.setPlaceholderText("Ingresa la edad")
		self.lineEdit_edad.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_edad))
		self.lineEdit_edad.setToolTip("Ingresa aquí la edad")
	  
		# Fecha de nacimiento ========================================================================================================          
		self.dateEdit_nacimiento = QDateEdit(self.groupBox_datosGnr)
		self.dateEdit_nacimiento.setGeometry(QRect(10, 255, 141, 22))
		self.dateEdit_nacimiento.setStyleSheet("QDateEdit{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"\n"
		"}")
		self.dateEdit_nacimiento.setObjectName("dateEdit_nacimiento")
		self.dateEdit_nacimiento.setDate(QDate.currentDate())
		self.dateEdit_nacimiento.setMaximumDate(QDate.currentDate())
		self.dateEdit_nacimiento.setDisplayFormat("dd/MM/yyyy")
		self.dateEdit_nacimiento.setCalendarPopup(True)
		self.dateEdit_nacimiento.setCursor(Qt.PointingHandCursor)
		self.dateEdit_nacimiento.setToolTip("Selecciona la fecha de nacimiento")

		self.label_fch_nacimiento = QLabel(self.groupBox_datosGnr)
		self.label_fch_nacimiento.setGeometry(QRect(20, 235, 131, 16))
		self.label_fch_nacimiento.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_fch_nacimiento.setAlignment(Qt.AlignCenter)
		self.label_fch_nacimiento.setObjectName("label_fch_nacimiento")
		self.label_fch_nacimiento.setText("Fecha de nacimiento:")

		# Opciones de checkbox datos generales ========================================================================================================       
		self.label_opciones = QLabel(self.groupBox_datosGnr)
		self.label_opciones.setGeometry(QRect(180, 260, 141, 19))
		self.label_opciones.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 10px")
		self.label_opciones.setAlignment(Qt.AlignCenter)
		self.label_opciones.setObjectName("label_opciones")
		self.label_opciones.setText("Posee alguna de las opciones:")

		self.checkBox_1_pensionado = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_1_pensionado.setGeometry(QRect(200, 280, 100, 17))
		self.checkBox_1_pensionado.setObjectName("checkBox_1_pensionado")
		self.checkBox_1_pensionado.setText("Pensionado")
		self.checkBox_1_pensionado.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")        
		
		self.checkBox_2_discapacidad = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_2_discapacidad.setGeometry(QRect(200, 300, 110, 17))
		self.checkBox_2_discapacidad.setObjectName("checkBox_2_discapacidad")
		self.checkBox_2_discapacidad.setText("Discapacidad")
		self.checkBox_2_discapacidad.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_3_enfer = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_3_enfer.setGeometry(QRect(200, 320, 100, 17))
		self.checkBox_3_enfer.setText("Enfermedad")
		self.checkBox_3_enfer.setObjectName("checkBox_3_enfer")
		self.checkBox_3_enfer.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_4_Embarazada = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_4_Embarazada.setGeometry(QRect(200, 340, 100, 17))
		self.checkBox_4_Embarazada.setObjectName("checkBox_4_Embarazada")
		self.checkBox_4_Embarazada.setText("Embarazada")
		self.checkBox_4_Embarazada.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_5_lactante = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_5_lactante.setGeometry(QRect(200, 360, 100, 17))
		self.checkBox_5_lactante.setObjectName("checkBox_5_lactante")
		self.checkBox_5_lactante.setText("Lactante")
		self.checkBox_5_lactante.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		# Profesion u oficio =================================================================================================
		self.label_profesion = QLabel(self.groupBox_datosGnr)
		self.label_profesion.setGeometry(QRect(30, 290, 101, 16))
		self.label_profesion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_profesion.setAlignment(Qt.AlignCenter)
		self.label_profesion.setObjectName("label_profesion")
		self.label_profesion.setText("Profesión u oficio:")

		self.comboBox_profesion = QComboBox(self.groupBox_datosGnr)
		self.comboBox_profesion.setGeometry(QRect(10, 310, 141, 21))
		self.comboBox_profesion.setToolTip("Selecciona la profesión")
		self.comboBox_profesion.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_profesion.setEditable(False)
		self.comboBox_profesion.setObjectName("comboBox_profesion")

		self.items_list_profesion = ['Contador', 'Albañil', 'Conductor de autobús', 'Carnicero', 'Carpintero',
		'Cocinero','Médico','Enfermero', 'Mecánico','Herrero','Abogado','Trabajador social','Funcionario público',
		'Profesor','Veterinario','Estudiante','Otro...'
		'']

		self.comboBox_profesion.addItems(self.items_list_profesion)

		# Nivel de instruccion ========================================================================================================       
		self.label_nvl_instruccion = QLabel(self.groupBox_datosGnr)
		self.label_nvl_instruccion.setGeometry(QRect(20, 345, 121, 16))
		self.label_nvl_instruccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_nvl_instruccion.setAlignment(Qt.AlignCenter)
		self.label_nvl_instruccion.setObjectName("label_nvl_instruccion")
		self.label_nvl_instruccion.setText("Nivel de instrucción:")

		self.comboBox_nvl_instruccion = QComboBox(self.groupBox_datosGnr)
		self.comboBox_nvl_instruccion.setGeometry(QRect(10, 365, 141, 21))
		self.comboBox_nvl_instruccion.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")
		self.comboBox_nvl_instruccion.setEditable(False)
		self.comboBox_nvl_instruccion.setToolTip("Selecciona el nivel de instrucción")
		self.comboBox_nvl_instruccion.setObjectName("comboBox_nvl_instruccion")

		self.Items_list_instruccion = ['Primaria', 'Bachillerato', 'Técnico superior', 
		'Universitario', 'Especialización', 'Postgrado', 'Doctorado']
		self.comboBox_nvl_instruccion.addItems(self.Items_list_instruccion)

		# Parentesco ========================================================================================================         
		self.label_parentesco = QLabel(self.groupBox_datosGnr)
		self.label_parentesco.setGeometry(QRect(210, 390, 81, 16))
		self.label_parentesco.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_parentesco.setAlignment(Qt.AlignCenter)
		self.label_parentesco.setObjectName("label_parentesco")
		self.label_parentesco.setText("<font color='#FF3300'>*</font>Parentesco:")

		self.comboBox_parentesco = QComboBox(self.groupBox_datosGnr)
		self.comboBox_parentesco.setGeometry(QRect(180, 410, 141, 21))
		self.comboBox_parentesco.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")

		self.comboBox_parentesco.setEditable(False)
		self.comboBox_parentesco.setObjectName("comboBox_parentesco")
		self.comboBox_parentesco.setToolTip("Selecciona el parentesco")

		self.items_list_parentesco = ['Jefe/a de familia', 'Padre', 'Madre', 'Hijo/a', 'Yerno', 'Nuera', 
		'Abuelo/a', 'Nieto/a', 'Hermano/a', 'Cuñado/a', 'Bisabuelo/a', 'Biznieto/a', 'Tío/a', 'Sobrino/a']
		self.comboBox_parentesco.addItems(self.items_list_parentesco)
		
		# Estado civil ========================================================================================================       
		self.label_estadocivil = QLabel(self.groupBox_datosGnr)
		self.label_estadocivil.setGeometry(QRect(45, 400, 71, 16))
		self.label_estadocivil.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_estadocivil.setAlignment(Qt.AlignCenter)
		self.label_estadocivil.setObjectName("label_estadocivil")
		self.label_estadocivil.setText("<font color='#FF3300'>*</font>Estado civil:")

		self.comboBox_estadocivil = QComboBox(self.groupBox_datosGnr)
		self.comboBox_estadocivil.setGeometry(QRect(10, 420, 141, 21))
		self.comboBox_estadocivil.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"color: #000000;\n"
		"}\n"
		"")

		self.comboBox_estadocivil.setEditable(False)
		self.comboBox_estadocivil.setToolTip("Selecciona el estado civil actual")
		self.comboBox_estadocivil.setObjectName("comboBox_estadocivil")
		self.items_list_estadocivil = ['Soltero', 'Casado']
		self.comboBox_estadocivil.addItems(self.items_list_estadocivil)

		# Inscrito en el REP ========================================================================================================         
		self.label_inscritoREP = QLabel(self.groupBox_datosGnr)
		self.label_inscritoREP.setGeometry(QRect(25, 455, 111, 16))
		self.label_inscritoREP.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_inscritoREP.setAlignment(Qt.AlignCenter)
		self.label_inscritoREP.setObjectName("label_inscritoREP")
		self.label_inscritoREP.setText("Esta inscrito en REP:")

		self.radiobutton_si_inscrito = QRadioButton(self.groupBox_datosGnr)
		self.radiobutton_si_inscrito.setGeometry(QRect(30, 471, 38, 17))
		"color:#000000\n"
		self.radiobutton_si_inscrito.setToolTip("Selecciona 'Si' si está inscrito\n"
												"en el registro electoral permanente")
		self.radiobutton_si_inscrito.setObjectName("radiobutton_si_inscrito")
		self.radiobutton_si_inscrito.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  
		self.radiobutton_si_inscrito.setText("Si")

		self.radiobutton_no_inscrito = QRadioButton(self.groupBox_datosGnr)
		self.radiobutton_no_inscrito.setGeometry(QRect(85, 471, 45, 17))
		self.radiobutton_no_inscrito.setObjectName("radiobutton_no_inscrito")
		self.radiobutton_no_inscrito.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  
		self.radiobutton_no_inscrito.setText("No")
		self.radiobutton_no_inscrito.setToolTip("Selecciona 'No' si no está inscrito\n"
												"en el registro electoral permanente")

		# Ingresar el correo ========================================================================================================         
		self.label_correo = QLabel(self.groupBox_datosGnr)
		self.label_correo.setGeometry(QRect(195, 445, 111, 16))
		self.label_correo.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 11px")
		self.label_correo.setAlignment(Qt.AlignCenter)
		self.label_correo.setObjectName("label_correo")
		self.label_correo.setText("Correo electronico: ")

		self.lineEdit_correo = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_correo.setGeometry(QRect(180, 465, 141, 20))
		self.lineEdit_correo.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_correo.setText("")
		self.lineEdit_correo.setAlignment(Qt.AlignCenter)
		self.lineEdit_correo.setObjectName("lineEdit_correo")
		self.lineEdit_correo.setPlaceholderText("Ingresa el correo")
		self.lineEdit_correo.setToolTip("Ingresa un correo electrónico vigente")

		# Ubicación geografica
		self.groupBox_datosUb = QGroupBox(self)
		self.groupBox_datosUb.setGeometry(QRect(530, 10, 371, 181))
		self.groupBox_datosUb.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosUb.setAlignment(Qt.AlignCenter)
		self.groupBox_datosUb.setObjectName("groupBox_datosUb")
		self.groupBox_datosUb.setTitle("                        Ubicación geográfica")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosUb.setGraphicsEffect(self.shadow)
		# Estado ========================================================================================================         
		self.label_estado = QLabel(self.groupBox_datosUb)
		self.label_estado.setGeometry(QRect(60, 20, 61, 16))
		self.label_estado.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_estado.setAlignment(Qt.AlignCenter)
		self.label_estado.setObjectName("label_estado")
		self.label_estado.setText("Estado:")

		self.lineEdit_estado = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_estado.setGeometry(QRect(20, 40, 141, 20))
		self.lineEdit_estado.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_estado.setText("")
		self.lineEdit_estado.setAlignment(Qt.AlignCenter)
		self.lineEdit_estado.setObjectName("lineEdit_estado")
		self.lineEdit_estado.setToolTip("Ingresa el estado donde se residencia")
		self.lineEdit_estado.setPlaceholderText("Ingresa el estado")
		self.lineEdit_estado.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_estado))

		# Municipio ========================================================================================================          
		self.label_municipio = QLabel(self.groupBox_datosUb)
		self.label_municipio.setGeometry(QRect(55, 70, 71, 16))
		self.label_municipio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_municipio.setAlignment(Qt.AlignCenter)
		self.label_municipio.setObjectName("label_municipio")
		self.label_municipio.setText("Municipio:")

		self.lineEdit_municipio = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_municipio.setGeometry(QRect(20, 90, 141, 20))
		self.lineEdit_municipio.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_municipio.setText("")
		self.lineEdit_municipio.setAlignment(Qt.AlignCenter)
		self.lineEdit_municipio.setObjectName("lineEdit_municipio")
		self.lineEdit_municipio.setToolTip("Ingresa el municipio donde se residencia")
		self.lineEdit_municipio.setPlaceholderText("Ingresa el municipio")
		self.lineEdit_municipio.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_municipio))

		# Parroquia ========================================================================================================          
		self.label_parroquia = QLabel(self.groupBox_datosUb)
		self.label_parroquia.setGeometry(QRect(55, 120, 71, 16))
		self.label_parroquia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_parroquia.setAlignment(Qt.AlignCenter)
		self.label_parroquia.setObjectName("label_parroquia")
		self.label_parroquia.setText("Parroquia:")

		self.lineEdit_parroquia = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_parroquia.setGeometry(QRect(20, 140, 141, 20))
		self.lineEdit_parroquia.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_parroquia.setText("")
		self.lineEdit_parroquia.setAlignment(Qt.AlignCenter)
		self.lineEdit_parroquia.setObjectName("lineEdit_parroquia")
		self.lineEdit_parroquia.setToolTip("Ingresa la parroquia donde se residencia")
		self.lineEdit_parroquia.setPlaceholderText("Ingresa la parroquia")
		self.lineEdit_parroquia.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_parroquia))


		# Nº de vivienda ========================================================================================================         
		self.label_N_vivienda = QLabel(self.groupBox_datosUb)
		self.label_N_vivienda.setGeometry(QRect(220, 130, 111, 16))
		self.label_N_vivienda.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_N_vivienda.setAlignment(Qt.AlignCenter)
		self.label_N_vivienda.setObjectName("label_N_vivienda")
		self.label_N_vivienda.setText("<font color='#FF3300'>*</font>Nº de vivienda:")

		self.lineEdit_N_vivienda = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_N_vivienda.setGeometry(QRect(205, 150, 141, 20))
		self.lineEdit_N_vivienda.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_N_vivienda.setText("")
		self.lineEdit_N_vivienda.setAlignment(Qt.AlignCenter)
		self.lineEdit_N_vivienda.setObjectName("lineEdit_N_vivienda")
		self.lineEdit_N_vivienda.setToolTip("Ingresa el numero de la vivienda")
		self.lineEdit_N_vivienda.setPlaceholderText("Numero de vivienda")
		self.lineEdit_N_vivienda.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_N_vivienda))


		# Direccion ========================================================================================================          
		self.label_direccion = QLabel(self.groupBox_datosUb) 
		self.label_direccion.setGeometry(QRect(193, 20, 161, 16))
		self.label_direccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_direccion.setAlignment(Qt.AlignCenter)
		self.label_direccion.setObjectName("label_direccion")
		self.label_direccion.setText("<font color='#FF3300'>*</font>Dirección y donde vota:")
		self.textEdit_direccion = QTextEdit(self.groupBox_datosUb)
		self.textEdit_direccion.setGeometry(QRect(193, 40, 161, 71))
		self.textEdit_direccion.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_direccion.setObjectName("textEdit_direccion")
		self.textEdit_direccion.setPlaceholderText("Ingresa la dirección\n"
													"Y lugar donde vota...")
		self.textEdit_direccion.setToolTip("Ingresa la dirección donde se residencia\n"
										   "Y lugar donde vota ")

		# Datos de la vivienda
		self.groupBox_datos_Vv = QGroupBox(self)
		self.groupBox_datos_Vv.setGeometry(QRect(530, 200, 371, 171))
		self.groupBox_datos_Vv.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datos_Vv.setAlignment(Qt.AlignCenter)
		self.groupBox_datos_Vv.setObjectName("groupBox_datosGnr_Vv")
		self.groupBox_datos_Vv.setTitle("                      Datos de la vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_Vv.setGraphicsEffect(self.shadow)
		# Metros cuadrados ========================================================================================================       
		self.label_M2 = QLabel(self.groupBox_datos_Vv)
		self.label_M2.setGeometry(QRect(25, 20, 121, 16))
		self.label_M2.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_M2.setAlignment(Qt.AlignCenter)
		self.label_M2.setObjectName("label_M2")
		self.label_M2.setText("Metros cuadrados:")

		self.lineEdit_M2 = QLineEdit(self.groupBox_datos_Vv)
		self.lineEdit_M2.setGeometry(QRect(15, 40, 141, 20))
		self.lineEdit_M2.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"color: #000000;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_M2.setText("")
		self.lineEdit_M2.setAlignment(Qt.AlignCenter)
		self.lineEdit_M2.setObjectName("lineEdit_M2")
		self.lineEdit_M2.setPlaceholderText("Ingresa los metros")
		self.lineEdit_M2.setToolTip("Ejemplo: Si la vivienda posee 12 metro cuadrados,\n"
									"escribirlo de esta manera: 12m^2")

		# Necesita alguna reparacion ========================================================================================================         
		self.label_reparacion = QLabel(self.groupBox_datos_Vv)
		self.label_reparacion.setGeometry(QRect(185, 130, 171, 16))
		self.label_reparacion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_reparacion.setAlignment(Qt.AlignCenter)
		self.label_reparacion.setObjectName("label_reparacion")
		self.label_reparacion.setText("Necesita alguna reparación:")

		self.radioButton_rp_si = QRadioButton(self.groupBox_datos_Vv)
		self.radioButton_rp_si.setGeometry(QRect(220, 150, 51, 17))
		self.radioButton_rp_si.setObjectName("radioButton_rp_si")
		self.radioButton_rp_si.setText("Si")
		self.radioButton_rp_si.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"}")
		self.radioButton_rp_si.setToolTip("Seleccione 'Si' si la vivienda\n"
											"necesita de alguna reparación")  

		self.radioButton_rp_no = QRadioButton(self.groupBox_datos_Vv)
		self.radioButton_rp_no.setGeometry(QRect(280, 150, 51, 17))
		self.radioButton_rp_no.setObjectName("radioButton_rp_no")
		self.radioButton_rp_no.setText("No")
		self.radioButton_rp_no.setStyleSheet("QRadioButton{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"}") 
		self.radioButton_rp_no.setToolTip("Seleccione 'No' si la vivienda\n"
											"no necesita de alguna reparación")   
		
		# Servivcios que posee ========================================================================================================            
		self.label_servicios = QLabel(self.groupBox_datos_Vv)
		self.label_servicios.setGeometry(QRect(195, 20, 151, 16))
		self.label_servicios.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_servicios.setAlignment(Qt.AlignCenter)
		self.label_servicios.setObjectName("label_servicios")
		self.label_servicios.setText("Servicios que posee:")


		self.checkBox_aguapotable = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguapotable.setGeometry(QRect(175 ,40, 98, 17))
		self.checkBox_aguapotable.setObjectName("checkBox_aguapotable")
		self.checkBox_aguapotable.setText("Agua potable")
		self.checkBox_aguapotable.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_aguasservidas = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguasservidas.setGeometry(QRect(175, 60, 100, 17))
		self.checkBox_aguasservidas.setObjectName("checkBox_aguasservidas")
		self.checkBox_aguasservidas.setText("Aguas servidas")
		self.checkBox_aguasservidas.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_gasdirecto = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasdirecto.setGeometry(QRect(175, 80, 91, 17))
		self.checkBox_gasdirecto.setObjectName("checkBox_gasdirecto")
		self.checkBox_gasdirecto.setText("Gas directo")
		self.checkBox_gasdirecto.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_gasbombona = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasbombona.setGeometry(QRect(175, 100, 111, 17))
		self.checkBox_gasbombona.setObjectName("checkBox_gasbombona")
		self.checkBox_gasbombona.setText("Gas bombona")
		self.checkBox_gasbombona.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")


		self.checkBox_internet = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_internet.setGeometry(QRect(274, 40, 81, 17))
		self.checkBox_internet.setObjectName("checkBox_internet")
		self.checkBox_internet.setText("Internet")
		self.checkBox_internet.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_electricidad = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_electricidad.setGeometry(QRect(274, 60, 91, 17))
		self.checkBox_electricidad.setObjectName("checkBox_electricidad")
		self.checkBox_electricidad.setText("Electricidad")
		self.checkBox_electricidad.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		self.checkBox_tlf_fijo = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_tlf_fijo.setGeometry(QRect(274, 80, 101, 17))
		self.checkBox_tlf_fijo.setObjectName("checkBox_tlf_fijo")
		self.checkBox_tlf_fijo.setText("Telefono fijo")
		self.checkBox_tlf_fijo.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 11px;\n"
		"}")  

		# Descripcion de la vivienda ========================================================================================================              
		self.label_dcrp_vv = QLabel(self.groupBox_datos_Vv)
		self.label_dcrp_vv.setGeometry(QRect(10, 80, 151, 16))
		self.label_dcrp_vv.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_dcrp_vv.setAlignment(Qt.AlignCenter)
		self.label_dcrp_vv.setObjectName("label_dcrp_vv")
		self.label_dcrp_vv.setText("Descripción de vivienda:")
		self.textEdit_dcrp_vv = QTextEdit(self.groupBox_datos_Vv)
		self.textEdit_dcrp_vv.setGeometry(QRect(10, 100, 151, 51))
		self.textEdit_dcrp_vv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_vv.setObjectName("textEdit_dcrp_vv")
		self.textEdit_dcrp_vv.setPlaceholderText("Describa la vivienda...")
		self.textEdit_dcrp_vv.setToolTip("Describa la vivienda si es una casa de una planta o dos,\n"
										"si es un apartamento o quinta, entre otras... ")

		# Proteccion Social	  
		self.groupBox_beneficios = QGroupBox(self)
		self.groupBox_beneficios.setGeometry(QRect(530, 380, 371, 123))
		self.groupBox_beneficios.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_beneficios.setAlignment(Qt.AlignCenter)
		self.groupBox_beneficios.setObjectName("groupBox_beneficios")
		self.groupBox_beneficios.setTitle("                  Proteccion social")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_beneficios.setGraphicsEffect(self.shadow)

		# Posee algun beneficio ========================================================================================================               
		self.label_beneficio = QLabel(self.groupBox_beneficios)
		self.label_beneficio.setGeometry(QRect(10, 20, 161, 16))
		self.label_beneficio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_beneficio.setAlignment(Qt.AlignCenter)
		self.label_beneficio.setObjectName("label_beneficio")
		self.label_beneficio.setText("Posee algun beneficio:")

		self.checkBox_hogarespatria = QCheckBox(self.groupBox_beneficios)
		self.checkBox_hogarespatria.setGeometry(QRect(10, 40, 151, 17))
		self.checkBox_hogarespatria.setObjectName("checkBox_hogarespatria")
		self.checkBox_hogarespatria.setText("Hogares de la patria")
		self.checkBox_hogarespatria.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"        
		"}")  

		self.checkBox_partohumanizado = QCheckBox(self.groupBox_beneficios)
		self.checkBox_partohumanizado.setGeometry(QRect(10, 100, 141, 20))
		self.checkBox_partohumanizado.setObjectName("checkBox_partohumanizado")
		self.checkBox_partohumanizado.setText("Parto humanizado")
		self.checkBox_partohumanizado.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_amormayor = QCheckBox(self.groupBox_beneficios)
		self.checkBox_amormayor.setGeometry(QRect(10, 60, 101, 17))
		self.checkBox_amormayor.setObjectName("checkBox_amormayor")
		self.checkBox_amormayor.setText("Amor mayor")
		self.checkBox_amormayor.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_joseGregorio  = QCheckBox(self.groupBox_beneficios)
		self.checkBox_joseGregorio.setGeometry(QRect(10, 80, 181, 17))
		self.checkBox_joseGregorio.setObjectName("checkBox_joseGregorio")
		self.checkBox_joseGregorio.setText("Dr. José Gregorio Hernández")
		self.checkBox_joseGregorio.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.label_grpsociales = QLabel(self.groupBox_beneficios)
		self.label_grpsociales.setGeometry(QRect(185,20,171,16))
		self.label_grpsociales.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_grpsociales.setAlignment(Qt.AlignCenter)
		self.label_grpsociales.setObjectName("label_grpsociales")
		self.label_grpsociales.setText("Esta en algun grupo social:")


		self.checkBox_somosvenezuela = QCheckBox(self.groupBox_beneficios)
		self.checkBox_somosvenezuela.setGeometry(QRect(200, 60, 131, 17))
		self.checkBox_somosvenezuela.setObjectName("checkBox_somosvenezuela")
		self.checkBox_somosvenezuela.setText("Somos Venezuela")
		self.checkBox_somosvenezuela.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_chambajuvenil = QCheckBox(self.groupBox_beneficios)
		self.checkBox_chambajuvenil.setGeometry(QRect(200, 40, 121, 17))
		self.checkBox_chambajuvenil.setObjectName("checkBox_chambajuvenil")
		self.checkBox_chambajuvenil.setText("Chamba juvenil")
		self.checkBox_chambajuvenil.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_FrenteMiranda = QCheckBox(self.groupBox_beneficios)
		self.checkBox_FrenteMiranda.setGeometry(QRect(200, 80, 191, 17))
		self.checkBox_FrenteMiranda.setObjectName("checkBox_FrenteMiranda")
		self.checkBox_FrenteMiranda.setText("Frente Francisco Miranda")
		self.checkBox_FrenteMiranda.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		self.checkBox_jpsuv = QCheckBox(self.groupBox_beneficios)
		self.checkBox_jpsuv.setGeometry(QRect(200, 100, 141, 17))
		self.checkBox_jpsuv.setObjectName("checkBox_jpsuv")
		self.checkBox_jpsuv.setText("JPSUV")
		self.checkBox_jpsuv.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000;\n"
		"font-size: 12px;\n"
		"}")  

		# Datos de estudiante
		self.frame_principal_estudiante = QFrame(self)
		self.frame_principal_estudiante.setGeometry(QRect(200,100,613,303))
		self.frame_principal_estudiante.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477,\n"
		"stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius:30px}")
		self.frame_principal_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_estudiante.move(200,1000)

		# Menu ========================================================================================================            
		self.frame_menu_estudiante = QFrame(self.frame_principal_estudiante)
		self.frame_menu_estudiante.setGeometry(QRect(20,20,121,261))
		self.frame_menu_estudiante.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius: 45px;\n"
		"}")
		self.frame_menu_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)

		self.label_estudiante = QLabel(self.frame_menu_estudiante)
		self.label_estudiante.setGeometry(QRect(20,10,81,20))
		self.label_estudiante.setText("Estudiante")
		self.label_estudiante.setStyleSheet("QLabel{\n"
		"color:rgb(255, 255, 255);\n"
		"font: 11pt Comic Sans MS;\n"
		"border-radius: 6px;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
		"}")

		self.label_estudiante.setAlignment(Qt.AlignHCenter)
		
		# Buttons de menu
		self.Button_aceptar_estudiante = QPushButton(self.frame_menu_estudiante)
		self.Button_aceptar_estudiante.setGeometry(QRect(0,80,121,31))
		self.Button_aceptar_estudiante.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px\n"
		"}\n"

		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"}")
		self.Button_aceptar_estudiante.setText("Aceptar")
		self.Button_aceptar_estudiante.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.Button_aceptar_estudiante.setIconSize(QSize(15,15))

		self.Button_cancelar_estudiante = QPushButton(self.frame_menu_estudiante)
		self.Button_cancelar_estudiante.setGeometry(QRect(2,110,121,31))
		self.Button_cancelar_estudiante.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px\n"
		"}\n"

		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"}")
		self.Button_cancelar_estudiante.setText("Cancelar")
		self.Button_cancelar_estudiante.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancelar_estudiante.setIconSize(QSize(15,15))

		self.frame_contenido_estudiante = QFrame(self.frame_principal_estudiante)
		self.frame_contenido_estudiante.setGeometry(QRect(170,20,421,261))
		self.frame_contenido_estudiante.setStyleSheet("color:#1b231f;\n"
		"background-color: #E5E7EE;\n"
		"font: 75 10pt Comic Sans MS;\n"
		"border-radius: 22px;")
		self.frame_contenido_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		# Nivel de instruccion ========================================================================================================            

		# label nivel de estudio:
		self.label_nivel_de_estudio = QLabel(self.frame_contenido_estudiante)
		self.label_nivel_de_estudio.setGeometry(QRect(70,10,125,16))
		self.label_nivel_de_estudio.setText("Nivel de estudio:")
		self.label_nivel_de_estudio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_nivel_de_estudio.setAlignment(Qt.AlignHCenter)

		# CheckBox de niveles de estudio primaria
		self.checkbox_primaria = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_primaria.setGeometry(QRect(20,30,121,21))
		self.checkbox_primaria.setText("Primaria")

		# CheckBox de niveles de estudio bachillerato
		self.checkbox_bachillerato = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_bachillerato.setGeometry(QRect(20,50,121,21))
		self.checkbox_bachillerato.setText("Bachillerato")

		# CheckBox de niveles de estudio tecnico superior
		self.checkbox_tcn_superior = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_tcn_superior.setGeometry(QRect(20,70,221,21))
		self.checkbox_tcn_superior.setText("Técnico superior universitario")

		# CheckBox de niveles de estudio universitario
		self.checkbox_universitario = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_universitario.setGeometry(QRect(20,90,111,21))
		self.checkbox_universitario.setText("Universitario")

		# CheckBox de niveles de estudio especializacion
		self.checkbox_especializacion = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_especializacion.setGeometry(QRect(20,110,131,21))
		self.checkbox_especializacion.setText("Especialización ")
		
		# Carrera que estudia ========================================================================================================             
		# Label de tipo de carrera
		self.label_carrera_que_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_carrera_que_estudia.setGeometry(QRect(255,10,145,16))
		self.label_carrera_que_estudia.setText("Carrera que estudia:")
		self.label_carrera_que_estudia.setAlignment(Qt.AlignHCenter)
		self.label_carrera_que_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")

		# QTextEdit de carrera que estudia
		self.texedit_carrera = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_carrera.setGeometry(QRect(250,30,161,81))
		self.texedit_carrera.setPlaceholderText("Carrera que cursa...")
		self.texedit_carrera.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")

		# Donde estudia ========================================================================================================               
		# Qlabel de donde estudia
		self.label_donde_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_donde_estudia.setGeometry(QRect(160,140,111,16))
		self.label_donde_estudia.setText("Donde estudia:")
		self.label_donde_estudia.setAlignment(Qt.AlignHCenter)
		self.label_donde_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")

		# QTextEdit de donde estudia
		self.texedit_donde_estudia = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_donde_estudia.setGeometry(QRect(40,160,341,81))
		self.texedit_donde_estudia.setPlaceholderText("Dirección y universidad donde estudia...")
		self.texedit_donde_estudia.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")

		# Ventana discapacidad
		self.frame_principal_Discpacidad = QFrame(self)
		self.frame_principal_Discpacidad.setGeometry(QRect(160,-200,590,294))
		self.frame_principal_Discpacidad.setStyleSheet("QFrame#frame_principal_Discpacidad{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_Discpacidad.move(180,1000)
		self.frame_principal_Discpacidad.setObjectName("frame_principal_Discpacidad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_Discpacidad.setGraphicsEffect(self.shadow)

		
		self.frame_2 = QFrame(self.frame_principal_Discpacidad)
		self.frame_2.setGeometry(QRect(20, 20, 121, 250))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"}")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Discapacidad")

		# Group de discapacidad ========================================================================================================               
		self.groupBox_datosdiscapacidad = QGroupBox(self.frame_principal_Discpacidad)
		self.groupBox_datosdiscapacidad.setGeometry(QRect(160, 20, 410, 251))
		self.groupBox_datosdiscapacidad.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosdiscapacidad.setAlignment(Qt.AlignCenter)
		self.groupBox_datosdiscapacidad.setObjectName("groupBox_datosdiscapacidad")
		self.groupBox_datosdiscapacidad.setTitle("Discapacidad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosdiscapacidad.setGraphicsEffect(self.shadow)
		
		# Descripcion de discapacidad ========================================================================================================             
		self.textEdit_dcrp_discapacidad = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_dcrp_discapacidad.setGeometry(QRect(250, 40, 141, 91))
		self.textEdit_dcrp_discapacidad.setStyleSheet("QTextEdit#textEdit_dcrp_discapacidad{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_discapacidad.setObjectName("textEdit_dcrp_discapacidad")
		self.textEdit_dcrp_discapacidad.setPlaceholderText("Describa la discapacidad...")

		
		self.dcrp_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.dcrp_discapacidad.setGeometry(QRect(245, 20, 151, 16))
		self.dcrp_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_discapacidad.setAlignment(Qt.AlignCenter)
		self.dcrp_discapacidad.setObjectName("dcrp_discapacidad")
		self.dcrp_discapacidad.setText("Describa la discapacidad:")

		# Opciones de discapacidad ========================================================================================================            
		self.label_opciones_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.label_opciones_discapacidad.setGeometry(QRect(10, 20, 221, 16))
		self.label_opciones_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")
		self.label_opciones_discapacidad.setAlignment(Qt.AlignCenter)
		self.label_opciones_discapacidad.setObjectName("label_opciones_discapacidad")
		self.label_opciones_discapacidad.setText("Posee alguna de estas discapacidades:")

		self.checkBox_27_Dscp_motriz =QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_27_Dscp_motriz.setGeometry(QRect(10, 120, 200, 17))
		self.checkBox_27_Dscp_motriz.setText("Discapacidad Motriz")
		self.checkBox_27_Dscp_motriz.setToolTip("Implica una disminución de la movilidad total o parcial \n" 
									"de uno o más miembros del cuerpo, la cual dificulta la realización\n"
									"de actividades motoras convencionales.")
		self.checkBox_27_Dscp_motriz.setObjectName("checkBox_27_Dscp_motriz")
		self.checkBox_27_Dscp_motriz.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_Dscp_auditiva = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_26_Dscp_auditiva.setGeometry(QRect(10, 80, 200, 17))
		self.checkBox_26_Dscp_auditiva.setText("Discapacidad Auditiva")
		self.checkBox_26_Dscp_auditiva.setToolTip("Es un déficit total o parcial en la percepción que se evalúa\n" 
									"por el grado de pérdida de la audición en cada oído")
		self.checkBox_26_Dscp_auditiva.setObjectName("checkBox_26_Dscp_auditiva")
		self.checkBox_26_Dscp_auditiva.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_Dscp_visual = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_25_Dscp_visual.setGeometry(QRect(10, 60, 200, 17))
		self.checkBox_25_Dscp_visual.setText("Discapacidad Visual")
		self.checkBox_25_Dscp_visual.setObjectName("checkBox_25_Dscp_visual")
		self.checkBox_25_Dscp_visual.setToolTip("Es de acuerdo al grado de limitación de la visión, se suele distinguir entre personas ciegas,\n" 
									"que no obtienen información a través del canal visual; y personas con disminución visual,\n"
									"quienes en cambio sí la adquieren mediante dicho canal pero con algún déficit.")
		self.checkBox_25_Dscp_visual.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_Dscp_mental = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_23_Dscp_mental.setGeometry(QRect(10, 40, 220, 17))
		self.checkBox_23_Dscp_mental.setText("Discapacidad Intelectual o mental")
		self.checkBox_23_Dscp_mental.setObjectName("checkBox_23_Dscp_mental")
		self.checkBox_23_Dscp_mental.setToolTip("Las personas con discapacidad intelectual tienen algunas limitaciones\n"
									"para funcionar en su vida diaria; les cuesta más aprender habilidades\n"
									"sociales e intelectuales para acutar en diferentes situaciones.")
		self.checkBox_23_Dscp_mental.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_Dscp_viceral = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_24_Dscp_viceral.setGeometry(QRect(10, 100, 200, 17))
		self.checkBox_24_Dscp_viceral.setText("Discapacidad visceral")
		self.checkBox_24_Dscp_viceral.setObjectName("checkBox_24_Dscp_viceral")
		self.checkBox_24_Dscp_viceral.setToolTip("Las personas con discapacidad visceral son aquellos individuos que, debido a alguna deficiencia \n"
									"en la función de órganos internos, por ejemplo, el cardíaco o el diabético, se encuentran impedidas de \n"
									"desarrollar su vida con total plenitud (aunque no tengan complicaciones en el campo intelectual, \n"
									"en sus funciones sensoriales o motoras)")
		self.checkBox_24_Dscp_viceral.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_otras = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otras.setGeometry(QRect(10, 140, 200, 17))
		self.checkBox_otras.setText("Otra...")
		self.checkBox_otras.setObjectName("checkBox_otras")
		self.checkBox_otras.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# Opciones de medicamentos ========================================================================================================            
		self.label_medicamentos = QLabel(self.groupBox_datosdiscapacidad)
		self.label_medicamentos.setGeometry(QRect(240, 140, 161, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos_dscp = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_si_medicamentos_dscp.setGeometry(QRect(270, 160, 45, 17))
		self.radioButton_si_medicamentos_dscp.setObjectName("radioButton_si_medicamentos_dscp")
		self.radioButton_si_medicamentos_dscp.setText("Si")
		self.radioButton_si_medicamentos_dscp.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos_dscp = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_no_medicamentos_dscp.setGeometry(QRect(330, 160, 45, 17))
		self.radioButton_no_medicamentos_dscp.setObjectName("radioButton_no_medicamentos_dscp")
		self.radioButton_no_medicamentos_dscp.setText("No")
		self.radioButton_no_medicamentos_dscp.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento_dscp = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_medicamento_dscp.setGeometry(QRect(250, 180, 141, 61))
		self.textEdit_medicamento_dscp.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento_dscp.setObjectName("textEdit_medicamento_dscp")
		self.textEdit_medicamento_dscp.setPlaceholderText("Escriba el medicamento...")

		self.label_insumomedico = QLabel(self.groupBox_datosdiscapacidad)
		self.label_insumomedico.setGeometry(QRect(20, 160, 190, 16))
		self.label_insumomedico.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_insumomedico.setAlignment(Qt.AlignCenter)
		self.label_insumomedico.setObjectName("label_insumomedico")
		self.label_insumomedico.setText("Necesita algún insumo medico:")

		self.checkBox_sillarueda = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_sillarueda.setGeometry(QRect(10, 180, 200, 17))
		self.checkBox_sillarueda.setText("Silla de rueda")
		self.checkBox_sillarueda.setObjectName("checkBox_sillarueda")
		self.checkBox_sillarueda.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_muletas = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_muletas.setGeometry(QRect(10, 200, 200, 17))
		self.checkBox_muletas.setText("Muletas")
		self.checkBox_muletas.setObjectName("checkBox_muletas")
		self.checkBox_muletas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_protesis = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_protesis.setGeometry(QRect(10, 220, 200, 17))
		self.checkBox_protesis.setText("Prótesis")
		self.checkBox_protesis.setObjectName("checkBox_protesis")
		self.checkBox_protesis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.checkBox_otros = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otros.setGeometry(QRect(130, 180, 90, 17))
		self.checkBox_otros.setText("Otros...")
		self.checkBox_otros.setObjectName("checkBox_otros")
		self.checkBox_otros.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;}")


		# BOTONES DE LA VENTANA DE DISCAPACIDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+        
		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_discapacidad = QPushButton(self.frame_2)
		self.pushButton_aceptar_discapacidad.setGeometry(QRect(-12, 80, 141, 31))
		self.pushButton_aceptar_discapacidad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_discapacidad.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_discapacidad.setText("Aceptar")
		self.pushButton_aceptar_discapacidad.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_discapacidad.setIconSize(QSize(15,15))
		
		# Boton Cancelar ==========================================================================================             
		self.pushButton_cancelar_discapacidad = QPushButton(self.frame_2)
		self.pushButton_cancelar_discapacidad.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar_discapacidad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_discapacidad.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_discapacidad.setText("Cancelar")
		self.pushButton_cancelar_discapacidad.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_discapacidad.setIconSize(QSize(15,15))

		# Ventana gas bombona		
		self.frame_principal_gas_bombona = QFrame(self)
		self.frame_principal_gas_bombona.setGeometry(QRect(160,-200,380,294))
		self.frame_principal_gas_bombona.setStyleSheet("QFrame#frame_principal_gas_bombona{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_gas_bombona.move(300,1000)
		self.frame_principal_gas_bombona.setObjectName("frame_principal_gas_bombona")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_gas_bombona.setGraphicsEffect(self.shadow)

		# Group de gas bombona ========================================================================================================            
		self.groupBox_gas_bombona = QGroupBox(self.frame_principal_gas_bombona)
		self.groupBox_gas_bombona.setGeometry(QRect(160, 20, 200, 251))
		self.groupBox_gas_bombona.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_gas_bombona.setAlignment(Qt.AlignCenter)
		self.groupBox_gas_bombona.setTitle("                Gas Bombona")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_gas_bombona.setGraphicsEffect(self.shadow)

		# Opciones de bombona========================================================================================================              
		self.label_tipo_cilindro = QLabel(self.groupBox_gas_bombona)
		self.label_tipo_cilindro.setGeometry(QRect(20, 30, 160, 16))
		self.label_tipo_cilindro.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")
		self.label_tipo_cilindro.setAlignment(Qt.AlignCenter)
		self.label_tipo_cilindro.setText("Tipo de cilindro que posee: ")

		self.checkBox_27_pdvsa_gas =QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_27_pdvsa_gas.setGeometry(QRect(50, 135, 200, 17))
		self.checkBox_27_pdvsa_gas.setText("PDVSA Gas")
		self.checkBox_27_pdvsa_gas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_tropiven = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_26_tropiven.setGeometry(QRect(50, 95, 200, 17))
		self.checkBox_26_tropiven.setText("Tropiven")
		self.checkBox_26_tropiven.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_dani_gas = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_25_dani_gas.setGeometry(QRect(50, 75, 200, 17))
		self.checkBox_25_dani_gas.setText("Dani el gas")
		self.checkBox_25_dani_gas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_hermagas = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_23_hermagas.setGeometry(QRect(50, 55, 220, 17))
		self.checkBox_23_hermagas.setText("Hermagas")
		self.checkBox_23_hermagas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_autogas = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_24_autogas.setGeometry(QRect(50, 115, 200, 17))
		self.checkBox_24_autogas.setText("Autogas")

		self.checkBox_24_autogas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# QSpinBox de cantidad de bombonas  ==========================================================================================              
		self.label_num_bombonas = QLabel(self.groupBox_gas_bombona)
		self.label_num_bombonas.setGeometry(QRect(20,170,160,16))
		self.label_num_bombonas.setText("Cuantas bombonas posee:")
		self.label_num_bombonas.setAlignment(Qt.AlignCenter)
		self.label_num_bombonas.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")

		self.num_bombonas = QSpinBox(self.groupBox_gas_bombona)
		self.num_bombonas.setGeometry(QRect(75,200,51,31))
		self.num_bombonas.setMaximum(15)
		self.num_bombonas.setStyleSheet("QSpinBox{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"border-radius: 5px;\n}")

		# Frame menu  ==========================================================================================             
		self.frame_2 = QFrame(self.frame_principal_gas_bombona)
		self.frame_2.setGeometry(QRect(20, 20, 121, 250))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"}")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Gas Bombona")

		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_gas_bombona = QPushButton(self.frame_2)
		self.pushButton_aceptar_gas_bombona.setGeometry(QRect(-12, 80, 141, 31))
		self.pushButton_aceptar_gas_bombona.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_gas_bombona.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_gas_bombona.setText("Aceptar")
		self.pushButton_aceptar_gas_bombona.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_gas_bombona.setIconSize(QSize(15,15))
		
		# Boton Cancelar ==========================================================================================             
		self.pushButton_cancelar_gas_bombona = QPushButton(self.frame_2)
		self.pushButton_cancelar_gas_bombona.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar_gas_bombona.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_gas_bombona.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_gas_bombona.setText("Cancelar")
		self.pushButton_cancelar_gas_bombona.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_gas_bombona.setIconSize(QSize(15,15))


		# Ventana enfermedad
		self.frame_principal_Enfermedad = QFrame(self)
		self.frame_principal_Enfermedad.setGeometry(QRect(190,-200,600,294))
		self.frame_principal_Enfermedad.setStyleSheet("QFrame#frame_principal_Enfermedad{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_Enfermedad.move(180,1000)
		self.frame_principal_Enfermedad.setObjectName("frame_principal_Enfermedad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_Enfermedad.setGraphicsEffect(self.shadow)

		# Group de enfermedad ========================================================================================================             
		self.groupBox_datos_enfermedad = QGroupBox(self.frame_principal_Enfermedad)
		self.groupBox_datos_enfermedad.setGeometry(QRect(160, 20, 421, 251))
		self.groupBox_datos_enfermedad.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datos_enfermedad.setAlignment(Qt.AlignCenter)
		self.groupBox_datos_enfermedad.setObjectName("groupBox_datos_enfermedad")
		self.groupBox_datos_enfermedad.setTitle("Enfermedad")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_enfermedad.setGraphicsEffect(self.shadow)
		
		# Descripcion de enfermedad ========================================================================================================               
		self.textEdit_dcrp_enfermedad = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_dcrp_enfermedad.setGeometry(QRect(265, 40, 141, 91))
		self.textEdit_dcrp_enfermedad.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_enfermedad.setObjectName("textEdit_dcrp_enfermedad")
		self.textEdit_dcrp_enfermedad.setPlaceholderText("Describa la enfermedad...")

		
		self.dcrp_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.dcrp_enfermedad.setGeometry(QRect(260, 20, 151, 16))
		self.dcrp_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_enfermedad.setAlignment(Qt.AlignCenter)
		self.dcrp_enfermedad.setObjectName("dcrp_enfermedad")
		self.dcrp_enfermedad.setText("Describa la enfermedad:")

		# Opciones de enfermedad ========================================================================================================              
		self.label_opciones_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.label_opciones_enfermedad.setGeometry(QRect(10, 20, 241, 16))
		self.label_opciones_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opciones_enfermedad.setAlignment(Qt.AlignCenter)
		self.label_opciones_enfermedad.setObjectName("label_opciones_enfermedad")
		self.label_opciones_enfermedad.setText("Posee alguna de estas enfermedades:")

		self.checkBox_27_cancer = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_27_cancer.setGeometry(QRect(40, 120, 70, 17))
		self.checkBox_27_cancer.setText("Cáncer")
		self.checkBox_27_cancer.setObjectName("checkBox_27_cancer")
		self.checkBox_27_cancer.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26_diabetes = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_26_diabetes.setGeometry(QRect(40, 80, 100, 17))
		self.checkBox_26_diabetes.setText("Diabetes")
		self.checkBox_26_diabetes.setObjectName("checkBox_26_diabetes")
		self.checkBox_26_diabetes.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25_hp_arterial = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_25_hp_arterial.setGeometry(QRect(40, 60, 200, 17))
		self.checkBox_25_hp_arterial.setText("Hipertensión arterial")
		self.checkBox_25_hp_arterial.setObjectName("checkBox_25_hp_arterial")
		self.checkBox_25_hp_arterial.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23_asma = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_23_asma.setGeometry(QRect(40, 40, 70, 17))
		self.checkBox_23_asma.setText("Asma")
		self.checkBox_23_asma.setObjectName("checkBox_23_asma")
		self.checkBox_23_asma.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24_vascular = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_24_vascular.setGeometry(QRect(40, 100, 200, 17))
		self.checkBox_24_vascular.setText("Cardio Vascular")
		self.checkBox_24_vascular.setObjectName("checkBox_24_vascular")
		self.checkBox_24_vascular.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_28_gastritis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_28_gastritis.setGeometry(QRect(40, 140, 70, 17))
		self.checkBox_28_gastritis.setText("Gastritis")
		self.checkBox_28_gastritis.setObjectName("checkBox_28_gastritis")
		self.checkBox_28_gastritis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_29_bronquitis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_29_bronquitis.setGeometry(QRect(40, 160, 100, 17))
		self.checkBox_29_bronquitis.setText("Bronquitis")
		self.checkBox_29_bronquitis.setObjectName("checkBox_29_bronquitis")
		self.checkBox_29_bronquitis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_30_calcu_rinon = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_30_calcu_rinon.setGeometry(QRect(40, 180, 200, 17))
		self.checkBox_30_calcu_rinon.setText("Cálculos de riñón")
		self.checkBox_30_calcu_rinon.setObjectName("checkBox_30_calcu_riñon")
		self.checkBox_30_calcu_rinon.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_31_sinusitis = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_31_sinusitis.setGeometry(QRect(40, 200, 70, 17))
		self.checkBox_31_sinusitis.setText("Sinusitis")
		self.checkBox_31_sinusitis.setObjectName("checkBox_31_sinusitis")
		self.checkBox_31_sinusitis.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_32_otra_enf = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_32_otra_enf.setGeometry(QRect(40, 220, 70, 17))
		self.checkBox_32_otra_enf.setText("Otra...")
		self.checkBox_32_otra_enf.setObjectName("checkBox_32_otra_enf")
		self.checkBox_32_otra_enf.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# Opciones de medicamentos ========================================================================================================            
		self.label_medicamentos = QLabel(self.groupBox_datos_enfermedad)
		self.label_medicamentos.setGeometry(QRect(255, 140, 160, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")       
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos_enfer = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_si_medicamentos_enfer.setGeometry(QRect(280, 160, 41, 17))
		self.radioButton_si_medicamentos_enfer.setObjectName("radioButton_si_medicamentos_enfer")
		self.radioButton_si_medicamentos_enfer.setText("Si")
		self.radioButton_si_medicamentos_enfer.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos_enfer = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_no_medicamentos_enfer.setGeometry(QRect(350, 160, 51, 17))
		self.radioButton_no_medicamentos_enfer.setObjectName("radioButton_no_medicamentos_enfer")
		self.radioButton_no_medicamentos_enfer.setText("No")
		self.radioButton_no_medicamentos_enfer.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento_enfer = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_medicamento_enfer.setGeometry(QRect(265, 180, 141, 61))
		self.textEdit_medicamento_enfer.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento_enfer.setObjectName("textEdit_medicamento_enfer")
		self.textEdit_medicamento_enfer.setPlaceholderText("Escriba el medicamento...")

		self.frame_2_enfer = QFrame(self.frame_principal_Enfermedad)
		self.frame_2_enfer.setGeometry(QRect(20, 20, 121, 251))
		self.frame_2_enfer.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px;\n"
		"}")
		self.frame_2_enfer.setFrameShape(QFrame.StyledPanel)
		self.frame_2_enfer.setFrameShadow(QFrame.Raised)
		self.frame_2_enfer.setObjectName("frame_2_enfer")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2_enfer)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Enfermedad")

		# + BOTONES DE LA VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+        
		
		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_Enfermedad = QPushButton(self.frame_2_enfer)
		self.pushButton_aceptar_Enfermedad.setGeometry(QRect(-12, 80, 141, 31))
		self.pushButton_aceptar_Enfermedad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_Enfermedad.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_Enfermedad.setText("Aceptar")
		self.pushButton_aceptar_Enfermedad.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_Enfermedad.setIconSize(QSize(15,15))
		
		# Boton Cancelar ==========================================================================================             
		self.pushButton_cancelar_Enfermedad = QPushButton(self.frame_2_enfer)
		self.pushButton_cancelar_Enfermedad.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar_Enfermedad.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_Enfermedad.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_Enfermedad.setText("Cancelar")
		self.pushButton_cancelar_Enfermedad.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_Enfermedad.setIconSize(QSize(15,15))

		# Ventana reparacion vivienda
		self.frame_principal_rpr_vv = QFrame(self)
		self.frame_principal_rpr_vv.setGeometry(QRect(190,-200,675,325))
		self.frame_principal_rpr_vv.setStyleSheet("QFrame#frame_principal_rpr_vv{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"}\n"
		"")
		self.frame_principal_rpr_vv.move(180,1000)
		self.frame_principal_rpr_vv.setObjectName("frame_principal_rpr_vv")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_rpr_vv.setGraphicsEffect(self.shadow)

		# GroupBox detalle de reparacion de vivienda ==========================================================================================             
		self.groupBox_dcrp_reparacionvv = QGroupBox(self.frame_principal_rpr_vv)
		self.groupBox_dcrp_reparacionvv.setGeometry(QRect(170, 20, 481, 281))
		self.groupBox_dcrp_reparacionvv.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_dcrp_reparacionvv.setAlignment(Qt.AlignCenter)
		self.groupBox_dcrp_reparacionvv.setObjectName("groupBox_dcrp_reparacionvv")
		self.groupBox_dcrp_reparacionvv.setTitle("Detalles de reparación de vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_dcrp_reparacionvv.setGraphicsEffect(self.shadow)		

		# Descripcion de la reparacion de vivienda ==========================================================================================           
		self.textEdit_dcrp_reparacionvv = QTextEdit(self.groupBox_dcrp_reparacionvv)
		self.textEdit_dcrp_reparacionvv.setGeometry(QRect(260, 50, 211, 90))
		self.textEdit_dcrp_reparacionvv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_reparacionvv.setObjectName("textEdit_dcrp_reparacionvv")
		self.textEdit_dcrp_reparacionvv.setPlaceholderText("Describa la reparación...")

		self.label_26 = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_26.setGeometry(QRect(290, 30, 151, 16))
		self.label_26.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_26.setAlignment(Qt.AlignCenter)
		self.label_26.setObjectName("label_26")
		self.label_26.setText("Describa la reparacion:")

		self.label_linea_blanca = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_linea_blanca.setGeometry(QRect(290, 150, 151, 16))
		self.label_linea_blanca.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_linea_blanca.setAlignment(Qt.AlignCenter)
		self.label_linea_blanca.setObjectName("label_linea_blanca")
		self.label_linea_blanca.setText("Necesita linea blanca:")

		self.checkBox_Lavadora = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Lavadora.setGeometry(QRect(280, 170,100,16))
		self.checkBox_Lavadora.setText("Lavadora")
		self.checkBox_Lavadora.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_Nevera = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Nevera.setGeometry(QRect(380, 170,100,16))
		self.checkBox_Nevera.setText("Nevera")
		self.checkBox_Nevera.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_Cocina = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Cocina.setGeometry(QRect(280, 190,100,16))
		self.checkBox_Cocina.setText("Cocina")
		self.checkBox_Cocina.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")


		self.checkBox_Aireacondicionado = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_Aireacondicionado.setGeometry(QRect(280, 210,160,16))
		self.checkBox_Aireacondicionado.setText("Aire acondicionado")
		self.checkBox_Aireacondicionado.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")
		
		# Opciones de reparacion de vivienda ==========================================================================================             
		self.label_opc_reparacion = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_opc_reparacion.setGeometry(QRect(10, 30, 238, 16))
		self.label_opc_reparacion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opc_reparacion.setAlignment(Qt.AlignCenter)
		self.label_opc_reparacion.setObjectName("label_opc_reparacion")
		self.label_opc_reparacion.setText("Necesita alguna de estas reparaciones:")

		self.checkBox_arreglo_techos = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_arreglo_techos.setGeometry(QRect(20, 60, 180, 17))
		self.checkBox_arreglo_techos.setText("Arreglo o falta de techos")
		self.checkBox_arreglo_techos.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_2_friso = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_2_friso.setGeometry(QRect(20, 80, 180, 17))
		self.checkBox_2_friso.setText("Friso de pared")
		self.checkBox_2_friso.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_3_pintura = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_3_pintura.setGeometry(QRect(20, 100, 180, 17))
		self.checkBox_3_pintura.setText("Falta de pintura ")
		self.checkBox_3_pintura.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_4_arreglo_Pisos = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_4_arreglo_Pisos.setGeometry(QRect(20, 120, 180, 17))
		self.checkBox_4_arreglo_Pisos.setText("Arreglo de pisos")
		self.checkBox_4_arreglo_Pisos.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_5_sistema_electrico = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_5_sistema_electrico.setGeometry(QRect(20, 140, 180, 17))
		self.checkBox_5_sistema_electrico.setText("Sistema eléctrico")
		self.checkBox_5_sistema_electrico.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_6_sistema_agua = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_6_sistema_agua.setGeometry(QRect(20, 160, 180, 17))
		self.checkBox_6_sistema_agua.setText("Sistema de agua")
		self.checkBox_6_sistema_agua.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_7_aguas_servidas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_7_aguas_servidas.setGeometry(QRect(20, 180, 180, 17))
		self.checkBox_7_aguas_servidas.setText("Sistema de aguas servida")
		self.checkBox_7_aguas_servidas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_8_fatla_ventanas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_8_fatla_ventanas.setGeometry(QRect(20, 200, 180, 17))
		self.checkBox_8_fatla_ventanas.setText("Falta de ventanas")
		self.checkBox_8_fatla_ventanas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_9_falta_puertas = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_9_falta_puertas.setGeometry(QRect(20, 220, 180, 17))
		self.checkBox_9_falta_puertas.setText("Falta de puertas")
		self.checkBox_9_falta_puertas.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_10_otras_rpr = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_10_otras_rpr.setGeometry(QRect(20, 240, 180, 17))
		self.checkBox_10_otras_rpr.setText("Otras...")
		self.checkBox_10_otras_rpr.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		# Botones para guardar y ver fotos  ==========================================================================================              
		self.pushButton_anexarfotos = QPushButton(self.frame_principal_rpr_vv)
		self.pushButton_anexarfotos.setGeometry(QRect(490, 255, 101, 31))
		self.pushButton_anexarfotos.setStyleSheet(
		"QPushButton{\n"
		"border:0px;\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: #ffffff;\n"
		"border-radius: 5px;\n"
		"}\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:#ffffff;\n"
		"font-size: 12px;\n"
		"}")        
		self.pushButton_anexarfotos.setObjectName("pushButton_anexarfotos")
		self.pushButton_anexarfotos.setText("Anexar fotos")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_anexarfotos.setGraphicsEffect(self.shadow)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.frame_2 = QFrame(self.frame_principal_rpr_vv)
		self.frame_2.setGeometry(QRect(20, 20, 121, 281))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius: 45px\n"
		"}")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_2.setGraphicsEffect(self.shadow)

		self.label_25 = QLabel(self.frame_2)
		self.label_25.setGeometry(QRect(-10, 10, 141, 20))
		self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"")
		self.label_25.setAlignment(Qt.AlignCenter)
		self.label_25.setObjectName("label_25")
		self.label_25.setText("Vivienda")

		# Boton Aceptar ==========================================================================================              
		self.pushButton_aceptar_rpr_vv = QPushButton(self.frame_2)
		self.pushButton_aceptar_rpr_vv.setGeometry(QRect(-12, 70, 141, 31))
		self.pushButton_aceptar_rpr_vv.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_aceptar_rpr_vv.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar_rpr_vv.setText("Aceptar")
		self.pushButton_aceptar_rpr_vv.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_rpr_vv.setIconSize(QSize(15,15))

		# Boton cancelar ==========================================================================================             
		self.pushButton_cancelar_rpr_vv = QPushButton(self.frame_2)
		self.pushButton_cancelar_rpr_vv.setGeometry(QRect(-10, 110, 141, 31))
		self.pushButton_cancelar_rpr_vv.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_cancelar_rpr_vv.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar_rpr_vv.setText("Cancelar")
		self.pushButton_cancelar_rpr_vv.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_rpr_vv.setIconSize(QSize(15,15))
		

		# Ventana de reparacion vivienda
		self.frame_principal_visualizador = QFrame(self)
		self.frame_principal_visualizador.setGeometry(QRect(100,-200,770,410))
		self.frame_principal_visualizador.setStyleSheet("QFrame#frame_principal_visualizador{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius: 30px;\n"
		"border: 5px solid #ffffff;\n"
		"}\n"
		"")
		self.frame_principal_visualizador.move(145,1000)
		self.frame_principal_visualizador.setObjectName("frame_principal_visualizador")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_visualizador.setGraphicsEffect(self.shadow)

		self.frame_3 = QFrame(self.frame_principal_visualizador)
		self.frame_3.setGeometry(QRect(20, 20, 121, 370))
		self.frame_3.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px;\n"
		"}")
		self.frame_3.setFrameShape(QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_3.setGraphicsEffect(self.shadow)

		self.label_28 = QLabel(self.frame_3)
		self.label_28.setGeometry(QRect(-10, 10, 141, 20))
		self.label_28.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"")
		self.label_28.setAlignment(Qt.AlignCenter)
		self.label_28.setObjectName("label_28")
		self.label_28.setText("Cargar Foto")

		# Parte del visualizador donde se mostrara la imagen ==========================================================================================             
		self.frame_visualizador = QFrame(self.frame_principal_visualizador)
		self.frame_visualizador.setGeometry(QRect(160, 20, 591, 371))
		self.frame_visualizador.setStyleSheet("QFrame{\n"
		"background-color:#E5E7EE;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.frame_visualizador.setFrameShape(QFrame.StyledPanel)
		self.frame_visualizador.setFrameShadow(QFrame.Raised)
		self.frame_visualizador.setObjectName("frame")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_visualizador.setGraphicsEffect(self.shadow)

		# Label de la miniatura de imagen ==========================================================================================            
		# Miniatura_1
		self.label_miniatura_1 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_1.setGeometry(QRect(20, 20, 171, 121))
		self.label_miniatura_1.setStyleSheet("QLabel{\n"
		"background-color: #12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_1.setText("Click para anexar")
		self.label_miniatura_1.setObjectName("label_miniatura_1")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_1.setGraphicsEffect(self.shadow)
		self.label_miniatura_1.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_1_nombre.setGeometry(QRect(180,140,170,16))
		self.label_miniatura_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_2
		self.label_miniatura_2 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_2.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2.setGeometry(QRect(210, 20, 171, 121))
		self.label_miniatura_2.setStyleSheet("QLabel{\n"
		"background-color: #12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_2.setText("Click para anexar")
		self.label_miniatura_2.setObjectName("label_miniatura_2")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_2.setGraphicsEffect(self.shadow)
		self.label_miniatura_2_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_2_nombre.setGeometry(QRect(370,140,170,16))
		self.label_miniatura_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")


		# Miniatura_3
		self.label_miniatura_3 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_3.setGeometry(QRect(400, 20, 171, 121))
		self.label_miniatura_3.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_3.setText("Click para anexar")
		self.label_miniatura_3.setObjectName("label_miniatura_3")
		self.label_miniatura_3.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_3.setGraphicsEffect(self.shadow)
		self.label_miniatura_3_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_3_nombre.setGeometry(QRect(560,140,171,16))
		self.label_miniatura_3_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_3_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")
		
		# Miniatura_4
		self.label_miniatura_4 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_4.setGeometry(QRect(20, 200, 171, 121))
		self.label_miniatura_4.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_4.setText("Click para anexar")
		self.label_miniatura_4.setObjectName("label_miniatura_4")
		self.label_miniatura_4.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_4.setGraphicsEffect(self.shadow)
		self.label_miniatura_4_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_4_nombre.setGeometry(QRect(180,320,171,16))
		self.label_miniatura_4_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_4_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_5
		self.label_miniatura_5 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_5.setGeometry(QRect(210, 200, 171, 121))
		self.label_miniatura_5.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_5.setText("Click para anexar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_5.setGraphicsEffect(self.shadow)
		self.label_miniatura_5.setObjectName("label_miniatura_5")
		self.label_miniatura_5.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_5.setObjectName("label_miniatura_5_nombre")
		self.label_miniatura_5_nombre.setGeometry(QRect(370,320,171,16))
		self.label_miniatura_5_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Miniatura_6
		self.label_miniatura_6 = QLabelClickable(self.frame_visualizador)
		self.label_miniatura_6.setGeometry(QRect(400, 200, 171, 121))
		self.label_miniatura_6.setStyleSheet("QLabel{\n"
		"background-color:#12191D;\n"
		"color:#ffffff;\n"
		"border-radius: 5px;\n"
		"font-size: 18px;\n"
		"}\n"
		"QLabel:hover{\n"
		"border: 1px solid  #ffffff;\n"
		"}")
		self.label_miniatura_6.setText("Click para anexar")
		self.label_miniatura_6.setObjectName("label_miniatura_6")
		self.label_miniatura_6.setAlignment(Qt.AlignCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(50)
		self.label_miniatura_6.setGraphicsEffect(self.shadow)
		self.label_miniatura_6_nombre = QLabel(self.frame_principal_visualizador)
		self.label_miniatura_6_nombre.setGeometry(QRect(560,320,171,16))
		self.label_miniatura_6_nombre.setAlignment(Qt.AlignCenter)

		self.label_miniatura_6_nombre.setStyleSheet("QLabel{\n"
		"background-color: #ffffff;\n"
		"color: #12191D;\n"
		"border-radius: 8px;\n"
		""
		"}")

		# Boton eliminar de miniatura_1  ==========================================================================================             
		self.pushButton_eliminar = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar.setGeometry(QRect(70, 150, 71, 21))
		self.pushButton_eliminar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar.setObjectName("pushButton_eliminar")
		self.pushButton_eliminar.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_2 ==========================================================================================             
		self.pushButton_eliminar_2 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_2.setGeometry(QRect(260, 150, 71, 21))
		self.pushButton_eliminar_2.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_2.setObjectName("pushButton_eliminar_2")
		self.pushButton_eliminar_2.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_2.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_3  ==========================================================================================             
		self.pushButton_eliminar_3 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_3.setGeometry(QRect(450, 150, 71, 21))
		self.pushButton_eliminar_3.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_3.setObjectName("pushButton_eliminar_3")
		self.pushButton_eliminar_3.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_3.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_4 ==========================================================================================             
		self.pushButton_eliminar_4 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_4.setGeometry(QRect(70, 330, 71, 21))
		self.pushButton_eliminar_4.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_4.setObjectName("pushButton_eliminar_4")
		self.pushButton_eliminar_4.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_4.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_5  ==========================================================================================             
		self.pushButton_eliminar_5 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_5.setGeometry(QRect(260, 330, 71, 21))
		self.pushButton_eliminar_5.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_5.setObjectName("pushButton_eliminar_5")
		self.pushButton_eliminar_5.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_5.setGraphicsEffect(self.shadow)

		# Boton eliminar de miniatura_6  ==========================================================================================             
		self.pushButton_eliminar_6 = QPushButton(self.frame_visualizador)
		self.pushButton_eliminar_6.setGeometry(QRect(450, 330, 71, 21))
		self.pushButton_eliminar_6.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"font-size: 12px;\n"
		"background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_eliminar_6.setObjectName("pushButton_eliminar_6")
		self.pushButton_eliminar_6.setText("Eliminar")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_eliminar_6.setGraphicsEffect(self.shadow)

		# Boton aceptar  ==========================================================================================              
		self.pushButton_visualizador_aceptar = QPushButton(self.frame_3)
		self.pushButton_visualizador_aceptar.setGeometry(QRect(-2, 70, 121, 31))
		self.pushButton_visualizador_aceptar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_visualizador_aceptar.setText("Guardar")
		self.pushButton_visualizador_aceptar.setIcon(QIcon(":/Icono_guardar/Imagenes-iconos/Guardar_blanco.png"))
		self.pushButton_visualizador_aceptar.setIconSize(QSize(18,18))

		# Boton cancelar  ==========================================================================================             
		self.pushButton_visualizador_cancelar = QPushButton(self.frame_3)
		self.pushButton_visualizador_cancelar.setGeometry(QRect(0, 110, 121, 31))
		self.pushButton_visualizador_cancelar.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.pushButton_visualizador_cancelar.setText("Cancelar")
		self.pushButton_visualizador_cancelar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_visualizador_cancelar.setIconSize(QSize(15,15))

		# Eventos==========================================================================================             
		self.label_miniatura_1.clicked.connect(self.Cargar)
		self.label_miniatura_2.clicked.connect(self.Cargar_1)
		self.label_miniatura_3.clicked.connect(self.Cargar_2)
		self.label_miniatura_4.clicked.connect(self.Cargar_3)
		self.label_miniatura_5.clicked.connect(self.Cargar_4)
		self.label_miniatura_6.clicked.connect(self.Cargar_5)

		self.pushButton_eliminar.clicked.connect(self.Eliminar)
		self.pushButton_eliminar_2.clicked.connect(self.Eliminar_1)
		self.pushButton_eliminar_3.clicked.connect(self.Eliminar_2)
		self.pushButton_eliminar_4.clicked.connect(self.Eliminar_3)
		self.pushButton_eliminar_5.clicked.connect(self.Eliminar_4)
		self.pushButton_eliminar_6.clicked.connect(self.Eliminar_5)

		# Lines
		# Line bajo Nombre-Apellido =====================================================================================   
		self.line = QFrame(self.groupBox_datosGnr)
		self.line.setGeometry(QRect(10, 110, 311, 16))
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)
		self.line.setObjectName("line")
		
		# Line bajo cedula ==============================================================================================       
		self.line_5 = QFrame(self.groupBox_datosGnr)
		self.line_5.setGeometry(QRect(10, 165, 141, 16))
		self.line_5.setFrameShape(QFrame.HLine)
		self.line_5.setFrameShadow(QFrame.Sunken)
		self.line_5.setObjectName("line_5")            

		# Line bajo telefono ===========================================================================================         
		self.line_3 = QFrame(self.groupBox_datosGnr)
		self.line_3.setGeometry(QRect(180, 190, 141, 16))
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)
		self.line_3.setObjectName("line_3")

		# Line bajo genero ========================================================================================================       
		self.line_2 = QFrame(self.groupBox_datosGnr)
		self.line_2.setGeometry(QRect(10, 220, 141, 16))
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)
		self.line_2.setObjectName("line_2")
	   
		# Line bajo edad ========================================================================================================         
		self.line_8 = QFrame(self.groupBox_datosGnr)
		self.line_8.setGeometry(QRect(180, 245, 141, 16))
		self.line_8.setFrameShape(QFrame.HLine)
		self.line_8.setFrameShadow(QFrame.Sunken)
		self.line_8.setObjectName("line_8")

		# Line bajo fecha de nacimiento ==========================================================================================      
		self.line_4 = QFrame(self.groupBox_datosGnr)
		self.line_4.setGeometry(QRect(10, 275, 141, 16))
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)
		self.line_4.setObjectName("line_4")
	   
		# Line bajo profesion u oficio ==========================================================================================      
		self.line_6 = QFrame(self.groupBox_datosGnr)
		self.line_6.setGeometry(QRect(10, 330, 141, 16))
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)
		self.line_6.setObjectName("line_6")

		# Line bajo nivel de instruccion ==========================================================================================      
		self.line_7 = QFrame(self.groupBox_datosGnr)
		self.line_7.setGeometry(QRect(10, 385, 141, 16))
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)
		self.line_7.setObjectName("line_7")       
		
		# Line bajo opciones checkbox ==========================================================================================      
		self.line_9 = QFrame(self.groupBox_datosGnr)
		self.line_9.setGeometry(QRect(180, 375, 141, 16))
		self.line_9.setFrameShape(QFrame.HLine)
		self.line_9.setFrameShadow(QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		
		# Line bajo estado civil ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(10, 440, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")

		# Line bajo parentesco ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(180, 430, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")

		# Line bajo direccion ==========================================================================================      
		self.line_10 = QFrame(self.groupBox_datosUb)
		self.line_10.setGeometry(QRect(193, 110, 161, 16))
		self.line_10.setFrameShape(QFrame.HLine)
		self.line_10.setFrameShadow(QFrame.Sunken)
		self.line_10.setObjectName("line_10")

		# Line bajo metros cuadrados ==========================================================================================      
		self.line_11 = QFrame(self.groupBox_datos_Vv)
		self.line_11.setGeometry(QRect(15, 63, 141, 16))
		self.line_11.setFrameShape(QFrame.HLine)
		self.line_11.setFrameShadow(QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		
		# Line bajo servicios que posee ==========================================================================================      
		self.line_12 = QFrame(self.groupBox_datos_Vv)
		self.line_12.setGeometry(QRect(180, 115, 181, 20))
		self.line_12.setFrameShape(QFrame.HLine)
		self.line_12.setFrameShadow(QFrame.Sunken)
		self.line_12.setObjectName("line_12")

		self.frame_nv_user = QFrame(self)
		self.frame_nv_user.setGeometry(QRect(20, 10, 121, 493))
		self.frame_nv_user.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"\n"
		"}")
		self.frame_nv_user.setFrameShape(QFrame.StyledPanel)
		self.frame_nv_user.setFrameShadow(QFrame.Raised)
		self.frame_nv_user.setObjectName("frame_nv_user")

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame_nv_user.setGraphicsEffect(self.shadow)


		self.label_13 = QLabel(self.frame_nv_user)
		self.label_13.setGeometry(QRect(25, 10, 141,20))
		self.label_13.setText("USUARIO")    
		self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"border-radius:6px\n"
		"")
		
		# Boton registrar ==========================================================================================            
		self.Button_register_user = QPushButton(self.frame_nv_user)
		self.Button_register_user.setGeometry(QRect(0, 80, 121, 31))
		self.Button_register_user.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_register_user.setObjectName("Button_register_user")
		self.Button_register_user.setText("Registrar")
		self.Button_register_user.setIcon(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"))
		self.Button_register_user.setIconSize(QSize(20,20))

		# Boton cancelar ==========================================================================================             
		self.Button_cancelar_user = QPushButton(self.frame_nv_user)
		self.Button_cancelar_user.setGeometry(QRect(0, 120, 121, 31))
		self.Button_cancelar_user.setStyleSheet("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"\n"
		"}")
		self.Button_cancelar_user.setObjectName("Button_cancelar_user")
		self.Button_cancelar_user.setText("Cancelar")   
		self.Button_cancelar_user.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancelar_user.setIconSize(QSize(17,17)) 

		# Eventos
		self.Button_register_user.clicked.connect(self.Verificar_datos)
		self.checkBox_2_discapacidad.clicked.connect(self.Descripcion_discapacidad)
		self.radioButton_rp_si.clicked.connect(self.Descripcion_reparacion)
		self.checkBox_3_enfer.clicked.connect(self.Descripcion_enfermedad)
		self.checkBox_gasbombona.clicked.connect(self.Window_gas_bombona)
		self.Button_cancelar_user.clicked.connect(self.cerrar_nv_user)
		self.pushButton_aceptar_discapacidad.clicked.connect(self.Aceptar_discapacidad)
		self.pushButton_cancelar_discapacidad.clicked.connect(self.Cancelar_Discapacidad)
		self.pushButton_aceptar_Enfermedad.clicked.connect(self.Aceptar_enfermedad)
		self.pushButton_cancelar_Enfermedad.clicked.connect(self.Cancelar_enfermedad)
		self.pushButton_aceptar_gas_bombona.clicked.connect(self.Aceptar_gas_bombona)
		self.pushButton_cancelar_gas_bombona.clicked.connect(self.Cancelar_gas_bombona)
		self.pushButton_aceptar_rpr_vv.clicked.connect(self.Aceptar_rpr_vv)
		self.pushButton_cancelar_rpr_vv.clicked.connect(self.Cancelar_rpr_vv)
		self.pushButton_anexarfotos.clicked.connect(self.Mostrar_visualizador)
		self.pushButton_visualizador_aceptar.clicked.connect(self.Aceptar_visualizador)
		self.pushButton_visualizador_cancelar.clicked.connect(self.Cancelar_visualizador)
		self.comboBox_profesion.currentIndexChanged.connect(self.Estudiante)
		self.Button_aceptar_estudiante.clicked.connect(self.Aceptar_estudiante)
		self.Button_cancelar_estudiante.clicked.connect(self.Cancelar_estudiante)
	
	def cerrar_nv_user(self):
		cerrar_user = QMessageBox(self)
		cerrar_user.setWindowTitle("Cancelar")
		cerrar_user.setIcon(QMessageBox.Question)
		cerrar_user.setText("¿Estás seguro que desea cancelar?")
		botonSalir_user = cerrar_user.addButton("Si", QMessageBox.YesRole)
		botonCancelar_user = cerrar_user.addButton("No", QMessageBox.NoRole)

		cerrar_user.exec_()

		if cerrar_user.clickedButton() == botonSalir_user:
			self.close()
		else:
			pass

	# Abrir ventana de gas_bobombona ==========================================================================================                 
	def Window_gas_bombona(self):
		if self.checkBox_gasbombona.isChecked():
			self.Mostrar_gas_bombona()
		else:
			None

	# Abrir ventana de Enfermedad ==========================================================================================                
	def Descripcion_enfermedad(self):
		if self.checkBox_3_enfer.isChecked():
			self.Mostrar_Enfermedad()
		else:
			None

	# Funcion  abrir ventana descripcion reparacion de vivienda ==========================================================================================                
	def Descripcion_reparacion(self):
		if self.radioButton_rp_si.isChecked():
			self.Mostrar_rpr_vv()
		else:
			None

	# Funcion abrir ventana descripcion de discapacidad ==========================================================================================               
	def Descripcion_discapacidad(self):
		if self.checkBox_2_discapacidad.isChecked():
			self.Mostrar_Discapacidad()
		else:
			None

	# Funcion ventana estudiante accion Aceptar ==========================================================================================            
	def Aceptar_estudiante(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_estudiante()
		else:
			pass    

	# Funcion ventana estudiante accion Cancelar ==========================================================================================           
	def Cancelar_estudiante(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.checkbox_primaria.setChecked(False)
			self.checkbox_bachillerato.setChecked(False)
			self.checkbox_universitario.setChecked(False)
			self.checkbox_especializacion.setChecked(False)
			self.texedit_donde_estudia.clear()
			self.texedit_carrera.clear()
			self.Ocultar_estudiante()
		else:
			pass    

	# Funcion para la ventana de visualizador de fotos accion de Aceptar ==========================================================================================             
	def Aceptar_visualizador(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_visualizador()
		else:
			pass    

	# Funcion para la ventana de reparacion vivienda accion de Cancelar ==========================================================================================              
	def Cancelar_visualizador(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.label_miniatura_1.clear()
			self.label_miniatura_1.setText("Click para anexar")
			self.label_miniatura_1_nombre.clear()
			self.label_miniatura_2.clear()
			self.label_miniatura_2.setText("Click para anexar")
			self.label_miniatura_2_nombre.clear()
			self.label_miniatura_3.clear()
			self.label_miniatura_3.setText("Click para anexar")
			self.label_miniatura_3_nombre.clear()
			self.label_miniatura_4.clear()
			self.label_miniatura_4.setText("Click para anexar")
			self.label_miniatura_4_nombre.clear()
			self.label_miniatura_5.clear()
			self.label_miniatura_5.setText("Click para anexar")
			self.label_miniatura_5_nombre.clear()
			self.label_miniatura_5.clear()
			self.label_miniatura_5.setText("Click para anexar")
			self.label_miniatura_5_nombre.clear()
			self.label_miniatura_6.clear()
			self.label_miniatura_6.setText("Click para anexar")
			self.label_miniatura_6_nombre.clear()
			self.Ocultar_visualizador()
		else:
			pass    

	# Funcion para la ventana de reparacion de vivienda accion de Aceptar ==========================================================================================            
	def Aceptar_rpr_vv(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_rpr_vv()
		else:
			pass    

	# Funcion para la ventana de reparacion vivienda accion de Cancelar ==========================================================================================              
	def Cancelar_rpr_vv(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.textEdit_dcrp_reparacionvv.clear()
			self.checkBox_arreglo_techos.setChecked(False)
			self.checkBox_2_friso.setChecked(False)
			self.checkBox_3_pintura.setChecked(False)
			self.checkBox_4_arreglo_Pisos.setChecked(False)
			self.checkBox_5_sistema_electrico.setChecked(False)
			self.checkBox_6_sistema_agua.setChecked(False)
			self.checkBox_7_aguas_servidas.setChecked(False)
			self.checkBox_8_fatla_ventanas.setChecked(False)
			self.checkBox_9_falta_puertas.setChecked(False)
			self.checkBox_10_otras_rpr.setChecked(False)
			self.checkBox_Lavadora.setChecked(False)
			self.checkBox_Nevera.setChecked(False)
			self.checkBox_Cocina.setChecked(False)
			self.checkBox_Aireacondicionado.setChecked(False)

			self.Ocultar_rpr_vv()
		else:
			pass    

	# Funcion para la ventana de gas bombona accion de Aceptar ==========================================================================================           
	def Aceptar_gas_bombona(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_gas_bombona()
		else:
			pass    

	# Funcion para la ventana de gas bombona accion de Cancelar ==========================================================================================              
	def Cancelar_gas_bombona(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.checkBox_27_pdvsa_gas.setChecked(False)
			self.checkBox_26_tropiven.setChecked(False)
			self.checkBox_25_dani_gas.setChecked(False)
			self.checkBox_23_hermagas.setChecked(False)
			self.checkBox_24_autogas.setChecked(False)
			self.num_bombonas.setValue(0)
			self.checkBox_gasbombona.setChecked(False)

			self.Ocultar_gas_bombona()
		else:
			pass    

	# Funcion para la ventana de Enfermedad accion de Aceptar ==========================================================================================            
	def Aceptar_enfermedad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Enfermedad()
		else:
			pass    

	# Funcion para la ventana de Enfermedad accion de Cancelar ==========================================================================================           
	def Cancelar_enfermedad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.textEdit_dcrp_enfermedad.clear()
			self.textEdit_medicamento_enfer.clear()
			self.checkBox_27_cancer.setChecked(False)
			self.checkBox_26_diabetes.setChecked(False)
			self.checkBox_25_hp_arterial.setChecked(False)
			self.checkBox_23_asma.setChecked(False)
			self.checkBox_24_vascular.setChecked(False)
			self.checkBox_28_gastritis.setChecked(False)        
			self.checkBox_29_bronquitis.setChecked(False)
			self.checkBox_30_calcu_rinon.setChecked(False)
			self.checkBox_31_sinusitis.setChecked(False)
			self.checkBox_32_otra_enf.setChecked(False)
			self.checkBox_3_enfer.setChecked(False)

			self.Ocultar_Enfermedad()
		else:
			pass    	

	# Funcion para la ventana de discapacidad accion de aceptar ==========================================================================================              
	def Aceptar_discapacidad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Ocultar_Discapacidad()
		else:
			pass

	# Funcion para la ventana de discapacidad accion de cancelar ==========================================================================================             
	def Cancelar_Discapacidad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.textEdit_dcrp_discapacidad.clear()
			self.checkBox_27_Dscp_motriz.setChecked(False)
			self.checkBox_26_Dscp_auditiva.setChecked(False)
			self.checkBox_25_Dscp_visual.setChecked(False)
			self.checkBox_23_Dscp_mental.setChecked(False)
			self.checkBox_24_Dscp_viceral.setChecked(False)
			self.checkBox_otras.setChecked(False)
			self.textEdit_medicamento_dscp.clear()
			self.checkBox_sillarueda.setChecked(False)
			self.checkBox_muletas.setChecked(False)
			self.checkBox_protesis.setChecked(False)
			self.checkBox_otros.setChecked(False)
			self.checkBox_2_discapacidad.setChecked(False)

			self.Ocultar_Discapacidad()
		else:
			pass

	# Funcion para verificar datos antes de crear la basde de datos ==========================================================================================              
	def Verificar_datos(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon(':/Logo_vesor/Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Verificar Datos")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		button_si.setIconSize(QSize(13,13))
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		button_no.setIconSize(QSize(13,13))
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")
		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")
		if (msg.exec_() == QMessageBox.Yes):
			self.Creater_base_datos()
			self.New_user()
		else:
			pass

	# Funcion crear nuevo usuario ==========================================================================================              
	def Creater_base_datos(self):
			if not QFile.exists("Base de datos"):
				makedirs("Base de datos")
			if QFile.exists("Base de datos"):
				if QFile.exists('Base de datos/DB_VESOR_USER_DATOSGENERALES.db'):
					None
				else:
					try:
						with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db') as db:
							cursor = db.cursor()
						cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_DT_GNR (ID INTEGER PRIMARY KEY,PRIMER_NOMBRE TEXT,"

																			"SEGUNDO_NOMBRE TEXT, PRIMER_APELLIDO TEXT, SEGUNDO_APELLIDO TEXT,"

																			"CEDULA TEXT, GENERO TEXT, TELEFONO_PRINCIPAL TEXT," 

																			"TELEFONO_SECUNDARIO TEXT, FECHA_NACIMIENTO TEXT, EDAD TEXT,"

																			"PROFESION_OFICIO TEXT, NIVEL_INSTRUCCION TEXT, PARENTESCO TEXT,"

																			"ESTADO_CIVIL TEXT, INSCRITO_REP TEXT, CORREO_ELECTRONICO TEXT,"

																			"PENSIONADO TEXT, DISCAPACIDAD TEXT, DISCAPACIDAD_MOTRIZ TEXT, DISCAPACIDAD_AUDITIVA TEXT,"

																			"DISCAPACIDAD_VISUAL TEXT, DISCAPACIDAD_INTELECTUAL TEXT, DISCAPACIDAD_VISCERAL TEXT,"

																			"DISCAPACIDAD_OTRAS TEXT, SILLA_DE_RUEDA TEXT, MULETAS TEXT, PROTESIS TEXT, INSUMO_OTROS TEXT,"

																			"DESCRIBA_DISCAPACIDAD TEXT, TOMA_MEDICAMENTO TEXT, DESCRIBA_MEDICAMENTO TEXT,"
																			
																			"ENFERMEDAD_CANCER TEXT, ENFERMEDAD_DIABETES TEXT, ENFERMEDAD_HIPERTENSION TEXT, ENFERMEDAD_ASMA TEXT,"

																			"ENFERMEDAD_CARDIO TEXT, ENFERMEDAD_GASTRITIS TEXT, ENFERMEDAD_BRONQUITIS TEXT, ENFERMEDAD_CALCULOS TEXT,"

																			"ENFERMEDAD_SINUSITIS TEXT, ENFERMEDAD_OTRAS TEXT,"

																			"DESCRIBA_ENFERMEDAD TEXT, TOMA_MEDICAMENTO_ENF TEXT, DESCRIBA_MEDICAMENTO_ENF TEXT,"

																			"EMBARAZADA TEXT, LACTANTE TEXT, NIVEL_DE_ESTUDIO TEXT, CARRERA_CURSANDO TEXT, DONDE_ESTUDIA TEXT, FECHA TEXT, HORA TEXT,"

																			"MODIFICACION TEXT, N_VIVIENDA TEXT)")

						db.commit()     
						cursor.close()
						db.close()

					except Exception as e:
						print(e)
						QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
											 QMessageBox.Ok)
				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db') as db:
						cursor = db.cursor()

					cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_UBCGEOG (ID INTEGER PRIMARY KEY,ESTADO TEXT, MUNICIPIO TEXT,PARROQUIA TEXT,"
																					"DIRECCION TEXT)")

					db.commit()     
					cursor.close()
					db.close()

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
										 QMessageBox.Ok)
				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db') as db:
						cursor = db.cursor()
						cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_DT_VV(ID INTEGER PRIMARY KEY,METROS_CUADRADOS TEXT, DESCRIPCION TEXT, NECESITA_REPARACION TEXT,"
									"REPARACION_TECHOS TEXT, REPARACION_PARED TEXT, REPARACION_PINTURA TEXT,REPARACION_PISOS TEXT,"
									"REPARACION_ELECTRICO TEXT, REPARACION_AGUA TEXT, REPARACION_AGUA_SERVIDAS TEXT, REPARACION_VENTANAS TEXT,"
									"REPARACION_PUERTARS TEXT, REPARACION_OTRAS TEXT,"
									"AGUA_POTABLE TEXT, AGUA_SERVIDAS TEXT, GAS_DIRECTO TEXT, GAS_BOMBONA TEXT,"
									"TIPO_DE_CILINDRO TEXT, CANTIDAD_DE_BOMBONAS INT,"
									"INTERNET TEXT, ElECTRICIDAD TEXT,"
									"TELEFONO_FIJO TEXT, DESCRIPCION_REPARACION TEXT, NECESITA_LINEBLANCA TEXT,"
									"FOTO_ANEXADA1 BLOB, FOTO_ANEXADA2 BLOB, FOTO_ANEXADA3 BLOB, FOTO_ANEXADA4 BLOB, FOTO_ANEXADA5,FOTO_ANEXADA6 BLOB)")

					db.commit()     
					cursor.close()
					db.close()
					
				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
										 QMessageBox.Ok)
				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_PROT_SOCIAL.db') as db:
						cursor = db.cursor()

					cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_PROT_SOCIAL(ID INTEGER PRIMARY KEY,HOGARES_PATRIA TEXT, AMOR_MAYOR TEXT,JOSE_GREGORIO TEXT,"
									"PARTO_HUMANIZADO, CHAMBA_JUVENIL TEXT, SOMOS_VENEZUELA TEXT, FRENTE_MIRANDA TEXT, JPSUV TEXT)")

					db.commit()     
					cursor.close()
					db.close()

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
										 QMessageBox.Ok)
			else:
				None

	def New_user(self):
		# Datos Generales
		nombre_1 = self.lineEdit_1_nombre.text() 
		nombre_2 = self.lineEdit_2_nombre.text()
		apellido_1 = self.lineEdit_1_Apellido.text()
		apellido_2 = self.lineEdit_2_Apellido.text()
		cedula_identidad = self.lineEdit_cedula.text()
		telefono_princ = self.lineEdit_1_tlf.text()
		telefono_secund = self.lineEdit_2_tlf.text()
		genero = self.comboBox_genero.currentText()
		edad = self.lineEdit_edad.text()
		fecha_Nacimiento = self.dateEdit_nacimiento.text()
		profesion_oficio = self.comboBox_profesion.currentText()
		nivel_instruccion = self.comboBox_nvl_instruccion.currentText()
		parentesco = self.comboBox_parentesco.currentText()
		opcion_pensionado = self.pensionado()
		opcion_discapacidad = self.si_posee_discapacidad
		opcion_enfermedad = self.checkBox_3_enfer.text()
		opcion_embarazada = self.opcion_de_embarazada()
		opcion_lactante = self.opcion_de_lactante()
		estado_civil = self.comboBox_estadocivil.currentText()
		inscrito_rep = self.RadioButton_rep()
		correo_electronico = self.lineEdit_correo.text()

		# Ubicacion geografica          
		estado = self.lineEdit_estado.text()
		municipio = self.lineEdit_municipio.text()
		parroquia = self.lineEdit_parroquia.text()
		numero_vivienda = self.lineEdit_N_vivienda.text()
		direccion = self.textEdit_direccion.toPlainText()

		# Datos de la vivienda
		metros_cuadrados = self.lineEdit_M2.text()
		descripcion_vivienda = self.textEdit_dcrp_vv.toPlainText()
		reparaciones = self.RadioButton_reparacion()
		servicio_aguapotable = self.CheckBox_aguapotable()
		servicio_aguaservidas = self.CheckBox_aguaservidas()
		servicio_gasdirecto = self.CheckBox_gasdirecto()
		servicio_gasbombona = self.gas_bombona_servicio()
		servicio_internet = self.CheckBox_internet()
		servicio_electricidad = self.CheckBox_electricidad()
		servicio_tlf_fijo = self.CheckBox_telefonofijo()

		# Proteccion Social
		hogaresdelapatria = self.CheckBox_hogaresdelapatria()
		amormayor = self.CheckBox_amormayor()
		josegregorio = self.CheckBox_josegregorio()
		partohumanizado = self.CheckBox_partohumanizado()

		chambajuvenil = self.CheckBox_chambajuvenil()
		somosvenezuela = self.CheckBox_somosvenezuela()
		frentemiranda = self.CheckBox_frentemiranda()
		jpsuv = self.CheckBox_jpsuv()

		# Ventana de discapacidad
		discapacidad = self.si_posee_discapacidad()
		descripcion_discapacidad = self.textEdit_dcrp_discapacidad.toPlainText()
		discapacidad_motriz = self.Discapacidad_Motriz()
		discapacidad_auditiva = self.Discapacidad_Auditiva()
		discapacidad_visual = self.Discapacidad_Visual()
		discapacidad_intelectual = self.Discapacidad_Intelectual_Mental()
		discapacidad_viceral = self.Discapacidad_Visceral()
		discapacidad_otras = self.Discapacidad_Otras()

		insumomedico_silla_de_reudas = self.Necesita_silla_de_rueda()
		insumomedico_muletas = self.Necesita_muletas()
		insumomedico_protesis = self.Necesita_protesis()
		insumomedico_otros = self.Necesita_Otros()
		descripcion_medicamento_dscp= self.textEdit_medicamento_dscp.toPlainText()
		necesita_algun_medicamento_dscp = self.necesita_algun_medicamento_dscp()

		# Ventana de enfermedad
		enfermedad_de_cancer = self.Tipo_Enfer_Cancer()
		enfermedad_de_diabetes = self.Tipo_Enfer_Diabetes()
		enfermedad_de_hipertension = self.Tipo_Enfer_Hipertension_arterial()
		enfermedad_de_asma = self.Tipo_Enfer_Asma()
		enfermedad_de_cardio = self.Tipo_Enfer_Cardio_Vascula()
		enfermedad_de_gastritis = self.Tipo_Enfer_Gastritis()
		enfermedad_de_bronquitis = self.Tipo_Enfer_Bronquitis()
		enfermedad_de_calculos = self.Tipo_Enfer_Calculos_rinon()
		enfermedad_de_sinusitis = self.Tipo_Enfer_Sinusitis()
		enfermedad_de_otras = self.Tipo_Enfer_Otras()

		descripcion_enfermedad=  self.textEdit_dcrp_enfermedad.toPlainText()
		necesita_algun_medicamento_enfer = self.necesita_medicamento_enfer()
		descripcion_medicamento_enfer = self.textEdit_medicamento_enfer.toPlainText()

		# Ventana de reparacion de vivienda:
		Descripcion_de_reparacion = self.textEdit_dcrp_reparacionvv.toPlainText()
		reparacion_de_techos = self.Reparacion_de_Techos()
		reparacion_de_pared = self.Reparacion_de_Pared()
		reparacion_de_pintura = self.Reparacion_de_Pintura()
		reparacion_de_pisos = self.Reparacion_de_Pisos()
		reparacion_de_electrico = self.Reparacion_de_Electrico()
		reparacion_de_agua = self.Reparacion_de_Agua()
		reparacion_de_agua_servidas = self.Reparacion_de_Agua_servidas()
		reparacion_de_ventanas = self.Reparacion_de_Ventanas()
		reparacion_de_puertas = self.Reparacion_de_Puertas()
		reparacion_de_otras = self.Reparacion_de_otras()
		Linea_blanca = self.Linea_blanca()

		# Ventana bombona 
		tipo_de_cilindro = self.Tipo_de_cilindro()
		cantidad_de_bombonas = int(self.num_bombonas.value())

		# Ventana estudiante
		nivel_estudio = self.nivel_estudio()
		carrera_cursando = self.texedit_carrera.toPlainText()
		donde_estudia = self.texedit_donde_estudia.toPlainText()

		# Venta de visualizador de fotos 
		foto_1 = self.label_miniatura_1.pixmap()
		foto_2 = self.label_miniatura_2.pixmap()
		foto_3 = self.label_miniatura_3.pixmap()
		foto_4 = self.label_miniatura_4.pixmap()
		foto_5 = self.label_miniatura_5.pixmap()
		foto_6 = self.label_miniatura_6.pixmap()

		if foto_1:
			bArray_1 = QByteArray()
			bufer = QBuffer(bArray_1)
			bufer.open(QIODevice.WriteOnly)
			bufer.close()
			foto_1.save(bufer,"PNG")
		else:
			bArray_1 = ""

		if foto_2:
				bArray_2 = QByteArray()
				bufer = QBuffer(bArray_2)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_2.save(bufer,"PNG")
		else:
				bArray_2 = ""

		if foto_3:
				bArray_3 = QByteArray()
				bufer = QBuffer(bArray_3)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_3.save(bufer,"PNG")
		else:
				bArray_3 = ""

		if foto_4:
				bArray_4 = QByteArray()
				bufer = QBuffer(bArray_4)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_4.save(bufer,"PNG")
		else:
				bArray_4 = ""

		if foto_5:
				bArray_5 = QByteArray()
				bufer = QBuffer(bArray_5)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_5.save(bufer,"PNG")
		else:
				bArray_5 = ""

		if foto_6:
				bArray_6 = QByteArray()
				bufer = QBuffer(bArray_6)
				bufer.open(QIODevice.WriteOnly)
				bufer.close()
				foto_6.save(bufer,"PNG")
		else:
				bArray_6 = ""

		if not nombre_1:
			self.lineEdit_1_nombre.setFocus()
		elif not apellido_1:
			self.lineEdit_1_Apellido.setFocus()
		elif not cedula_identidad:
			self.lineEdit_cedula.setFocus()
		elif not telefono_princ:
			self.lineEdit_1_tlf.setFocus()
		elif not genero:
			self.comboBox_genero.setFocus()
		elif not numero_vivienda:
			self.lineEdit_N_vivienda.setFocus()
		elif not direccion:
			self.textEdit_direccion.setFocus()  
		elif not edad:
			self.lineEdit_edad.setFocus()
		elif not parentesco:
			self.comboBox_parentesco.setFocus()
		elif not estado_civil:
			self.comboBox_estadocivil.setFocus()
		else:       

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db')
				cursor = conexion.cursor()
				try:
					# Variables de tiempo insertadas en base de datos
					hora = time.strftime("%I:%M:%S")
					fecha_actual = time.strftime("%d/%m/%y")

					datos_insertar_Gnr = [nombre_1, nombre_2, apellido_1, apellido_2,
									cedula_identidad, genero, telefono_princ, telefono_secund,
									fecha_Nacimiento, edad, profesion_oficio, nivel_instruccion,
									parentesco, estado_civil, inscrito_rep, correo_electronico,
									opcion_pensionado, discapacidad_motriz, discapacidad_auditiva, discapacidad_visual,
									discapacidad_intelectual, discapacidad_viceral, discapacidad_otras,
									descripcion_discapacidad,necesita_algun_medicamento_dscp,
									descripcion_medicamento_dscp, insumomedico_silla_de_reudas,
									insumomedico_muletas, insumomedico_protesis,insumomedico_otros,
									enfermedad_de_cancer,enfermedad_de_diabetes, enfermedad_de_hipertension, enfermedad_de_asma,
									enfermedad_de_cardio, enfermedad_de_gastritis, enfermedad_de_bronquitis, enfermedad_de_calculos,
									enfermedad_de_sinusitis, enfermedad_de_otras,descripcion_enfermedad,
									necesita_algun_medicamento_enfer,descripcion_medicamento_enfer, opcion_embarazada,opcion_lactante,
									nivel_estudio,carrera_cursando,donde_estudia, fecha_actual, hora, numero_vivienda]

					cursor.execute("INSERT INTO USUARIO_DT_GNR(PRIMER_NOMBRE,"
																			"SEGUNDO_NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO,"

																			"CEDULA , GENERO , TELEFONO_PRINCIPAL ," 

																			"TELEFONO_SECUNDARIO, FECHA_NACIMIENTO, EDAD,"

																			"PROFESION_OFICIO, NIVEL_INSTRUCCION, PARENTESCO,"

																			"ESTADO_CIVIL, INSCRITO_REP, CORREO_ELECTRONICO,"

																			"PENSIONADO,DISCAPACIDAD_MOTRIZ, DISCAPACIDAD_AUDITIVA,"
																			
																			"DISCAPACIDAD_VISUAL, DISCAPACIDAD_INTELECTUAL, DISCAPACIDAD_VISCERAL,"
																			
																			"DISCAPACIDAD_OTRAS, DESCRIBA_DISCAPACIDAD,"

																			"TOMA_MEDICAMENTO,DESCRIBA_MEDICAMENTO, SILLA_DE_RUEDA, MULETAS, PROTESIS, INSUMO_OTROS,"
																			
																			"ENFERMEDAD_CANCER, ENFERMEDAD_DIABETES, ENFERMEDAD_HIPERTENSION, ENFERMEDAD_ASMA,"

																			"ENFERMEDAD_CARDIO, ENFERMEDAD_GASTRITIS, ENFERMEDAD_BRONQUITIS, ENFERMEDAD_CALCULOS,"

																			"ENFERMEDAD_SINUSITIS, ENFERMEDAD_OTRAS,"

																			"DESCRIBA_ENFERMEDAD,TOMA_MEDICAMENTO_ENF, DESCRIBA_MEDICAMENTO_ENF,"  

																			"EMBARAZADA, LACTANTE, NIVEL_DE_ESTUDIO,CARRERA_CURSANDO,DONDE_ESTUDIA, FECHA, HORA, N_VIVIENDA)"
										
										" VALUES(?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,"
											"?,?,?,?,?,?,?)", datos_insertar_Gnr)

					idusuario = cursor.lastrowid

					conexion.commit()       
					cursor.close()
					conexion.close()

					if QFile.exists("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db"):
						conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db')
						cursor = conexion.cursor()

						datos_insertar_Ubc = [estado, municipio,parroquia,direccion]

						cursor.execute("INSERT INTO USUARIO_UBCGEOG VALUES(NULL,?,?,?,?)", datos_insertar_Ubc)
						conexion.commit()       
						cursor.close()
						conexion.close()
				
						if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):
							conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db')
							cursor = conexion.cursor()
	
							datos_insertar_Vv = [metros_cuadrados, descripcion_vivienda, reparaciones, Descripcion_de_reparacion,
													reparacion_de_techos,reparacion_de_pared,reparacion_de_pintura, reparacion_de_pisos,
													reparacion_de_electrico,reparacion_de_agua, reparacion_de_agua_servidas, reparacion_de_ventanas,
													reparacion_de_puertas, reparacion_de_otras,
													Linea_blanca, servicio_aguapotable, servicio_aguaservidas, 
													servicio_gasdirecto, servicio_gasbombona, tipo_de_cilindro,cantidad_de_bombonas,
													servicio_internet,servicio_electricidad,
													servicio_tlf_fijo,bArray_1, bArray_2, bArray_3, bArray_4, bArray_5, bArray_6]
								
							cursor.execute("INSERT INTO USUARIO_DT_VV(METROS_CUADRADOS, DESCRIPCION, NECESITA_REPARACION,DESCRIPCION_REPARACION,"
													"REPARACION_TECHOS, REPARACION_PARED, REPARACION_PINTURA, REPARACION_PISOS, REPARACION_ELECTRICO,"
													"REPARACION_AGUA, REPARACION_AGUA_SERVIDAS, REPARACION_VENTANAS, REPARACION_PUERTARS,"
													"REPARACION_OTRAS,"
													"NECESITA_LINEBLANCA, AGUA_POTABLE, AGUA_SERVIDAS,"
													"GAS_DIRECTO, GAS_BOMBONA,"
													"TIPO_DE_CILINDRO , CANTIDAD_DE_BOMBONAS,"
													"INTERNET, ElECTRICIDAD,"
													"TELEFONO_FIJO,"
													"FOTO_ANEXADA1, FOTO_ANEXADA2, FOTO_ANEXADA3, FOTO_ANEXADA4, FOTO_ANEXADA5,FOTO_ANEXADA6)"
													"VALUES(?,?,?,?,"
													"?,?,?,?,"
													"?,?,?,?,"
													"?,?,?,?,"
													"?,?,?,?,"
													"?,?,?,?,"
													"?,?,?,?,?,?)", datos_insertar_Vv)


							conexion.commit()       
							cursor.close()
							conexion.close()

				
							if QFile.exists("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db"):
								conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_PROT_SOCIAL.db')
								cursor = conexion.cursor()

								datos_insertar_Prot = [hogaresdelapatria, amormayor,josegregorio,partohumanizado,
														chambajuvenil, somosvenezuela,frentemiranda, jpsuv]

								cursor.execute("INSERT INTO USUARIO_PROT_SOCIAL VALUES(NULL,?,?,?,?,"
																							"?,?,?,?)", datos_insertar_Prot)
								conexion.commit()       
								cursor.close()
								conexion.close()

								QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",QMessageBox.Ok)

							else:
								QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)
						
						else:
							QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)                            
					else:

						QMessageBox.information(self,"Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
											 QMessageBox.Ok)
				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
											QMessageBox.Ok)
			else:

				QMessageBox.information(self, "Conexion con la base de datos", "No se ha podido conectar con la base de datos.",
												   QMessageBox.Ok)


			self.lineEdit_1_nombre.clear() 
			self.lineEdit_2_nombre.clear()
			self.lineEdit_1_Apellido.clear()
			self.lineEdit_2_Apellido.clear()
			self.lineEdit_cedula.clear()
			self.lineEdit_1_tlf.clear()
			self.lineEdit_2_tlf.clear()
			self.comboBox_genero.setCurrentIndex(-1)
			self.lineEdit_edad.clear()
			self.dateEdit_nacimiento.setDate(QDate.currentDate())
			self.comboBox_profesion.setCurrentIndex(-1)
			self.comboBox_nvl_instruccion.setCurrentIndex(-1)
			self.comboBox_parentesco.setCurrentIndex(-1)
			self.checkBox_1_pensionado.setChecked(False)
			self.checkBox_2_discapacidad.setChecked(False)
			self.checkBox_3_enfer.setChecked(False)
			self.checkBox_4_Embarazada.setChecked(False)
			self.checkBox_5_lactante.setChecked(False)
			self.comboBox_estadocivil.setCurrentIndex(-1)
			self.lineEdit_correo.clear()

			# Ubicacion geografica          
			self.lineEdit_estado.clear()
			self.lineEdit_municipio.clear()
			self.lineEdit_parroquia.clear()
			self.lineEdit_N_vivienda.clear()
			self.textEdit_direccion.clear()

			# Datos de la vivienda
			self.lineEdit_M2.clear()
			self.textEdit_dcrp_vv.clear()

			self.checkBox_aguapotable.setChecked(False)
			self.checkBox_aguasservidas.setChecked(False)
			self.checkBox_gasdirecto.setChecked(False)
			self.checkBox_gasbombona.setChecked(False)
			self.checkBox_internet.setChecked(False)
			self.checkBox_electricidad.setChecked(False)
			self.checkBox_tlf_fijo.setChecked(False)

			# Proteccion Social
			self.checkBox_hogarespatria.setChecked(False)
			self.checkBox_amormayor.setChecked(False)
			self.checkBox_joseGregorio.setChecked(False)
			self.checkBox_partohumanizado.setChecked(False)

			self.checkBox_chambajuvenil.setChecked(False)
			self.checkBox_somosvenezuela.setChecked(False)
			self.checkBox_FrenteMiranda.setChecked(False)
			self.checkBox_jpsuv.setChecked(False)

			# Ventana discapacidad
			self.textEdit_dcrp_discapacidad.clear()

			self.checkBox_27_Dscp_motriz.setChecked(False)
			self.checkBox_26_Dscp_auditiva.setChecked(False)
			self.checkBox_25_Dscp_visual.setChecked(False)
			self.checkBox_23_Dscp_mental.setChecked(False)
			self.checkBox_24_Dscp_viceral.setChecked(False)
			self.checkBox_otras.setChecked(False)

			self.textEdit_medicamento_dscp.clear()

			self.checkBox_sillarueda.setChecked(False)
			self.checkBox_muletas.setChecked(False)
			self.checkBox_protesis.setChecked(False)
			self.checkBox_otros.setChecked(False)

			# Ventana de enfermedad
			self.textEdit_dcrp_enfermedad.clear()
			self.textEdit_medicamento_enfer.clear()
			self.checkBox_27_cancer.setChecked(False)
			self.radioButton_si_medicamentos_enfer.setChecked(False)

			self.checkBox_26_diabetes.setChecked(False)
			self.checkBox_25_hp_arterial.setChecked(False)
			self.checkBox_23_asma.setChecked(False)
			self.checkBox_24_vascular.setChecked(False)
			self.checkBox_28_gastritis.setChecked(False)        
			self.checkBox_29_bronquitis.setChecked(False)
			self.checkBox_30_calcu_rinon.setChecked(False)
			self.checkBox_31_sinusitis.setChecked(False)
			self.checkBox_32_otra_enf.setChecked(False)

			# Ventana reparacion de vivienda
			self.textEdit_dcrp_reparacionvv.clear()

			self.checkBox_arreglo_techos.setChecked(False)
			self.checkBox_2_friso.setChecked(False)
			self.checkBox_3_pintura.setChecked(False)
			self.checkBox_4_arreglo_Pisos.setChecked(False)
			self.checkBox_5_sistema_electrico.setChecked(False)
			self.checkBox_6_sistema_agua.setChecked(False)
			self.checkBox_7_aguas_servidas.setChecked(False)
			self.checkBox_8_fatla_ventanas.setChecked(False)
			self.checkBox_9_falta_puertas.setChecked(False)
			self.checkBox_10_otras_rpr.setChecked(False)

			self.checkBox_Lavadora.setChecked(False)
			self.checkBox_Nevera.setChecked(False)
			self.checkBox_Cocina.setChecked(False)
			self.checkBox_Aireacondicionado.setChecked(False)

			# Ventana de gas bombona
			self.checkBox_27_pdvsa_gas.setChecked(False)
			self.checkBox_26_tropiven.setChecked(False)
			self.checkBox_25_dani_gas.setChecked(False)
			self.checkBox_23_hermagas.setChecked(False)
			self.checkBox_24_autogas.setChecked(False)
			self.num_bombonas.setValue(0)

			# Ventana estudiante
			self.checkbox_primaria.setChecked(False)
			self.checkbox_bachillerato.setChecked(False)
			self.checkbox_universitario.setChecked(False)
			self.checkbox_especializacion.setChecked(False)

			self.texedit_donde_estudia.clear()
			self.texedit_carrera.clear()

			# Ventana visualizador de foto
			self.label_miniatura_1.clear()
			self.label_miniatura_1.setText("Click para anexar")
			self.label_miniatura_1_nombre.clear()

			self.label_miniatura_2.clear()
			self.label_miniatura_2.setText("Click para anexar")
			self.label_miniatura_2_nombre.clear()

			self.label_miniatura_3.clear()
			self.label_miniatura_3.setText("Click para anexar")
			self.label_miniatura_3_nombre.clear()

			self.label_miniatura_4.clear()
			self.label_miniatura_4.setText("Click para anexar")
			self.label_miniatura_4_nombre.clear()

			self.label_miniatura_5.clear()
			self.label_miniatura_5.setText("Click para anexar")
			self.label_miniatura_5_nombre.clear()


			self.label_miniatura_5.clear()
			self.label_miniatura_5.setText("Click para anexar")
			self.label_miniatura_5_nombre.clear()


			self.label_miniatura_6.clear()
			self.label_miniatura_6.setText("Click para anexar")
			self.label_miniatura_6_nombre.clear()
	
	# funcion de estudiante nivel de estudio =======================================================================================
	def nivel_estudio(self):
		if self.checkbox_primaria.isChecked():
			return "Primaria"
		elif self.checkbox_bachillerato.isChecked():
			return "Bachillerato"
		elif self.checkbox_universitario.isChecked():
			return "Universitario"
		elif self.checkbox_tcn_superior.isChecked():
			return "Técnico Superior universitario "
		elif self.checkbox_especializacion.isChecked():
			return "Especialización"
		else:
			return "Ningún"

	# funcion de estudiante =======================================================================================
	def Estudiante(self,i):
			if i == 15:
				self.Mostrar_estudiante()
			else:
				return "No esta estudiando"

	# opcion de lactante =======================================================================================
	def opcion_de_lactante(self):
		if self.checkBox_5_lactante.isChecked():
			return "Si"
		else: 
			return "No esta en estado de lactancia"

	# opcion de embarazada =======================================================================================
	def opcion_de_embarazada(self):
		if self.checkBox_4_Embarazada.isChecked():
			return "Si"
		else:
			return "No esta en estado de embarazo"

	# opcion de servicio gas bombona =======================================================================================
	def gas_bombona_servicio(self):
		if self.checkBox_gasbombona.isChecked():
			return "Si"
		else:
			return "No"

	# opcion pensionado  =======================================================================================c
	def pensionado(self):
		if self.checkBox_1_pensionado.isChecked():
			return "Pensionado"
		else:
			return "No esta pensionado"

	# Ventana reparacion de vivienda  =======================================================================================
	def Linea_blanca(self):
		if self.checkBox_Lavadora.isChecked():
			return "Lavadora"
		elif self.checkBox_Nevera.isChecked():
			return "Nevera"
		elif self.checkBox_Cocina.isChecked():
			return "Cocina"
		elif self.checkBox_Aireacondicionado.isChecked():
			return "Aire Acondicionado"
		else:
			return "No necesita linea blanca"

	# TIPOS DE REPARACION
	def Reparacion_de_Techos(self):
		if self.checkBox_arreglo_techos.isChecked():
			return "Arreglo o falta de techos"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pared(self):
		if self.checkBox_2_friso.isChecked():
			return "Friso de pared"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pintura(self):
		if self.checkBox_3_pintura.isChecked():
			return " Falta de pintura"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Pisos(self):
		if self.checkBox_4_arreglo_Pisos.isChecked():
			return "Arreglo de pisos"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Electrico(self):
		if self.checkBox_5_sistema_electrico.isChecked():
			return "Sistema eléctrico"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Agua(self):
		if self.checkBox_6_sistema_agua.isChecked():
			return "Sistema de agua"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Agua_servidas(self):
		if self.checkBox_7_aguas_servidas.isChecked():
			return "Sistema de aguas servida"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Ventanas(self):
		if self.checkBox_8_fatla_ventanas.isChecked():
			return "Falta de Ventanas"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_Puertas(self):
		if self.checkBox_9_falta_puertas.isChecked():
			return "Falta de puertas"
		else:
			return "No necesita este arreglo"

	def Reparacion_de_otras(self):
		if self.checkBox_10_otras_rpr.isChecked():
			return "Otras..."
		else:
			"No necesita este arreglo"

	# Ventana de Enfermedad =======================================================================================
	def Tipo_Enfer_Cancer(self):    
		if self.checkBox_27_cancer.isChecked():
			return "Cáncer"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Diabetes(self):
		if self.checkBox_26_diabetes.isChecked():
			return "Diabetes"
		else:
			return "No posee esta enfermedad" 

	def Tipo_Enfer_Hipertension_arterial(self):
		if self.checkBox_25_hp_arterial.isChecked():
			return "Hipertensión arterial"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Asma(self):
		if self.checkBox_23_asma.isChecked():
			return "Asma"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Cardio_Vascula(self):
		if self.checkBox_24_vascular.isChecked():
			return "Cardio Vascular"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Gastritis(self):
		if self.checkBox_28_gastritis.isChecked():
			return "Gastritis"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Bronquitis(self):
		if self.checkBox_29_bronquitis.isChecked():
			return "Bronquitis"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Calculos_rinon(self):
		if self.checkBox_30_calcu_rinon.isChecked():
			return "Cálculos de riñón"
		else:
			return "No posee esta enfermedad"

	def Tipo_Enfer_Sinusitis(self):
		if self.checkBox_31_sinusitis.isChecked():
			return "Sinusitis"
		else:
			return "No posee esta enfermedad"
			
	def Tipo_Enfer_Otras(self):
		if self.checkBox_32_otra_enf.isChecked():
			return "Otra..."
		else:
			"No posee esta enfermedad"

	def necesita_medicamento_enfer(self):
			if self.radioButton_si_medicamentos_enfer.isChecked():
				return "Si"
			elif self.radioButton_no_medicamentos_enfer.isChecked():
				return "No"
			else:
				return "No necesita medicamento"

	# Ventana de discapacidad =======================================================================================
	def Necesita_silla_de_rueda(self):
		if self.checkBox_sillarueda.isChecked():
			return "Necesita silla de rueda"
		else:
			return "No necesita este insumo medico"

	def Necesita_muletas(self):
		if self.checkBox_muletas.isChecked():
			return "Necesita muletas"
		else:
			return "No necesita este insumo medico"

	def Necesita_protesis(self):
		if self.checkBox_protesis.isChecked():
			return "Necesita protesis"
		else:
			return "No necesita este insumo medico"

	def Necesita_Otros(self):
		if self.checkBox_otros.isChecked():
			return "Otros..."
		else:
			return "No necesita este insumo medico"

	def necesita_algun_medicamento_dscp(self):
			if self.radioButton_si_medicamentos_dscp.isChecked():
				return "Si"
			elif self.radioButton_no_medicamentos_dscp.isChecked():
				return "No"
			else:
				return "No necesita medicamento"

	# Tipo de discapacidades        
	def si_posee_discapacidad(self):
		if self.checkBox_2_discapacidad.isChecked():
			return "Si"
		else:
			return "No"

	def Discapacidad_Motriz(self):
		if self.checkBox_27_Dscp_motriz.isChecked():
			return "Discapacidad Motriz"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Auditiva(self):
		if self.checkBox_26_Dscp_auditiva.isChecked():
			return "Discapacidad Auditiva"

		else:
			return "No posee esta discapacidad"

	def Discapacidad_Visual(self):
		if self.checkBox_25_Dscp_visual.isChecked():
			return "Discapacidad Visual"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Intelectual_Mental(self):
		if self.checkBox_23_Dscp_mental.isChecked():
			return "Discapacidad Intelectual o Mental"
		else:
			return "No posee esta discapacidad"

	def Discapacidad_Visceral(self):
		if self.checkBox_24_Dscp_viceral.isChecked():
				return "Discapacidad Visceral"
		else: 
			return " No posee esta discapacidad"

	def Discapacidad_Otras(self):
		if self.checkBox_otras.isChecked():
			return "Otras..."
		else:
			return "No posee esta discapacidad"

	# RadioButton_reparacion
	def RadioButton_reparacion(self):
		if self.radioButton_rp_si.isChecked():
			return "Si"
		elif self.radioButton_rp_no.isChecked():
			return "No"
		else:
			return "No necesita reparacion"

	# Funcion de si esta inscrito en el REP o no =============================================================================================
	def RadioButton_rep(self):
		if self.radiobutton_si_inscrito.isChecked():
			return "Si"
		elif self.radiobutton_no_inscrito.isChecked():
			return "No esta inscrito"
		else:
			return "No"

	# CheckBox de servicios que posee ==================================================================================================
	def CheckBox_aguapotable(self):
		if self.checkBox_aguapotable.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_aguaservidas(self):
		if self.checkBox_aguasservidas.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_gasdirecto(self):
		if self.checkBox_gasdirecto.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_gasbombona(self):
		if self.checkBox_gasbombona.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_internet(self):
		if self.checkBox_internet.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_electricidad(self):
		if self.checkBox_electricidad.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_telefonofijo(self):
		if self.checkBox_tlf_fijo.isChecked():
			return "Si"
		else:
			return "No"

	# Proteccion Social =======================================================================================
	def CheckBox_hogaresdelapatria(self):
		if self.checkBox_hogarespatria.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_amormayor(self):
		if self.checkBox_amormayor.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_josegregorio(self):
		if self.checkBox_joseGregorio.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_partohumanizado(self):
		if self.checkBox_partohumanizado.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_somosvenezuela(self):
		if self.checkBox_somosvenezuela.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_chambajuvenil(self):
		if self.checkBox_chambajuvenil.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_frentemiranda(self):
		if self.checkBox_FrenteMiranda.isChecked():
			return "Si"
		else:
			return "No"

	def CheckBox_jpsuv(self):
		if self.checkBox_jpsuv.isChecked():
			return "Si"
		else:
			return "No"

	def Tipo_de_cilindro(self):
		if self.checkBox_27_pdvsa_gas.isChecked():
			return "PDVSA Gas"
		elif self.checkBox_26_tropiven.isChecked():
			return "Tropiven"
		elif self.checkBox_25_dani_gas.isChecked():
			return "Dani el gas" 
		elif self.checkBox_23_hermagas.isChecked():
			return "Hermagas" 
		elif self.checkBox_24_autogas.isChecked():
			return "Autogas" 
		else:
			return "No"

	def centrar(self):
		frameGm = self.frameGeometry()
		screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
		centerPoint = QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	def Mostrar_Discapacidad(self,posicionX=190):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_Discpacidad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Discpacidad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(posicionX, 600, 590, 294))
		self.animacionMostar.setEndValue(QRect(190, 120, 590, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_Discapacidad(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_Discpacidad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Discpacidad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(190, 120, 590, 294))
		self.animacionMostar.setEndValue(QRect(190, 600, 590, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_Enfermedad(self,posicionX=190):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_Enfermedad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Enfermedad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(posicionX, 600, 600, 294))
		self.animacionMostar.setEndValue(QRect(190, 120, 600, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_Enfermedad(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_Enfermedad,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_Enfermedad))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(190, 120, 600, 294))
		self.animacionMostar.setEndValue(QRect(190, 600, 600, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_gas_bombona(self,posicionX=300):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_gas_bombona,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_gas_bombona))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(posicionX, 600, 380, 294))
		self.animacionMostar.setEndValue(QRect(300, 120, 380, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_gas_bombona(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_gas_bombona,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_gas_bombona))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(300, 120,  380, 294))
		self.animacionMostar.setEndValue(QRect(300, 600, 380, 294))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_rpr_vv(self,posicionX=180):
		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(self.frame_principal_rpr_vv,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_rpr_vv))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(posicionX, 600, 675, 325))
		self.animacionMostar.setEndValue(QRect(180, 100, 675, 325))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_rpr_vv(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_rpr_vv,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_rpr_vv))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(180, 100, 675, 325))
		self.animacionMostar.setEndValue(QRect(180,600, 675, 325))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_visualizador(self,posicionX=145):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_visualizador,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_visualizador))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(posicionX, 600, 770,410))
		self.animacionMostar.setEndValue(QRect(145, 50, 770,410))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_visualizador(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_visualizador,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_visualizador))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(145, 50, 770,410))
		self.animacionMostar.setEndValue(QRect(145,600, 770,410))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Mostrar_estudiante(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_estudiante,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_estudiante))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(200, 1000, 613,303))
		self.animacionMostar.setEndValue(QRect(200, 100, 613,303))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_estudiante(self):
		self.animacionMostar = QPropertyAnimation(self.frame_principal_estudiante,b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.frame_principal_estudiante))

		self.animacionMostar.setDuration(100)
		self.animacionMostar.setStartValue(QRect(200, 100, 613,303))
		self.animacionMostar.setEndValue(QRect(200, 1000, 613,303))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Eliminar(self):
		def establecerValores():
			labelConImagen.clear()
					
		# Verificar que QLabel tiene imagen
		labelConNombre = self.label_miniatura_1_nombre
		if labelConNombre:
			labelConNombre.clear()

		labelConImagen = ""
		if self.label_miniatura_1.pixmap():
			labelConImagen = self.label_miniatura_1                     
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_1(self):
		def establecerValores():
			labelConImagen.clear()

		labelConNombre = self.label_miniatura_2_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_2.pixmap():
			labelConImagen = self.label_miniatura_2
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_2(self):
		def establecerValores():
			labelConImagen.clear()
		
		labelConNombre = self.label_miniatura_3_nombre
		if labelConNombre:
			labelConNombre.clear()

		if self.label_miniatura_3.pixmap():
			labelConImagen = self.label_miniatura_3
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_3(self):
		def establecerValores():
			labelConImagen.clear()

		labelConNombre = self.label_miniatura_4_nombre
		if labelConNombre:
			labelConNombre.clear()

		if self.label_miniatura_4.pixmap():
			labelConImagen = self.label_miniatura_4
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_4(self):
		def establecerValores():
			labelConImagen.clear()

		labelConNombre = self.label_miniatura_5_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_5.pixmap():
			labelConImagen = self.label_miniatura_5
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")

	def Eliminar_5(self):
		def establecerValores():
			labelConImagen.clear()

		labelConNombre = self.label_miniatura_6_nombre
		if labelConNombre:
			labelConNombre.clear()
			
		if self.label_miniatura_6.pixmap():
			labelConImagen = self.label_miniatura_6
		if labelConImagen:
			labelConImagen.clear()
			labelConImagen.setText("Click para anexar")
	
	def Cargar_5(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_5(self.label_miniatura_6, imagen, nombre)
				self.foto_1(imagen)
		else:
			None

	def Mostrar_5(self, label, imagen, nombre, posicionX= 400):
		imagen = QPixmap.fromImage(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_6_nombre.setText(nombre)))
													   
		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(400, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_4(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   
			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_4(self.label_miniatura_5, imagen, nombre)
				self.foto_1(imagen)
		else:
			None

	def Mostrar_4 (self, label, imagen, nombre, posicionX= 210):
		imagen = QPixmap.fromImage(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_5_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(210, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_3(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_3(self.label_miniatura_4, imagen, nombre)
				self.foto_1(imagen)
		else:
			None

	def Mostrar_3 (self, label, imagen, nombre, posicionX= 20):
		imagen = QPixmap.fromImage(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_4_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 180, 171, 121))
		self.animacionMostar.setEndValue(QRect(20, 200, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_2(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:   			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_2(self.label_miniatura_3, imagen, nombre)
				self.foto_1(imagen)

		else:
			None

	def Mostrar_2 (self, label, imagen, nombre, posicionX= 400):
		imagen = QPixmap.fromImage(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_3_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(400, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar_1(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  QDir.currentPath(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)")
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:               
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_1(self.label_miniatura_2, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_2 = imagen
		else:
			None

	def Mostrar_1 (self, label, imagen, nombre, posicionX= 210):
		imagen = QPixmap.fromImage(imagen)

		# Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_2_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(210, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar(self):
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
													  getcwd(),
													   "Archivos de imagen (*.jpg *.png *.ico *.bmp)",
													   options = QFileDialog.Options())
		if nombreImagen:
			imagen = QImage(nombreImagen)
			if imagen.isNull():
				if nombreImagen:
					self.Eliminar()
						
					QMessageBox.information(self, "Visor de imágenes",
											"No se puede cargar %s." % nombreImagen)
					return
			else:
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar(self.label_miniatura_1, imagen, nombre)
				self.foto_1(imagen)
		else:
			None
			
	def foto_1(self,imagen):
		Ver_fotos(imagen,self).exec_()

	def Mostrar(self,label, imagen, nombre, posicionX=20):
		imagen = QPixmap.fromImage(imagen)
		self.foto_1 = imagen
		# Escalar imagen a 169x119 si el ancho es mayor a 171 o el alto mayor a 121
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)

		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_1_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 0, 171, 121))
		self.animacionMostar.setEndValue(QRect(20, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

class QLabelClickable(QLabel):
	clicked = pyqtSignal()
	
	def __init__(self, parent=None):
		super(QLabelClickable, self).__init__(parent)

	def mousePressEvent(self, event):
		self.clicked.emit()

# Clase ventana Acerca de
class Acerca_de(QDialog):
	def __init__(self, parent = None):
		super(Acerca_de, self).__init__()
		self.setWindowTitle("Acerca de VESOR")
		self.setWindowIcon(QIcon(":/Logo_vesor/Imagenes-iconos/Icono_window.png"))
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setObjectName("Dialog")
		self.resize(519,671)
		self.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591,\n" 
		"x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}")

		self.initUi()

	def initUi(self):
		# Frame fondo
		self.frame_contenido = QFrame(self)
		self.frame_contenido.setGeometry(QRect(10,10,500,650))
		self.frame_contenido.setStyleSheet("QFrame{background-color:#E5E7EE;\n"
		"border-radius: 20px;\n"
		"}")

		# Label con nombre Vesor
		self.label_imagen = QLabel(self)
		self.label_imagen.setGeometry(QRect(-20,-70,361,291))
		self.label_imagen.setStyleSheet("QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png);\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"}")

		# Texto descripcion Vesor
		self.frame_texto = QFrame(self)
		self.frame_texto.setGeometry(QRect(320,20,181,111))
		self.frame_texto.setStyleSheet("QFrame{background-color: #12191D;\n"
		"border-radius: 20px;\n"
		"}")
		self.label_descripcion = QLabel(self)
		self.label_descripcion.setGeometry(QRect(305,-25,210,210))
		self.label_descripcion.setStyleSheet("QLabel{\n"
		"border-image: url(:/Icono_descipcion/Imagenes-iconos/descripcion.png);\n"
		"}")

		# Imagen Central
		self.label_imagen_central = QLabel(self)
		self.label_imagen_central.setGeometry(QRect(20,140,481,341))
		self.label_imagen_central.setStyleSheet("QLabel{border-radius:25px;\n"
		"border-image: url(:/Acerca_de/Imagenes-iconos/Acerca de .png);\n"
		"}")

		# Datos de diseñadores y dev
		self.frame_disenadores = QFrame(self)
		self.frame_disenadores.setGeometry(QRect(20,490,481,161))
		self.frame_disenadores.setStyleSheet("QFrame{border-radius: 20px;\n"
		"background-color:#12191D;\n"
		"}")

		self.label_texto = QLabel(self.frame_disenadores)
		self.label_texto.setGeometry(QRect(150,0,181,31))
		self.label_texto.setText("Desarrolladores y Diseñadores")
		self.label_texto.setStyleSheet("QLabel{color: #ffffff}")

		self.Button_facebook = QPushButton(self.frame_disenadores)
		self.Button_facebook.setGeometry(QRect(-3,20,148,32))
		self.Button_facebook.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}" )
		self.Button_facebook.setText("Jose Alejandro")
		self.Button_facebook.setIcon(QIcon(":/Icono_facebook/Imagenes-iconos/Facebook.png"))
		self.Button_facebook.setIconSize(QSize(30,30))
		self.Button_facebook.setToolTip("Click para ir al perfil")

		self.Button_gmail = QPushButton(self.frame_disenadores)
		self.Button_gmail.setGeometry(QRect(0,50,300,32))
		self.Button_gmail.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"font:10pt Arial;"
		"}" )
		self.Button_gmail.setText("sierramendezjosealejandro@gmail.com")
		self.Button_gmail.setIcon(QIcon(":/Icono_gmail/Imagenes-iconos/gmail.png"))
		self.Button_gmail.setIconSize(QSize(30,30))


		self.Button_github = QPushButton(self.frame_disenadores)
		self.Button_github.setGeometry(QRect(140,20,141,32))
		self.Button_github.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}" )
		self.Button_github.setText("JoseSierraVzl")
		self.Button_github.setIcon(QIcon(":/Icono_github/Imagenes-iconos/Githup.png"))
		self.Button_github.setIconSize(QSize(30,30))
		self.Button_github.setToolTip("Click para ir al perfil")

		self.line = QFrame(self.frame_disenadores)
		self.line.setGeometry(QRect(15, 85, 270, 1))
		self.line.setStyleSheet("QFrame{background-color: #E5E7EE;}")

		self.Button_facebook_2 = QPushButton(self.frame_disenadores)
		self.Button_facebook_2.setGeometry(QRect(-5,90,141,32))
		self.Button_facebook_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}" )
		self.Button_facebook_2.setText("Cristian Cala")
		self.Button_facebook_2.setIcon(QIcon(":/Icono_facebook/Imagenes-iconos/Facebook.png"))
		self.Button_facebook_2.setIconSize(QSize(30,30))
		self.Button_facebook_2.setToolTip("Click para ir al perfil")

		self.Button_gmail_2 = QPushButton(self.frame_disenadores)
		self.Button_gmail_2.setGeometry(QRect(-15,120,271,32))
		self.Button_gmail_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"font:10pt Arial;"
		"}")
		self.Button_gmail_2.setText("cristiancala@protonmail.com")
		self.Button_gmail_2.setIcon(QIcon(":/Icono_gmail/Imagenes-iconos/gmail.png"))
		self.Button_gmail_2.setIconSize(QSize(30,30))


		self.Button_github_2 = QPushButton(self.frame_disenadores)
		self.Button_github_2.setGeometry(QRect(135,90,141,32))
		self.Button_github_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}" )

		self.Button_github_2.setText("CristianCala")
		self.Button_github_2.setIcon(QIcon(":/Icono_github/Imagenes-iconos/Githup.png"))
		self.Button_github_2.setIconSize(QSize(30,30))
		self.Button_github_2.setToolTip("Click para ir al perfil")

		self.texto_instagram = QTextBrowser(self.frame_disenadores)
		self.texto_instagram.setGeometry(QRect(355,20,211,101))
		self.texto_instagram.setText("   Síguenos\nen Instagram")
		self.texto_instagram.setStyleSheet("QTextBrowser{font: 11pt;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"   
		"color: #ffffff;\n"
		"}")

		self.Button_instagram = QPushButton(self.frame_disenadores)
		self.Button_instagram.setGeometry(QRect(330,65,140,32))
		self.Button_instagram.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt Arial;\n"
		"}" )
		self.Button_instagram.setText("@_codeloid")
		self.Button_instagram.setIcon(QIcon(":/Icono_instagram/Imagenes-iconos/Instagram.png"))
		self.Button_instagram.setToolTip("Click para ir al perfil")

		self.texto_instagram_2 = QTextBrowser(self.frame_disenadores)
		self.texto_instagram_2.setGeometry(QRect(330,95,211,101))
		self.texto_instagram_2.setText("Para que estés al tanto\n"
										"  de nuestros trabajos")
		self.texto_instagram_2.setStyleSheet("QTextBrowser{font: 10pt;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"   
		"color: #ffffff;\n"
		"}")

		# Eventos
		self.Button_facebook.clicked.connect(self.enlace_facebook_1)
		self.Button_github.clicked.connect(self.enlance_github_1)
		self.Button_facebook_2.clicked.connect(self.enlace_facebook_2)
		self.Button_github_2.clicked.connect(self.enlace_github_2)
		self.Button_instagram.clicked.connect(self.enlace_instagram)

	def enlace_facebook_1(self):
		url = "https://www.facebook.com/JAMSCMD"
		webbrowser.open(url)

	def enlance_github_1(self):
		url = "https://github.com/JoseSierraVzl"
		webbrowser.open(url)

	def enlace_facebook_2(self):
		url = "https://www.facebook.com/rafael.sierra.31542841"
		webbrowser.open(url)

	def enlace_github_2(self):
		url = "https://github.com/CristianCala"
		webbrowser.open(url)

	def enlace_instagram(self):
		url = "https://www.instagram.com/_codeloid/"
		webbrowser.open(url)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	Window_ventana = CustomWindow()
	Window_ventana.showFullScreen()
	Window_ventana.show()
	app.exec_()