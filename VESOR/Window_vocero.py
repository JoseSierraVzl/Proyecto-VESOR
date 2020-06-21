#======================================================================================================
import sqlite3
from os import getcwd, makedirs
from Source_rc import *

#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import*

#from Window_visor_de_imagenes import *

#from Window_reparacion import *

#from Window_enfermedad import * 

#from Window_discapacidad import *

#from Window_gas_bombona import *



#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
import sys, os
from random import randint
from PyQt5 import  uic 

from PyQt5.QtGui import (QFont, QIcon, QResizeEvent, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (pyqtSlot, Qt, QDir, QPoint, pyqtSignal, QByteArray, QIODevice, QBuffer, QFile, QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,QSpinBox)







 
class Window_vocero(QDialog):
	def __init__(self, parent = None):
		super(Window_vocero, self).__init__()
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowTitle("Nuevo vocero")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(351, 268)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()

	def initUi(self):
		#Stylos =====================================================================================================		

		#Style de frame principal
		Style_frame_principal = ("QFrame{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		###

		#Style labels
		Style_labels = ("QLabel{\n"
						"background-color:#4466B8;\n"
						"color: rgb(255, 255, 255);\n"
						"border-radius: 5px\n"
						"}")
		###

		#Style line Eedit

		Style_line_edit = 				("QLineEdit{\n"
										"border-radius: 8px;\n"
										"background:#B7C0EE;\n"
										"color: #000000;\n"
										"}\n"
										"QLineEdit:hover{\n"
										"border: 1px solid #113384;\n"
										"}")
		###

		#Style frame menu

		Style_frame_menu = ("QFrame{\n"
							"background-color:#12191D;\n"
							"border-radius: 45px;\n"
							"}")
		###

		#Style de button
		
		Style_buttons = ("QPushButton{\n"
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
		###

		#Label vocero
		Style_label_vocero = ("QLabel{\n"
								"color:rgb(255, 255, 255);\n"
								"font: 14pt 'Comic Sans MS';\n"
								"border-radius: 6px;\n"
								"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
								"}")
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#frames=====================================================================================================		
		#Frame principal
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(170,20,161,231))
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)
		###

		#Frame menu
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(20,20,121,231))
		self.frame_menu.setStyleSheet(Style_frame_menu)
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Labels =====================================================================================================		
		self.label_vocero = QLabel(self.frame_menu)
		self.label_vocero.setGeometry(QRect(20,10,81,20))
		self.label_vocero.setText("vocero")
		self.label_vocero.setStyleSheet(Style_label_vocero)
		self.label_vocero.setAlignment(Qt.AlignCenter)			

		self.label_nombre = QLabel(self.frame_principal_contenido)
		self.label_nombre.setGeometry(QRect(40,20,81,16))
		self.label_nombre.setStyleSheet(Style_labels)
		self.label_nombre.setText("1°Nombre:")
		self.label_nombre.setAlignment(Qt.AlignCenter)

		self.label_apellido = QLabel(self.frame_principal_contenido)
		self.label_apellido.setGeometry(QRect(40,90,81,16))
		self.label_apellido.setStyleSheet(Style_labels)
		self.label_apellido.setText("1°Apellido:")
		self.label_apellido.setAlignment(Qt.AlignCenter)

		self.label_apellido = QLabel(self.frame_principal_contenido)
		self.label_apellido.setGeometry(QRect(40,90,81,16))
		self.label_apellido.setStyleSheet(Style_labels)
		self.label_apellido.setText("1°Apellido:")
		self.label_apellido.setAlignment(Qt.AlignCenter)

		self.label_cedula = QLabel(self.frame_principal_contenido)
		self.label_cedula.setGeometry(QRect(40,160,81,16))
		self.label_cedula.setStyleSheet(Style_labels)
		self.label_cedula.setText("Cedula:")
		self.label_cedula.setAlignment(Qt.AlignCenter)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line Edits =====================================================================================================		
		self.line_edit_nombre = QLineEdit(self.frame_principal_contenido)
		self.line_edit_nombre.setGeometry(QRect(20,40,121,21))
		self.line_edit_nombre.setText("")
		self.line_edit_nombre.setStyleSheet(Style_line_edit)
		self.line_edit_nombre.setAlignment(Qt.AlignCenter)
		self.line_edit_nombre.setPlaceholderText("Primer nombre")
		self.line_edit_nombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.line_edit_nombre))
		self.line_edit_apellido = QLineEdit(self.frame_principal_contenido)
		self.line_edit_apellido.setGeometry(QRect(20,110,121,21))
		self.line_edit_apellido.setText("")
		self.line_edit_apellido.setStyleSheet(Style_line_edit)
		self.line_edit_apellido.setAlignment(Qt.AlignCenter)
		self.line_edit_apellido.setPlaceholderText("Primer apellido")
		self.line_edit_apellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.line_edit_apellido))
		self.line_edit_cedula = QLineEdit(self.frame_principal_contenido)
		self.line_edit_cedula.setGeometry(QRect(20,180,121,21))
		self.line_edit_cedula.setText("")
		self.line_edit_cedula.setStyleSheet(Style_line_edit)
		self.line_edit_cedula.setAlignment(Qt.AlignCenter)
		self.line_edit_cedula.setPlaceholderText("Cedula")
		self.line_edit_cedula.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.line_edit_cedula))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Buttons  =====================================================================================================		
		self.Button_registra = QPushButton(self.frame_menu)
		self.Button_registra.setGeometry(QRect(0,80,121,31))
		self.Button_registra.setStyleSheet(Style_buttons)
		self.Button_registra.setText("Registrar")
		self.Button_registra.setIcon(QIcon("Imagenes-iconos/Registrar.png"))
		self.Button_registra.setIconSize(QSize(20,20))


		self.Button_cancelar = QPushButton(self.frame_menu)
		self.Button_cancelar.setGeometry(QRect(0,110,121,31))
		self.Button_cancelar.setStyleSheet(Style_buttons)
		self.Button_cancelar.setText("Registrar")
		self.Button_cancelar.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancelar.setIconSize(QSize(17,17))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		

		#EVENTOS =====================================================================================================		
		self.Button_registra.clicked.connect(self.Creater_db)
		self.Button_registra.clicked.connect(self.Nv_vocero)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

	def Creater_db(self):

		if not QFile.exists("Voceros"):
			makedirs("Voceros")

		if QFile.exists("Voceros"):
			if QFile.exists("Voceros/DB_VOCEROS.db"):
				None
			else:

				try:					
					with sqlite3.connect("Voceros/DB_VOCEROS.db") as db:
						cursor = db.cursor()


					cursor.execute("CREATE TABLE IF NOT EXISTS DATOS_VOCEROS (ID INTEGER PRIMARY KEY, PRIMER_NOMBRE TEXT,"
									"PRIMER_APELLIDO TEXT, CEDULA TEXT)")

					db.commit()
					cursor.close()
					db.close()
					QMessageBox.information(self, "Nuevo Vocero", "Vocero registrado.",
											QMessageBox.Ok)

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Vocero", "Error desconocidoB.",
											 QMessageBox.Ok)

	def Nv_vocero(self):

		nombre = self.line_edit_nombre.text()
		apellido = self.line_edit_apellido.text()
		cedula = self.line_edit_cedula.text()

		if not nombre:
			self.line_edit_nombre.setFocus()
		elif not apellido:
			self.line_edit_apellido.setFocus()
		elif not cedula:
			self.line_edit_cedula.setFocus()
		else:

			if QFile.exists("Voceros/DB_VOCEROS.db"):
				conexion = sqlite3.connect('Voceros/DB_VOCEROS.db')
				cursor = conexion.cursor()

				try:
					datos = [nombre,apellido,cedula]

					cursor.execute("INSERT INTO DATOS_VOCEROS(PRIMER_NOMBRE,PRIMER_APELLIDO,CEDULA) VALUES(?,?,?)",datos)

					conexion.commit()
					cursor.close()
					conexion.close()
					QMessageBox.information(self, "Nuevo Vocero", "Vocero registrado.",
											QMessageBox.Ok)

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Vocero", "Error desconocidoA.",
									QMessageBox.Ok)







if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_vocero()
	interface.show()
	app.exec_()