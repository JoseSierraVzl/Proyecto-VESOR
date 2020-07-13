import sqlite3
#from os import getcwd, makedirs
from Source_rc import *
import sys
import os
import random
import re
#import time

#from time import clock
#from random import randint
#from PyQt5 import uic

#importaciones de encriptado
import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from PyQt5 import QtGui
from PyQt5.QtGui import (QIcon)
						 
from PyQt5.QtCore import (Qt, QRect, QPropertyAnimation, QAbstractAnimation, QTimer)

from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, QFrame, QLabel)


class serial_validation(QDialog):

	def __init__(self, parent=None):
		super(serial_validation, self).__init__()
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowTitle("Validación de VESOR")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		#self.setFixedSize(530, 542)
		self.setFixedSize(800,440)
		self.setStyleSheet("QDialog{\n"
						   "background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
						   "}\n"
						   "")
		self.initUi()
		#self.Mostrar_1()
		#self.Mostrar_imagenes()
		self.time_image()


		count = 1
		self.crearSerial(count)

	def crearSerial(self, count):
		serial = ("LPQO0-PCZDU-BXZZZ-JG9U1-UT08A")
		if os.path.isfile('archivito-de-pruebas/Serial.txt'):
			print("ya esta creado el serial papu")

		else:
			try:
				archivo_serial = open("archivito-de-pruebas/Serial.txt", "w")
				archivo_serial.write(serial)
				archivo_serial.close()

			except Exception as e:
				print("Error 1: ", e)

			try:

				random_generator = Crypto.Random.new().read

				private_key = RSA.generate(1024, random_generator) #Llave privada 
				public_key = private_key.publickey() #Llave publica 

				private_key = private_key.exportKey(format='DER')
				public_key = public_key.exportKey(format='DER')

				private_key = binascii.hexlify(private_key).decode('utf8')
				public_key = binascii.hexlify(public_key).decode('utf8')

				with open("archivito-de-pruebas/clave.key", "w") as archivo_clave:
						archivo_clave.write(public_key)
						archivo_clave.close()

						if archivo_clave:
							privat = open("archivito-de-pruebas/clave2.key", "w")
							privat.write(private_key)
							privat.close()



				clave = open("archivito-de-pruebas/clave.key", "rb").read()

				#encrypt_message = str(encrypt_message)
				archivo_serial = open("archivito-de-pruebas/Serial.txt", "r").read()
				archivo_serial = archivo_serial.encode()

				clave = RSA.importKey(binascii.unhexlify(clave))

				cipher = PKCS1_OAEP.new(clave)

				encrypt_message = cipher.encrypt(archivo_serial)
				print("Este es el mensaje encriptado: ", encrypt_message)

				if encrypt_message:
					archivo_serial = open("archivito-de-pruebas/Serial.txt", "wb")
					archivo_serial.write(encrypt_message)
					archivo_serial.close()

			except Exception as e:
				print(e)




	def initUi(self):

		#Style #############################################

		# Style de carousel
		style_frame_carousel = ("QFrame\n"
								"{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		###

		# Style Label Vesor
		style_label_vesor = (
			"QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png)}")
		###

		# Style label text
		style_label_text = ("QLabel{\n"
							"color:#12191D;\n"
							"border-radius: 6px;\n"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							"}")
		###

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
		###

		#Style QPushButton
		style_QPushButton = ("QPushButton{\n"
							"border: 2px solid white;"
							"}\n"
							"QPushButton:hover{\n"
							"background-color:rgb(0, 0, 0);\n"
							"color:rgb(255, 255, 255);\n"
							"}")
		###

		# Style_labelImagen_1
		style_labelImagen_1 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_1.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###
		# style_labelImagen_2
		style_labelImagen_2 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_2.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###
		# style_labelImagen_3
		style_labelImagen_3 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_3.png);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###

		# style_labelImagen_4
		style_labelImagen_4 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_4.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###

		# style_labelImagen_5
		style_labelImagen_5 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_5.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###

		# style_labelImagen_6
		style_labelImagen_6 = ("QLabel{\n"
							   "border-radius: 22px;\n"
							   "border-image: url(:/Imagenes/Imagenes-iconos/imagen_6.jpg);\n"
							   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							   "}")
		###
		#####################################################
		
		self.frame_carousel = QFrame(self)
		self.frame_carousel.setGeometry(QRect(20, 90, 491, 370))
		self.frame_carousel.setStyleSheet(style_frame_carousel)
		self.frame_carousel.move(300,20)

		self.label_vesor = QLabel(self)
		self.label_vesor.setGeometry(QRect(100, 100,200, 150))
		self.label_vesor.setStyleSheet(style_label_vesor)
		self.label_vesor.move(50,-20)

		self.label_encabezado = QLabel(self)
		self.label_encabezado.setGeometry(QRect(100, 300,300, 150))
		self.label_encabezado.setStyleSheet(style_label_text_especial)
		self.label_encabezado.setText("Ingrese el serial para validar")
		self.label_encabezado.setFont(QtGui.QFont("Comic Sans", 11, QtGui.QFont.Bold))
		self.label_encabezado.move(30,50)

		self.text_explicacion = QLabel(self)
		self.text_explicacion.setGeometry(QRect(100,300,300,150))
		self.text_explicacion.setStyleSheet(style_label_text_especial)
		self.text_explicacion.setAlignment(Qt.AlignJustify)
		self.text_explicacion.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.text_explicacion.setText(" Recibirá el código de parte de X\n y a continuación podrá validar\n VESOR con facilidad para que pueda\n disfrutar de todo lo que el programa\n puede ofrecerle.")
		self.text_explicacion.move(20,150)

		self.text_encabezado = QLabel(self)
		self.text_encabezado.setGeometry(QRect(100,300,300,150))
		self.text_encabezado.setStyleSheet(style_label_text_especial)
		self.text_encabezado.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.text_encabezado.setText("El serial es similar a esto:\nSerial:\nXXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
		self.text_encabezado.move(20,190)

		self.label_text = QLabel(self)
		self.label_text.setGeometry(QRect(20, 460, 411, 20))
		self.label_text.setStyleSheet(style_label_text_especial)
		self.label_text.setText("Serial del producto:")
		self.label_text.setFont(QtGui.QFont("Comic Sans", 11, QtGui.QFont.Bold))
		self.label_text.move(20,380)

		self.lineEdit_serial = QLineEdit(self)
		self.lineEdit_serial.setGeometry(QRect(10, 200, 300, 20))
		self.lineEdit_serial.setAlignment(Qt.AlignCenter)
		self.lineEdit_serial.setMaxLength(29)
		self.lineEdit_serial.setInputMask('XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')
		self.lineEdit_serial.setStyleSheet(style_lineEdit_serial)
		self.lineEdit_serial.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.lineEdit_serial.setToolTip("Ingrese el serial para la validación del programa")
		self.lineEdit_serial.move(20,400)


		self.buttonAceptar = QPushButton(self)
		self.buttonAceptar.setGeometry(QRect(450,500,80,31))
		self.buttonAceptar.setStyleSheet(style_QPushButton)
		self.buttonAceptar.setText("Aceptar")
		self.buttonAceptar.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))        
		self.buttonAceptar.move(350,400)

		self.buttonCancelar = QPushButton(self)
		self.buttonCancelar.setGeometry(QRect(450,500,80,31))
		self.buttonCancelar.setStyleSheet(style_QPushButton)
		self.buttonCancelar.setText("Cancelar")
		self.buttonCancelar.setFont(QtGui.QFont("Comic Sans", 9, QtGui.QFont.Bold))
		self.buttonCancelar.move(700,400)

		#Label description
		self.label_description_1 = QLabel(self)
		self.label_description_1.setGeometry(QRect(20, 100, 491, 20))
		self.label_description_1.setStyleSheet(style_label_text)
		self.label_description_1.setText("")
		self.label_description_1.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
		self.label_description_1.setAlignment(Qt.AlignCenter)
		self.label_description_1.move(300,30)
		###

		# Imagen_1
		self.label_Imagen_1 = QLabel(self.frame_carousel)
		self.label_Imagen_1.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_1.setStyleSheet(style_labelImagen_1)
		###


		# Imagen_2
		self.label_Imagen_2 = QLabel(self.frame_carousel)
		self.label_Imagen_2.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_2.setStyleSheet(style_labelImagen_2)
		###

		#Imagen_3
		self.label_Imagen_3 = QLabel(self.frame_carousel)
		self.label_Imagen_3.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_3.setStyleSheet(style_labelImagen_3)
		###
  
		#Imagen_4
		self.label_Imagen_4 = QLabel(self.frame_carousel)
		self.label_Imagen_4.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_4.setStyleSheet(style_labelImagen_4)
		###

		#Imagen_5
		self.label_Imagen_5 = QLabel(self.frame_carousel)
		self.label_Imagen_5.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_5.setStyleSheet(style_labelImagen_5)
		###

		#Imagen_6
		self.label_Imagen_6 = QLabel(self.frame_carousel)
		self.label_Imagen_6.setGeometry(QRect(-520, 40, 451, 311))
		self.label_Imagen_6.setStyleSheet(style_labelImagen_6)
		###

		#Eventos #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
		self.buttonAceptar.clicked.connect(self.Encriptar)
		self.buttonCancelar.clicked.connect(self.cancelar)
		#########################################################################


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
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("Vista general de datos")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)
	def Ocultar_1(self):

		self.animacionMostar = QPropertyAnimation(self.label_Imagen_1, b"geometry")
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))
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
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

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
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)


	def Mostrar_4(self):

		self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText("Opciones de búsqueda especificadas")))
		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Ocultar_4(self):

		self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

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
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

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
		self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

		self.animacionMostar.setDuration(500)
		self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
		self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)


	def Encriptar(self):
		
		serial = str(self.lineEdit_serial.text())

		archivo_serial = open("archivito-de-pruebas/Serial.txt", "rb").read()

		#Desencriptar mensaje 
		clave_2 = open("archivito-de-pruebas/clave2.key", "rb").read()

		clave_2 = RSA.importKey(binascii.unhexlify(clave_2)) 

		cipher_2 = PKCS1_OAEP.new(clave_2)

		dato_desencriptado = cipher_2.decrypt(archivo_serial)
		print(dato_desencriptado)

		serial_line = ("b"+"'"+serial+"'")
		dato_desencriptado = str(dato_desencriptado)

		print("ESTE ES EL LINE: ", serial_line)

		if dato_desencriptado == serial_line:
			print("Funciono, arranco la siguiente ventana")

		else:
			print("No ha escrito nada")

		# if dato != None:
		#     print("todo bien")

		# else:
		#     QMessageBox.information(self, "Error", "Serial no válido", QMessageBox.Yes)



	def cancelar(self):

		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de validación?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar esta ventana?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
				
		cerrar.exec_()
				
		if cerrar.clickedButton() == botonSalir:
			self.destroy()
		else:
			pass


		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = serial_validation()
	interface.show()
	app.exec_()
