#======================================================================================================
import sqlite3
from os import getcwd, makedirs
from Source_rc import *

import sys, os
from random import randint
from PyQt5 import  uic 

from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
                             QGraphicsDropShadowEffect, QGraphicsBlurEffect,)


#======================================================================================================


 
class Interface(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("Ventana_inicial_menus.ui", self)
		self.setWindowTitle("Menu principal")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)



#========================================= #Eventos# ==================================================================

		self.buttonNewUser.clicked.connect(self.Nuevo_user)
		self.lineEditSearch.setToolTip("Ingresa la cedula de quien deseas buscar.")

#======================================== #Funciones# ==================================================================

	def Nuevo_user(self):
		Window_nv_users(self).exec_()
		

#========================================== #Classes# ===================================================================

#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+Ventana registro de usuario+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+

class Window_nv_users(QDialog):

	def __init__(self, parent=None):
		super(Window_nv_users, self).__init__()
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowTitle("Nuevo usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(887, 514)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()

	def initUi(self):

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Datos generales #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
		self.groupBox_datosGnr = QGroupBox(self)
		self.groupBox_datosGnr.setGeometry(QRect(170, 10, 341, 493))
		self.groupBox_datosGnr.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosGnr.setAlignment(Qt.AlignCenter)
		self.groupBox_datosGnr.setObjectName("groupBox_datosGnr")
		self.groupBox_datosGnr.setTitle("Datos generales")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosGnr.setGraphicsEffect(self.shadow)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#1ºNombre =====================================================================================================	
		self.label_1ºnombre = QLabel(self.groupBox_datosGnr)
		self.label_1ºnombre.setGeometry(QRect(40, 20, 71, 16))
		self.label_1ºnombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1ºnombre.setAlignment(Qt.AlignCenter)
		self.label_1ºnombre.setObjectName("label_1ºnombre")
		self.label_1ºnombre.setText("<font color='#FF3300'>*</font>1ºNombre:")

		self.lineEdit_1ºnombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1ºnombre.setGeometry(QRect(10, 40, 141, 20))
		self.lineEdit_1ºnombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1ºnombre.setText("")
		self.lineEdit_1ºnombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_1ºnombre.setObjectName("lineEdit_1ºnombre")
		self.lineEdit_1ºnombre.setPlaceholderText("Primer nombre")
		self.lineEdit_1ºnombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1ºnombre))

			

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#2ºNombre =====================================================================================================
		self.label_2ºnombre = QLabel(self.groupBox_datosGnr)
		self.label_2ºnombre.setGeometry(QRect(210, 20, 71, 16))
		self.label_2ºnombre.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2ºnombre.setAlignment(Qt.AlignCenter)
		self.label_2ºnombre.setObjectName("label_2ºnombre")
		self.label_2ºnombre.setText("2ºNombre:")

		self.lineEdit_2ºnombre = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2ºnombre.setGeometry(QRect(180, 40, 141, 20))
		self.lineEdit_2ºnombre.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2ºnombre.setText("")
		self.lineEdit_2ºnombre.setAlignment(Qt.AlignCenter)
		self.lineEdit_2ºnombre.setObjectName("lineEdit_2ºnombre")
		self.lineEdit_2ºnombre.setPlaceholderText("Segundo nombre")
		self.lineEdit_2ºnombre.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2ºnombre))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#1º Apellido =====================================================================================================		
		self.label_1ºApellido = QLabel(self.groupBox_datosGnr)
		self.label_1ºApellido.setGeometry(QRect(40, 70, 71, 16))
		self.label_1ºApellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_1ºApellido.setAlignment(Qt.AlignCenter)
		self.label_1ºApellido.setObjectName("label_1ºApellido")
		self.label_1ºApellido.setText("<font color='#FF3300'>*</font>1ºApellido:")


		self.lineEdit_1ºApellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1ºApellido.setGeometry(QRect(10, 90, 141, 20))
		self.lineEdit_1ºApellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1ºApellido.setText("")		
		self.lineEdit_1ºApellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_1ºApellido.setObjectName("lineEdit_1ºApellido")
		self.lineEdit_1ºApellido.setPlaceholderText("Primer apellido")
		self.lineEdit_1ºApellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_1ºApellido))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#2º Apellido =====================================================================================================		
		self.lineEdit_2ºApellido = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2ºApellido.setGeometry(QRect(180, 90, 141, 20))
		self.lineEdit_2ºApellido.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2ºApellido.setText("")
		self.lineEdit_2ºApellido.setAlignment(Qt.AlignCenter)
		self.lineEdit_2ºApellido.setObjectName("lineEdit_2ºApellido")

		self.label_2ºApellido = QLabel(self.groupBox_datosGnr)
		self.label_2ºApellido.setGeometry(QRect(210, 70, 71, 16))
		self.label_2ºApellido.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_2ºApellido.setAlignment(Qt.AlignCenter)
		self.label_2ºApellido.setObjectName("label_2ºApellido")
		self.label_2ºApellido.setText("2ºApellido:")
		self.lineEdit_2ºApellido.setPlaceholderText("Segundo apellido")
		self.lineEdit_2ºApellido.setValidator(QRegExpValidator(QRegExp("[A-ZÑ][a-záéíóúüñ]+"),
															self.lineEdit_2ºApellido))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	   
		#Cedula de identidad =====================================================================================================		
		self.label_cedula = QLabel(self.groupBox_datosGnr)
		self.label_cedula.setGeometry(QRect(20, 125, 121, 16))
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
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid #113384;\n"
		"}")
		self.lineEdit_cedula.setText("")
		self.lineEdit_cedula.setAlignment(Qt.AlignCenter)
		self.lineEdit_cedula.setObjectName("lineEdit_cedula")
		self.lineEdit_cedula.setPlaceholderText("Ingresa la cedula")
		self.lineEdit_cedula.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_cedula))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Telefono =====================================================================================================		
		self.label_tlf = QLabel(self.groupBox_datosGnr)
		self.label_tlf.setGeometry(QRect(210, 125, 71, 16))
		self.label_tlf.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_tlf.setAlignment(Qt.AlignCenter)
		self.label_tlf.setObjectName("label_tlf")
		self.label_tlf.setText("<font color='#FF3300'>*</font>Telefonos:")

		self.lineEdit_1ºtlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_1ºtlf.setGeometry(QRect(180, 145, 141, 20))
		self.lineEdit_1ºtlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_1ºtlf.setText("")
		self.lineEdit_1ºtlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_1ºtlf.setObjectName("lineEdit_1ºtlf")
		self.lineEdit_1ºtlf.setPlaceholderText("Principal")
		self.lineEdit_1ºtlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_1ºtlf))


		self.lineEdit_2ºtlf = QLineEdit(self.groupBox_datosGnr)
		self.lineEdit_2ºtlf.setGeometry(QRect(180, 170, 141, 20))
		self.lineEdit_2ºtlf.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_2ºtlf.setText("")
		self.lineEdit_2ºtlf.setAlignment(Qt.AlignCenter)
		self.lineEdit_2ºtlf.setObjectName("lineEdit_2ºtlf")
		self.lineEdit_2ºtlf.setPlaceholderText("Secundario")
		self.lineEdit_2ºtlf.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_2ºtlf))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Genero ========================================================================================================	      
		self.comboBox_genero = QComboBox(self.groupBox_datosGnr)
		self.comboBox_genero.setGeometry(QRect(10, 200, 141, 21))
		self.comboBox_genero.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"}\n"
		"")
		self.comboBox_genero.setEditable(False)
		self.comboBox_genero.setObjectName("comboBox_genero")


		self.items_list_genero = ["Masculino", "Femenino"]
		self.comboBox_genero.addItems(self.items_list_genero)

		self.label_genero = QLabel(self.groupBox_datosGnr)
		self.label_genero.setGeometry(QRect(40, 180, 71, 16))
		self.label_genero.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_genero.setAlignment(Qt.AlignCenter)
		self.label_genero.setObjectName("label_genero")
		self.label_genero.setText("<font color='#FF3300'>*</font>Genero:")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
				
		#Edad ========================================================================================================	      
		self.label_edad = QLabel(self.groupBox_datosGnr)
		self.label_edad.setGeometry(QRect(215, 205, 71, 16))
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
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_edad.setText("")
		self.lineEdit_edad.setAlignment(Qt.AlignCenter)
		self.lineEdit_edad.setObjectName("lineEdit_edad")
		self.lineEdit_edad.setPlaceholderText("Ingresa la edad")
		self.lineEdit_edad.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_edad))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	  
		#Fecha de nacimiento ========================================================================================================	        
		self.dateEdit_nacimiento = QDateEdit(self.groupBox_datosGnr)
		self.dateEdit_nacimiento.setGeometry(QRect(10, 255, 141, 22))
		self.dateEdit_nacimiento.setStyleSheet("QDateEdit{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"\n"
		"}")
		self.dateEdit_nacimiento.setObjectName("dateEdit_nacimiento")
		self.dateEdit_nacimiento.setDate(QDate.currentDate())
		self.dateEdit_nacimiento.setMaximumDate(QDate.currentDate())
		self.dateEdit_nacimiento.setDisplayFormat("dd/MM/yyyy")
		self.dateEdit_nacimiento.setCalendarPopup(True)
		self.dateEdit_nacimiento.setCursor(Qt.PointingHandCursor)

		self.label_fch_nacimiento = QLabel(self.groupBox_datosGnr)
		self.label_fch_nacimiento.setGeometry(QRect(20, 235, 121, 16))
		self.label_fch_nacimiento.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_fch_nacimiento.setAlignment(Qt.AlignCenter)
		self.label_fch_nacimiento.setObjectName("label_fch_nacimiento")
		self.label_fch_nacimiento.setText("Fecha de nacimiento:")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de checkbox datos generales ========================================================================================================	      
		self.label_opciones = QLabel(self.groupBox_datosGnr)
		self.label_opciones.setGeometry(QRect(180, 260, 141, 21))
		self.label_opciones.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 10px")
		self.label_opciones.setAlignment(Qt.AlignCenter)
		self.label_opciones.setObjectName("label_opciones")
		self.label_opciones.setText("Posee alguna de las opciones:")

		self.checkBox_1 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_1.setGeometry(QRect(210, 280, 81, 17))
		self.checkBox_1.setObjectName("checkBox_1")
		self.checkBox_1.setText("Pensionado")        
		
		self.checkBox_2 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_2.setGeometry(QRect(210, 300, 81, 17))
		self.checkBox_2.setObjectName("checkBox_2")
		self.checkBox_2.setText("Discapacidad")

		self.checkBox_3 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_3.setGeometry(QRect(210, 320, 81, 17))
		self.checkBox_3.setText("Enfermedad")
		self.checkBox_3.setObjectName("checkBox_3")

		self.checkBox_4 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_4.setGeometry(QRect(210, 340, 81, 17))
		self.checkBox_4.setObjectName("checkBox_4")
		self.checkBox_4.setText("Embarazada")

		self.checkBox_5 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_5.setGeometry(QRect(210, 360, 81, 17))
		self.checkBox_5.setObjectName("checkBox_5")
		self.checkBox_5.setText("Lactante")

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Profesion u oficio =================================================================================================
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
		self.comboBox_profesion.setStyleSheet("QComboBox{\n"
		"border: 0px;\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE\n"
		"}\n"
		"")
		self.comboBox_profesion.setEditable(False)
		self.comboBox_profesion.setObjectName("comboBox_profesion")

		self.items_list_profesion = ['Contador', 'Albañil', 'Conductor de autobús', 'Carnicero', 'Carpintero',
		'Cocinero','Médico','Enfermero', 'Mecánico','Herrero','Abogado','Trabajador social','Funcionario público',
		'Profesor','Veterinario', 'Otro...'
		'']

		self.comboBox_profesion.addItems(self.items_list_profesion)

		


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Nivel de instruccion ========================================================================================================	      
		self.label_nvl_instruccion = QLabel(self.groupBox_datosGnr)
		self.label_nvl_instruccion.setGeometry(QRect(25, 345, 111, 16))
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
		"}\n"
		"")
		self.comboBox_nvl_instruccion.setEditable(False)
		self.comboBox_nvl_instruccion.setObjectName("comboBox_nvl_instruccion")

		self.Items_list_instruccion = ['Primaria', 'Bachillerato', 'Técnico superior', 
		'Universitario', 'Especialización', 'Postgrado', 'Doctorado']

		self.comboBox_nvl_instruccion.addItems(self.Items_list_instruccion)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Parentesco ========================================================================================================	      
		self.label_parentesco = QLabel(self.groupBox_datosGnr)
		self.label_parentesco.setGeometry(QRect(200, 390, 101, 16))
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
		"}\n"
		"")

		self.comboBox_parentesco.setEditable(False)
		self.comboBox_parentesco.setObjectName("comboBox_parentesco")

		self.items_list_parentesco = ['Jefe/a de familia', 'Padre', 'Madre', 'Hijo/a', 'Yerno', 'Nuera', 
		'Abuelo/a', 'Nieto/a', 'Hermano/a', 'Cuñado/a', 'Bisabuelo/a', 'Biznieto/a', 'Tío/a', 'Sobrino/a']
		self.comboBox_parentesco.addItems(self.items_list_parentesco)

	   
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Estado civil ========================================================================================================	      

		self.label_estadocivil = QLabel(self.groupBox_datosGnr)
		self.label_estadocivil.setGeometry(QRect(30, 400, 101, 16))
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
		"}\n"
		"")

		self.comboBox_estadocivil.setEditable(False)
		self.comboBox_estadocivil.setObjectName("comboBox_estadocivil")
		self.items_list_estadocivil = ['Soltero', 'Casado']
		self.comboBox_estadocivil.addItems(self.items_list_estadocivil)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Inscrito en el REP ========================================================================================================	      

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
		self.radiobutton_si_inscrito.setGeometry(QRect(40, 470, 31, 17))
		self.radiobutton_si_inscrito.setObjectName("radiobutton_si_inscrito")
		self.radiobutton_si_inscrito.setText("Si")

		self.radiobutton_no_inscrito = QRadioButton(self.groupBox_datosGnr)
		self.radiobutton_no_inscrito.setGeometry(QRect(90, 470, 31, 17))
		self.radiobutton_no_inscrito.setObjectName("radiobutton_no_inscrito")
		self.radiobutton_no_inscrito.setText("No")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Ingresar el correo ========================================================================================================	      

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
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_correo.setText("")
		self.lineEdit_correo.setAlignment(Qt.AlignCenter)
		self.lineEdit_correo.setObjectName("lineEdit_correo")
		self.lineEdit_correo.setPlaceholderText("Ingresa el correo")
		#self.lineEdit_correo.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$+'),self.lineEdit_correo))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ubicacion geografica #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

		self.groupBox_datosUb = QGroupBox(self)
		self.groupBox_datosUb.setGeometry(QRect(530, 10, 341, 181))
		self.groupBox_datosUb.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datosUb.setAlignment(Qt.AlignCenter)
		self.groupBox_datosUb.setObjectName("groupBox_datosUb")
		self.groupBox_datosUb.setTitle("Ubicación geográfica")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosUb.setGraphicsEffect(self.shadow)
		#Estado ========================================================================================================	      
		self.label_estado = QLabel(self.groupBox_datosUb)
		self.label_estado.setGeometry(QRect(40, 20, 71, 16))
		self.label_estado.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_estado.setAlignment(Qt.AlignCenter)
		self.label_estado.setObjectName("label_estado")
		self.label_estado.setText("Estado:")

		self.lineEdit_estado = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_estado.setGeometry(QRect(20, 40, 111, 20))
		self.lineEdit_estado.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_estado.setText("")
		self.lineEdit_estado.setAlignment(Qt.AlignCenter)
		self.lineEdit_estado.setObjectName("lineEdit_estado")
		self.lineEdit_estado.setPlaceholderText("Ingresa el estado")
		self.lineEdit_estado.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_estado))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Municipio ========================================================================================================	      
		self.label_municipio = QLabel(self.groupBox_datosUb)
		self.label_municipio.setGeometry(QRect(40, 70, 71, 16))
		self.label_municipio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_municipio.setAlignment(Qt.AlignCenter)
		self.label_municipio.setObjectName("label_municipio")
		self.label_municipio.setText("Municipio:")

		self.lineEdit_municipio = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_municipio.setGeometry(QRect(20, 90, 111, 20))
		self.lineEdit_municipio.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_municipio.setText("")
		self.lineEdit_municipio.setAlignment(Qt.AlignCenter)
		self.lineEdit_municipio.setObjectName("lineEdit_municipio")
		self.lineEdit_municipio.setPlaceholderText("Ingresa el municipio")
		self.lineEdit_municipio.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_municipio))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Parroquia ========================================================================================================	      
		self.label_parroquia = QLabel(self.groupBox_datosUb)
		self.label_parroquia.setGeometry(QRect(40, 120, 71, 16))
		self.label_parroquia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_parroquia.setAlignment(Qt.AlignCenter)
		self.label_parroquia.setObjectName("label_parroquia")
		self.label_parroquia.setText("Parroquia:")

		self.lineEdit_parroquia = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_parroquia.setGeometry(QRect(20, 140, 111, 20))
		self.lineEdit_parroquia.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_parroquia.setText("")
		self.lineEdit_parroquia.setAlignment(Qt.AlignCenter)
		self.lineEdit_parroquia.setObjectName("lineEdit_parroquia")
		self.lineEdit_parroquia.setPlaceholderText("Ingresa la parroquia")
		self.lineEdit_parroquia.setValidator(QRegExpValidator(QRegExp("[\sA-ZÑ][\sa-záéíóúüñ]+"),
																	self.lineEdit_parroquia))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Nº de vivienda ========================================================================================================	      
		self.label_Nºvivienda = QLabel(self.groupBox_datosUb)
		self.label_Nºvivienda.setGeometry(QRect(190, 130, 111, 16))
		self.label_Nºvivienda.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_Nºvivienda.setAlignment(Qt.AlignCenter)
		self.label_Nºvivienda.setObjectName("label_Nºvivienda")
		self.label_Nºvivienda.setText("<font color='#FF3300'>*</font>Nº de vivienda:")

		self.lineEdit_Nºvivienda = QLineEdit(self.groupBox_datosUb)
		self.lineEdit_Nºvivienda.setGeometry(QRect(190, 150, 111, 20))
		self.lineEdit_Nºvivienda.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
		"}\n"
		"QLineEdit:hover{\n"
		"border: 1px solid  #113384;\n"
		"}")
		self.lineEdit_Nºvivienda.setText("")
		self.lineEdit_Nºvivienda.setAlignment(Qt.AlignCenter)
		self.lineEdit_Nºvivienda.setObjectName("lineEdit_Nºvivienda")
		self.lineEdit_Nºvivienda.setPlaceholderText("Numero de vivienda")
		self.lineEdit_Nºvivienda.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.lineEdit_Nºvivienda))

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Direccion ========================================================================================================	      
		self.label_direccion = QLabel(self.groupBox_datosUb) 
		self.label_direccion.setGeometry(QRect(210, 20, 71, 16))
		self.label_direccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_direccion.setAlignment(Qt.AlignCenter)
		self.label_direccion.setObjectName("label_direccion")
		self.label_direccion.setText("<font color='#FF3300'>*</font>Dirección:")
		self.textEdit_direccion = QTextEdit(self.groupBox_datosUb)
		self.textEdit_direccion.setGeometry(QRect(173, 40, 141, 71))
		self.textEdit_direccion.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_direccion.setObjectName("textEdit_direccion")
		self.textEdit_direccion.setPlaceholderText("Ingresa la dirección...")



		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Datos de la vivienda #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

		self.groupBox_datos_Vv = QGroupBox(self)
		self.groupBox_datos_Vv.setGeometry(QRect(530, 200, 341, 171))
		self.groupBox_datos_Vv.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_datos_Vv.setAlignment(Qt.AlignCenter)
		self.groupBox_datos_Vv.setObjectName("groupBox_datosGnr_Vv")
		self.groupBox_datos_Vv.setTitle("Datos de la vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_Vv.setGraphicsEffect(self.shadow)
		#Metros cuadrados ========================================================================================================	      
		self.label_M2 = QLabel(self.groupBox_datos_Vv)
		self.label_M2.setGeometry(QRect(30, 20, 111, 16))
		self.label_M2.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_M2.setAlignment(Qt.AlignCenter)
		self.label_M2.setObjectName("label_M2")
		self.label_M2.setText("Metros cuadrados:")

		self.lineEdit_M2 = QLineEdit(self.groupBox_datos_Vv)
		self.lineEdit_M2.setGeometry(QRect(20, 40, 131, 20))
		self.lineEdit_M2.setStyleSheet("QLineEdit{\n"
		"border-radius: 8px;\n"
		"background:#B7C0EE;\n"
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Necesita alguna reparacion ========================================================================================================	      
		self.label_reparacion = QLabel(self.groupBox_datos_Vv)
		self.label_reparacion.setGeometry(QRect(180, 130, 141, 16))
		self.label_reparacion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_reparacion.setAlignment(Qt.AlignCenter)
		self.label_reparacion.setObjectName("label_reparacion")
		self.label_reparacion.setText("Necesita alguna reparación:")

		self.radioButton_rp_si = QRadioButton(self.groupBox_datos_Vv)
		self.radioButton_rp_si.setGeometry(QRect(210, 150, 31, 17))
		self.radioButton_rp_si.setObjectName("radioButton_rp_si")
		self.radioButton_rp_si.setText("Si")

		self.radioButton_rp_no = QRadioButton(self.groupBox_datos_Vv)
		self.radioButton_rp_no.setGeometry(QRect(260, 150, 31, 17))
		self.radioButton_rp_no.setObjectName("radioButton_rp_no")
		self.radioButton_rp_no.setText("No")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Servivcios que posee ========================================================================================================	           
		self.label_servicios = QLabel(self.groupBox_datos_Vv)
		self.label_servicios.setGeometry(QRect(180, 20, 151, 16))
		self.label_servicios.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_servicios.setAlignment(Qt.AlignCenter)
		self.label_servicios.setObjectName("label_servicios")
		self.label_servicios.setText("Servicios que posee:")


		self.checkBox_aguapotable = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguapotable.setGeometry(QRect(170 ,40, 91, 17))
		self.checkBox_aguapotable.setObjectName("checkBox_aguapotable")
		self.checkBox_aguapotable.setText("Agua potable")

		self.checkBox_aguasservidas = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_aguasservidas.setGeometry(QRect(170, 60, 91, 17))
		self.checkBox_aguasservidas.setObjectName("checkBox_aguasservidas")
		self.checkBox_aguasservidas.setText("Aguas servidas")

		self.checkBox_gasdirecto = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasdirecto.setGeometry(QRect(170, 80, 91, 17))
		self.checkBox_gasdirecto.setObjectName("checkBox_gasdirecto")
		self.checkBox_gasdirecto.setText("Gas directo")

		self.checkBox_gasbombona = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_gasbombona.setGeometry(QRect(170, 100, 111, 17))
		self.checkBox_gasbombona.setObjectName("checkBox_gasbombona")
		self.checkBox_gasbombona.setText("Gas bombona")

		self.checkBox_internet = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_internet.setGeometry(QRect(260, 40, 61, 17))
		self.checkBox_internet.setObjectName("checkBox_internet")
		self.checkBox_internet.setText("Internet")

		self.checkBox_electricidad = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_electricidad.setGeometry(QRect(260, 60, 61, 17))
		self.checkBox_electricidad.setObjectName("checkBox_electricidad")
		self.checkBox_electricidad.setText("Electricidad")

		self.checkBox_tlf_fijo = QCheckBox(self.groupBox_datos_Vv)
		self.checkBox_tlf_fijo.setGeometry(QRect(260, 80, 101, 17))
		self.checkBox_tlf_fijo.setObjectName("checkBox_tlf_fijo")
		self.checkBox_tlf_fijo.setText("Telefono fijo")

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Descripcion de la vivienda ========================================================================================================	           
		self.label_dcrp_vv = QLabel(self.groupBox_datos_Vv)
		self.label_dcrp_vv.setGeometry(QRect(10, 70, 151, 16))
		self.label_dcrp_vv.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_dcrp_vv.setAlignment(Qt.AlignCenter)
		self.label_dcrp_vv.setObjectName("label_dcrp_vv")
		self.label_dcrp_vv.setText("Descripción de vivienda:")
		self.textEdit_dcrp_vv = QTextEdit(self.groupBox_datos_Vv)
		self.textEdit_dcrp_vv.setGeometry(QRect(10, 90, 151, 71))
		self.textEdit_dcrp_vv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_vv.setObjectName("textEdit_dcrp_vv")
		self.textEdit_dcrp_vv.setPlaceholderText("Describa la vivienda...")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Proteccion Social #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
	  
		self.groupBox_beneficios = QGroupBox(self)
		self.groupBox_beneficios.setGeometry(QRect(530, 380, 341, 123))
		self.groupBox_beneficios.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_beneficios.setAlignment(Qt.AlignCenter)
		self.groupBox_beneficios.setObjectName("groupBox_beneficios")
		self.groupBox_beneficios.setTitle("Proteccion social")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_beneficios.setGraphicsEffect(self.shadow)

		#Posee algun beneficio ========================================================================================================	           
		self.label_beneficio = QLabel(self.groupBox_beneficios)
		self.label_beneficio.setGeometry(QRect(10, 20, 161, 16))
		self.label_beneficio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_beneficio.setAlignment(Qt.AlignCenter)
		self.label_beneficio.setObjectName("label_beneficio")
		self.label_beneficio.setText("Posee algun beneficio:")

		self.checkBox_hogarespatria = QCheckBox(self.groupBox_beneficios)
		self.checkBox_hogarespatria.setGeometry(QRect(10, 40, 121, 17))
		self.checkBox_hogarespatria.setObjectName("checkBox_hogarespatria")
		self.checkBox_hogarespatria.setText("Hogares de la patria")


		self.checkBox_partohumanizado = QCheckBox(self.groupBox_beneficios)
		self.checkBox_partohumanizado.setGeometry(QRect(10, 100, 111, 20))
		self.checkBox_partohumanizado.setObjectName("checkBox_partohumanizado")
		self.checkBox_partohumanizado.setText("Parto humanizado")

		self.checkBox_amormayor = QCheckBox(self.groupBox_beneficios)
		self.checkBox_amormayor.setGeometry(QRect(10, 60, 81, 17))
		self.checkBox_amormayor.setObjectName("checkBox_amormayor")
		self.checkBox_amormayor.setText("Amor mayor")

		self.checkBox_joseGregorio  = QCheckBox(self.groupBox_beneficios)
		self.checkBox_joseGregorio.setGeometry(QRect(10, 80, 161, 17))
		self.checkBox_joseGregorio.setObjectName("checkBox_joseGregorio")
		self.checkBox_joseGregorio.setText("Dr. José Gregorio Hernández")

		self.label_grpsociales = QLabel(self.groupBox_beneficios)
		self.label_grpsociales.setGeometry(QRect(185,20,141,16))
		self.label_grpsociales.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_grpsociales.setAlignment(Qt.AlignCenter)
		self.label_grpsociales.setObjectName("label_grpsociales")
		self.label_grpsociales.setText("Esta en algun grupo social:")


		self.checkBox_somosvenezuela = QCheckBox(self.groupBox_beneficios)
		self.checkBox_somosvenezuela.setGeometry(QRect(190, 60, 111, 17))
		self.checkBox_somosvenezuela.setObjectName("checkBox_somosvenezuela")
		self.checkBox_somosvenezuela.setText("Somos Venezuela")

		self.checkBox_chambajuvenil = QCheckBox(self.groupBox_beneficios)
		self.checkBox_chambajuvenil.setGeometry(QRect(190, 40, 111, 17))
		self.checkBox_chambajuvenil.setObjectName("checkBox_chambajuvenil")
		self.checkBox_chambajuvenil.setText("Chamba juvenil")

		self.checkBox_FrenteMiranda = QCheckBox(self.groupBox_beneficios)
		self.checkBox_FrenteMiranda.setGeometry(QRect(190, 80, 141, 17))
		self.checkBox_FrenteMiranda.setObjectName("checkBox_FrenteMiranda")
		self.checkBox_FrenteMiranda.setText("Frente Francisco Miranda")

		self.checkBox_jpsuv = QCheckBox(self.groupBox_beneficios)
		self.checkBox_jpsuv.setGeometry(QRect(190, 100, 141, 17))
		self.checkBox_jpsuv.setObjectName("checkBox_jpsuv")
		self.checkBox_jpsuv.setText("JPSUV")

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#========================================== #Lineas# =======================================================================================

		#Line bajo Nombre-Apellido =====================================================================================	
		self.line = QFrame(self.groupBox_datosGnr)
		self.line.setGeometry(QRect(10, 110, 311, 16))
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)
		self.line.setObjectName("line")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Line bajo cedula ==============================================================================================		
		self.line_5 = QFrame(self.groupBox_datosGnr)
		self.line_5.setGeometry(QRect(10, 165, 141, 16))
		self.line_5.setFrameShape(QFrame.HLine)
		self.line_5.setFrameShadow(QFrame.Sunken)
		self.line_5.setObjectName("line_5")		       
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo telefono ===========================================================================================		 
		self.line_3 = QFrame(self.groupBox_datosGnr)
		self.line_3.setGeometry(QRect(180, 190, 141, 16))
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo genero ========================================================================================================	      
		self.line_2 = QFrame(self.groupBox_datosGnr)
		self.line_2.setGeometry(QRect(10, 220, 141, 16))
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	   
		#Line bajo edad ========================================================================================================	      
		self.line_8 = QFrame(self.groupBox_datosGnr)
		self.line_8.setGeometry(QRect(180, 245, 141, 16))
		self.line_8.setFrameShape(QFrame.HLine)
		self.line_8.setFrameShadow(QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo fecha de nacimiento ==========================================================================================      
		self.line_4 = QFrame(self.groupBox_datosGnr)
		self.line_4.setGeometry(QRect(10, 275, 141, 16))
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	   
		#Line bajo profesion u oficio ==========================================================================================      
		self.line_6 = QFrame(self.groupBox_datosGnr)
		self.line_6.setGeometry(QRect(10, 330, 141, 16))
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo nivel de instruccion ==========================================================================================      
		self.line_7 = QFrame(self.groupBox_datosGnr)
		self.line_7.setGeometry(QRect(10, 385, 141, 16))
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)
		self.line_7.setObjectName("line_7")       
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Line bajo opciones checkbox ==========================================================================================      
		self.line_9 = QFrame(self.groupBox_datosGnr)
		self.line_9.setGeometry(QRect(180, 375, 141, 16))
		self.line_9.setFrameShape(QFrame.HLine)
		self.line_9.setFrameShadow(QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#		
		
		#Line bajo estado civil ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(10, 440, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#		

		#Line bajo parentesco ==========================================================================================      
		self.line_20 = QFrame(self.groupBox_datosGnr)
		self.line_20.setGeometry(QRect(180, 430, 141, 16))
		self.line_20.setFrameShape(QFrame.HLine)
		self.line_20.setFrameShadow(QFrame.Sunken)
		self.line_20.setObjectName("line_20")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#		


		#Line bajo direccion ==========================================================================================      
		self.line_10 = QFrame(self.groupBox_datosUb)
		self.line_10.setGeometry(QRect(173, 110, 141, 16))
		self.line_10.setFrameShape(QFrame.HLine)
		self.line_10.setFrameShadow(QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo metros cuadrados ==========================================================================================      
		self.line_11 = QFrame(self.groupBox_datos_Vv)
		self.line_11.setGeometry(QRect(20, 58, 131, 16))
		self.line_11.setFrameShape(QFrame.HLine)
		self.line_11.setFrameShadow(QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Line bajo servicios que posee ==========================================================================================      
		self.line_12 = QFrame(self.groupBox_datos_Vv)
		self.line_12.setGeometry(QRect(170, 115, 161, 20))
		self.line_12.setFrameShape(QFrame.HLine)
		self.line_12.setFrameShadow(QFrame.Sunken)
		self.line_12.setObjectName("line_12")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		self.frame = QFrame(self)
		self.frame.setGeometry(QRect(20, 10, 121, 493))
		self.frame.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px\n"
		"\n"
		"}")
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setFrameShadow(QFrame.Raised)
		self.frame.setObjectName("frame")

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)


		self.label_13 = QLabel(self.frame)
		self.label_13.setGeometry(QRect(25, 10, 141, 20))
		self.label_13.setText("USUARIO")	
		self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font: 75 11pt \"Comic Sans MS\";\n"
		"border-radius:6px\n"
		"")
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ BOTONES DE LA VENTANA DE REGISTRO DE USUARIO #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
		
		#Boton registrar ==========================================================================================      		
		self.Button_register_user = QPushButton(self.frame)
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton cancelar ==========================================================================================      		
		self.Button_cancel_user = QPushButton(self.frame)
		self.Button_cancel_user.setGeometry(QRect(0, 120, 121, 31))
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
		self.Button_cancel_user.setObjectName("Button_cancel_user")
		self.Button_cancel_user.setText("Cancelar")		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ FIN DE BOTONES DE LA VENTANA DE REGISTRO DE USUARIO #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

#========================================= #Eventos# ==================================================================

		self.Button_register_user.clicked.connect(self.Creater_base_datos)

		self.Button_register_user.clicked.connect(self.New_user)

		self.checkBox_2.clicked.connect(self.Descripcion_discapacidad)

		self.radioButton_rp_si.clicked.connect(self.Descripcion_reparacion)

		self.checkBox_3.clicked.connect(self.Descripcion_enfermedad)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


#========================================= #Funciones# ==================================================================
	def Descripcion_enfermedad(self):
		Window_enfermedad(self).exec_()

	#Funcion para abrir ventana de descripcion de reparacion de vivienda ==========================================================================================      			

	def Descripcion_reparacion(self):
		Window_reparacionvivienda(self).exec_()

	#Funcion para abrir ventan de descripcion de discapacidad ==========================================================================================      			
	
	def Descripcion_discapacidad(self):		
		Window_discapacidad(self).exec_()

	#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

	#Funcion para crecar nuevo usuario ==========================================================================================      		

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

																			"PENSIONADO TEXT, ENFERMEDAD TEXT, EMBARAZADA TEXT, LACTANTE TEXT)")

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
																					"DIRECCION TEXT, Nº_VIVIENDA)")


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
									"AGUA_POTABLE TEXT, AGUA_SERVIDAS TEXT, GAS_DIRECTO TEXT, GAS_BOMBONA TEXT, INTERNET TEXT, ElECTRICIDAD TEXT,"
									"TELEFONO_FIJO TEXT)")



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

		#Datos Generales
		nombre_1 = self.lineEdit_1ºnombre.text() 
		nombre_2 = self.lineEdit_2ºnombre.text()
		apellido_1 = self.lineEdit_1ºApellido.text()
		apellido_2 = self.lineEdit_2ºApellido.text()
		cedula_identidad = self.lineEdit_cedula.text()
		telefono_princ = self.lineEdit_1ºtlf.text()
		telefono_secund = self.lineEdit_2ºtlf.text()
		genero = self.comboBox_genero.currentText()
		edad = self.lineEdit_edad.text()
		fecha_Nacimiento = self.dateEdit_nacimiento.text()
		profesion_oficio = self.comboBox_profesion.currentText()
		nivel_instruccion = self.comboBox_nvl_instruccion.currentText()
		parentesco = self.comboBox_parentesco.currentText()
		opcion_pensionado = self.checkBox_1.text()
		#opcion_discapacidad = self.checkBox_2.text()
		opcion_enfermedad = self.checkBox_3.text()
		opcion_embarazada = self.checkBox_4.text()
		opcion_lactante = self.checkBox_5.text()
		estado_civil = self.comboBox_estadocivil.currentText()
		inscrito_rep = self.RadioButton_rep()
		correo_electronico = self.lineEdit_correo.text()

				#Ubicacion geografica			
		estado = self.lineEdit_estado.text()
		municipio = self.lineEdit_municipio.text()
		parroquia = self.lineEdit_parroquia.text()
		numero_vivienda = self.lineEdit_Nºvivienda.text()
		dirección = self.textEdit_direccion.toPlainText()


		#Datos de la vivienda
		metros_cuadrados = self.lineEdit_M2.text()
		descripcion_vivienda = self.textEdit_dcrp_vv.toPlainText()
		reparaciones = self.RadioButton_reparacion()
		servicio_aguapotable = self.CheckBox_aguapotable()
		servicio_aguaservidas = self. CheckBox_aguaservidas()
		servicio_gasdirecto = self.CheckBox_gasdirecto()
		servicio_gasbombona = self.CheckBox_gasbombona()
		servicio_internet = self.CheckBox_internet()
		servicio_electricidad = self.CheckBox_electricidad()
		servicio_tlf_fijo = self.CheckBox_telefonofijo()

		#Proteccion Social
		hogaresdelapatria = self.CheckBox_hogaresdelapatria()
		amormayor = self.CheckBox_amormayor()
		josegregorio = self.CheckBox_josegregorio()
		partohumanizado = self.CheckBox_partohumanizado()
		#=============
		chambajuvenil = self.CheckBox_chambajuvenil()
		somosvenezuela = self.CheckBox_somosvenezuela()
		frentemiranda = self.CheckBox_frentemiranda()
		jpsuv = self.CheckBox_jpsuv()
				
				
		if not nombre_1:
			self.lineEdit_1ºnombre.setFocus()
		elif not apellido_1:
			self.lineEdit_1ºApellido.setFocus()
		elif not cedula_identidad:
			self.lineEdit_cedula.setFocus()
		elif not telefono_princ:
			self.lineEdit_1ºtlf.setFocus()
		elif not genero:
			self.comboBox_genero.setFocus()
		elif not numero_vivienda:
			self.lineEdit_Nºvivienda.setFocus()
		elif not dirección:
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
					datos_insertar_Gnr = [nombre_1, nombre_2, apellido_1, apellido_2,
									cedula_identidad, genero, telefono_princ, telefono_secund,
									fecha_Nacimiento, edad, profesion_oficio, nivel_instruccion,
									parentesco, estado_civil, inscrito_rep, correo_electronico,
									opcion_pensionado,opcion_enfermedad, opcion_embarazada,
									opcion_lactante]

					cursor.execute("INSERT INTO USUARIO_DT_GNR (PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO , SEGUNDO_APELLIDO,"
									"CEDULA, GENERO, TELEFONO_PRINCIPAL, TELEFONO_SECUNDARIO,"
									"FECHA_NACIMIENTO, EDAD, PROFESION_OFICIO, NIVEL_INSTRUCCION,"
									"PARENTESCO, ESTADO_CIVIL, INSCRITO_REP, CORREO_ELECTRONICO,"
									"PENSIONADO, ENFERMEDAD, EMBARAZADA, LACTANTE) VALUES(?,?,?,?,"
									"?,?,?,?,"
									"?,?,?,?,"
									"?,?,?,?,"
									"?,?,?,?)", datos_insertar_Gnr)
					

					idusuario = cursor.lastrowid
					conexion.commit()		
					cursor.close()
					conexion.close()
					QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",
														   QMessageBox.Ok)
				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
								 QMessageBox.Ok)



			if QFile.exists("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db')
				cursor = conexion.cursor()

			try:		
				datos_insertar_Ubc = [estado, municipio,parroquia,dirección,numero_vivienda]

				cursor.execute("INSERT INTO USUARIO_UBCGEOG VALUES(NULL,?,?,?,?,?)", datos_insertar_Ubc)
				conexion.commit()		
				cursor.close()
				conexion.close()

				QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",
															   QMessageBox.Ok)
			except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
								 QMessageBox.Ok)

				
			if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db')
				cursor = conexion.cursor()
	
			try:		
				datos_insertar_Vv = [metros_cuadrados, descripcion_vivienda, reparaciones, servicio_aguapotable,
									servicio_aguaservidas, servicio_gasdirecto, servicio_gasbombona, servicio_internet,
									servicio_electricidad, servicio_tlf_fijo]

				cursor.execute("INSERT INTO USUARIO_DT_VV VALUES(NULL,?,?,?,?,?,"
															  "?,?,?,?,?)", datos_insertar_Vv)
				conexion.commit()		
				cursor.close()
				conexion.close()

				QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",
											   QMessageBox.Ok)
			except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
									QMessageBox.Ok)


				
			if QFile.exists("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_PROT_SOCIAL.db')
				cursor = conexion.cursor()

				try:		
					datos_insertar_Prot = [hogaresdelapatria, amormayor,josegregorio,partohumanizado,
										chambajuvenil, somosvenezuela,frentemiranda, jpsuv]

					cursor.execute("INSERT INTO USUARIO_PROT_SOCIAL VALUES(NULL,?,?,?,?,"
																			"?,?,?,?)", datos_insertar_Prot)
					conexion.commit()		
					cursor.close()
					conexion.close()

					QMessageBox.information(self, "Nuevo usuario", "Usuario registrado.",
													   QMessageBox.Ok)
				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Nuevo Usuario", "Error desconocido.",
									QMessageBox.Ok)



			self.lineEdit_1ºnombre.clear() 
			self.lineEdit_2ºnombre.clear()
			self.lineEdit_1ºApellido.clear()
			self.lineEdit_2ºApellido.clear()
			self.lineEdit_cedula.clear()
			self.lineEdit_1ºtlf.clear()
			self.lineEdit_2ºtlf.clear()
			self.comboBox_genero.setCurrentIndex(-1)
			self.lineEdit_edad.clear()
			self.dateEdit_nacimiento.setDate(QDate.currentDate())
			self.comboBox_profesion.setCurrentIndex(-1)
			self.comboBox_nvl_instruccion.setCurrentIndex(-1)
			self.comboBox_parentesco.setCurrentIndex(-1)
			#self.checkBox_1.clear()
			#self.checkBox_2.clear()
			#self.checkBox_3.clear()
			#self.checkBox_4.clear()
			#self.checkBox_5.clear()
			self.comboBox_estadocivil.setCurrentIndex(-1)
			#self.RadioButton_rep.clear()
			self.lineEdit_correo.clear()

					#Ubicacion geografica			
			self.lineEdit_estado.clear()
			self.lineEdit_municipio.clear()
			self.lineEdit_parroquia.clear()
			self.lineEdit_Nºvivienda.clear()
			self.textEdit_direccion.clear()


			#Datos de la vivienda
			self.lineEdit_M2.clear()
			self.textEdit_dcrp_vv.clear()
			#self.RadioButton_reparacion.clear()
			#self.CheckBox_aguapotable.clear()
			#self.CheckBox_aguaservidas.clear()
			#self.CheckBox_gasdirecto.clear()
			#self.CheckBox_gasbombona.clear()
			#self.CheckBox_internet.clear()
			#self.CheckBox_electricidad.clear()
			#self.CheckBox_telefonofijo.clear()

			#Proteccion Social
			#self.CheckBox_hogaresdelapatria.clear()
			#self.CheckBox_amormayor.clear()
			#self.CheckBox_josegregorio.clear()
			#self.CheckBox_partohumanizado.clear()
			#=============
			#self.CheckBox_chambajuvenil.clear()
			#self.CheckBox_somosvenezuela.clear()
			#self.CheckBox_frentemiranda.clear()
			#self.CheckBox_jpsuv.clear()
						

	#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	

	###################################### Funciones para los radio button y Checkbox #########################################
	#Funcion para el RadioButton de si necesita alguna reparacion ==========================================================================================      			
	def RadioButton_reparacion(self):
		
		if self.radioButton_rp_si.isChecked():
			
			return "Si"

		elif self.radioButton_rp_no.isChecked():
			return "No"

		else:
			None

	#Funcion de si esta inscrito en el REP =============================================================================================
	def RadioButton_rep(self):

		if self.radiobutton_si_inscrito.isChecked():
			return "Si"

		elif self.radiobutton_no_inscrito.isChecked():
			return "No"

		else:
			None

	#CheckBox de servicios que posee ==================================================================================================
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

	#Proteccion Social =======================================================================================
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







	#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	

#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ Fin de la Ventana registro de usuario+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+





















#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ Ventana de Discapacidad +/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+


class Window_discapacidad(QDialog):
	def __init__(self, parent = None):
		super(Window_discapacidad, self).__init__()

		self.setObjectName("Dialog")
		self.setWindowTitle("Discapacidad")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.resize(555, 294)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()

	def initUi(self):

		#Group de discapacidad ========================================================================================================	           
		self.groupBox_datosdiscapacidad = QGroupBox(self)
		self.groupBox_datosdiscapacidad.setGeometry(QRect(160, 20, 381, 251))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Descripcion de discapacidad ========================================================================================================	           
		self.textEdit_dcrp_discapacidad = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_dcrp_discapacidad.setGeometry(QRect(230, 40, 141, 91))
		self.textEdit_dcrp_discapacidad.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_discapacidad.setObjectName("textEdit_dcrp_discapacidad")
		self.textEdit_dcrp_discapacidad.setPlaceholderText("Describa la discapacidad...")

		
		self.dcrp_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.dcrp_discapacidad.setGeometry(QRect(235, 20, 131, 16))
		self.dcrp_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_discapacidad.setAlignment(Qt.AlignCenter)
		self.dcrp_discapacidad.setObjectName("dcrp_discapacidad")
		self.dcrp_discapacidad.setText("Describa la discapacidad:")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de discapacidad ========================================================================================================	           
		self.label_opciones_discapacidad = QLabel(self.groupBox_datosdiscapacidad)
		self.label_opciones_discapacidad.setGeometry(QRect(10, 20, 201, 16))
		self.label_opciones_discapacidad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opciones_discapacidad.setAlignment(Qt.AlignCenter)
		self.label_opciones_discapacidad.setObjectName("label_opciones_discapacidad")
		self.label_opciones_discapacidad.setText("Posee alguna de estas discapacidades:")

		self.checkBox_27 =QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_27.setGeometry(QRect(20, 120, 200, 17))
		self.checkBox_27.setText("Discapacidad Motriz")
		self.checkBox_27.setToolTip("Implica una disminución de la movilidad total o parcial \n" 
									"de uno o más miembros del cuerpo, la cual dificulta la realización\n"
									"de actividades motoras convencionales.")
		self.checkBox_27.setObjectName("checkBox_27")

		self.checkBox_26 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_26.setGeometry(QRect(20, 80, 200, 17))
		self.checkBox_26.setText("Discapacidad Auditiva")
		self.checkBox_26.setToolTip("Es un déficit total o parcial en la percepción que se evalúa\n" 
									"por el grado de pérdida de la audición en cada oído")
		self.checkBox_26.setObjectName("checkBox_26")

		self.checkBox_25 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_25.setGeometry(QRect(20, 60, 200, 17))
		self.checkBox_25.setText("Discapacidad Visual")
		self.checkBox_25.setObjectName("checkBox_25")
		self.checkBox_25.setToolTip("Es de acuerdo al grado de limitación de la visión, se suele distinguir entre personas ciegas,\n" 
									"que no obtienen información a través del canal visual; y personas con disminución visual,\n"
									"quienes en cambio sí la adquieren mediante dicho canal pero con algún déficit.")

		self.checkBox_23 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_23.setGeometry(QRect(20, 40, 200, 17))
		self.checkBox_23.setText("Discapacidad Intelectual o mental")
		self.checkBox_23.setObjectName("checkBox_23")
		self.checkBox_23.setToolTip("Las personas con discapacidad intelectual tienen algunas limitaciones\n"
									"para funcionar en su vida diaria; les cuesta más aprender habilidades\n"
									"sociales e intelectuales para acutar en diferentes situaciones.")
		self.checkBox_24 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_24.setGeometry(QRect(20, 100, 200, 17))
		self.checkBox_24.setText("Discapacidad visceral")
		self.checkBox_24.setObjectName("checkBox_24")
		self.checkBox_24.setToolTip("Las personas con discapacidad visceral son aquellos individuos que, debido a alguna deficiencia \n"
									"en la función de órganos internos, por ejemplo, el cardíaco o el diabético, se encuentran impedidas de \n"
									"desarrollar su vida con total plenitud (aunque no tengan complicaciones en el campo intelectual, \n"
									"en sus funciones sensoriales o motoras)")
		self.checkBox_otras = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otras.setGeometry(QRect(20, 140, 200, 17))
		self.checkBox_otras.setText("Otra...")
		self.checkBox_otras.setObjectName("checkBox_otras")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de medicamentos ========================================================================================================	           
		self.label_medicamentos = QLabel(self.groupBox_datosdiscapacidad)
		self.label_medicamentos.setGeometry(QRect(235, 140, 131, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")		
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_si_medicamentos.setGeometry(QRect(260, 160, 41, 17))
		self.radioButton_si_medicamentos.setObjectName("radioButton_si_medicamentos")
		self.radioButton_si_medicamentos.setText("Si")

		self.radioButton_no_medicamentos = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_no_medicamentos.setGeometry(QRect(310, 160, 41, 17))
		self.radioButton_no_medicamentos.setObjectName("radioButton_no_medicamentos")
		self.radioButton_no_medicamentos.setText("No")

		self.textEdit_medicamento = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_medicamento.setGeometry(QRect(230, 180, 141, 61))
		self.textEdit_medicamento.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento.setObjectName("textEdit_medicamento")
		self.textEdit_medicamento.setPlaceholderText("Escriba el medicamento...")

		self.label_insumomedico = QLabel(self.groupBox_datosdiscapacidad)
		self.label_insumomedico.setGeometry(QRect(30, 160, 160, 16))
		self.label_insumomedico.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")		
		self.label_insumomedico.setAlignment(Qt.AlignCenter)
		self.label_insumomedico.setObjectName("label_insumomedico")
		self.label_insumomedico.setText("Necesita algún insumo medico:")

		self.checkBox_sillarueda = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_sillarueda.setGeometry(QRect(20, 180, 200, 17))
		self.checkBox_sillarueda.setText("Silla de rueda")
		self.checkBox_sillarueda.setObjectName("checkBox_sillarueda")

		self.checkBox_muletas = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_muletas.setGeometry(QRect(20, 195, 200, 17))
		self.checkBox_muletas.setText("Muletas")
		self.checkBox_muletas.setObjectName("checkBox_muletas")

		self.checkBox_protesis = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_protesis.setGeometry(QRect(20, 210, 200, 17))
		self.checkBox_protesis.setText("Prótesis")
		self.checkBox_protesis.setObjectName("checkBox_protesis")

		self.checkBox_otros = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_otros.setGeometry(QRect(20, 225, 200, 17))
		self.checkBox_otros.setText("Otros...")
		self.checkBox_otros.setObjectName("checkBox_otros")

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.frame_2 = QFrame(self)
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
		# ========================================================================================================	           

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ BOTONES DE LA VENTANA DE DISCAPACIDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		
		
		#Boton Aceptar ==========================================================================================      		
		self.pushButton_aceptar = QPushButton(self.frame_2)
		self.pushButton_aceptar.setGeometry(QRect(-10, 80, 141, 31))
		self.pushButton_aceptar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_aceptar.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar.setText("Aceptar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Boton Cancelar ==========================================================================================      		
		self.pushButton_cancelar = QPushButton(self.frame_2)
		self.pushButton_cancelar.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_cancelar.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar.setText("Cancelar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
 
		###################################### Eventos #########################################################
		self.pushButton_aceptar.clicked.connect(self.Guardar_datos)




		#Funcion para guardar los datos de discapacidad==========================================================================
	def Guardar_datos(self):

			descripcion_discapacidad = self.textEdit_dcrp_discapacidad.toPlainText()
			tipo_de_discapacidad = self.tipo_discapacidad()
			necesita_algun_medicamento = self.necesita_medicamento()
			descripcion_medicamento = self.textEdit_medicamento.toPlainText()
			insumos_medicos = self.insumomedico()


			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db')
				cursor = conexion.cursor()
				

				try:
					datos_insertar_Gnr = [tipo_de_discapacidad, insumos_medicos,descripcion_discapacidad,
										  necesita_algun_medicamento, descripcion_medicamento]


					cursor.execute("INSERT INTO USUARIO_DT_GNR (POSEE_DISCAPACIDAD, NECESITA_INSUMO_MEDICO?, DESCRIBA_DISCAPACIDAD,"
								   "TOMA_MEDICAMENTO, DESCRIBA_MEDICAMENTO) VALUES(?,?,?,?,?)", datos_insertar_Gnr)

					conexion.commit()
					cursor.close()
					conexion.close()

					QMessageBox.information(self, "Discapacidad", "Datos guardados con exito."
											"   ", QMessageBox.Ok)
				except Exception as e:
					print(e)					
					QMessageBox.critical(self, "Discapacidad", "Error desconocido.",
										 QMessageBox.Ok)

			else:
				if not QFile.exists("Base de datos"):
					makedirs("Base de datos")

				if QFile.exists("Base de datos"):
					try:
						datos_insertar_Gnr = [tipo_de_discapacidad, insumos_medicos,descripcion_discapacidad,
						necesita_algun_medicamento, descripcion_medicamento]

						with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db') as db:
							cursor = db.cursor()
					
						cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_DT_GNR (ID INTEGER PRIMARY KEY,PRIMER_NOMBRE TEXT,"

																			"SEGUNDO_NOMBRE TEXT, PRIMER_APELLIDO TEXT, SEGUNDO_APELLIDO TEXT,"

																			"CEDULA TEXT, GENERO TEXT, TELEFONO_PRINCIPAL TEXT," 

																			"TELEFONO_SECUNDARIO TEXT, FECHA_NACIMIENTO TEXT, EDAD TEXT,"

																			"PROFESION_OFICIO TEXT, NIVEL_INSTRUCCION TEXT, PARENTESCO TEXT,"

																			"ESTADO_CIVIL TEXT, INSCRITO_REP TEXT, CORREO_ELECTRONICO TEXT,"

																			"PENSIONADO TEXT, POSEE_DISCAPACIDAD TEXT,NECESITA_INSUMO_MEDICO TEXT,"

																			"DESCRIBA_DISCAPACIDAD TEXT, TOMA_MEDICAMENTO TEXT, DESCRIBA_MEDICAMENTO TEXT,"
																			
																			"ENFERMEDAD TEXT, EMBARAZADA TEXT, LACTANTE TEXT)")


						cursor.execute("INSERT INTO USUARIO_DT_GNR(POSEE_DISCAPACIDAD, NECESITA_INSUMO_MEDICO, DESCRIBA_DISCAPACIDAD,TOMA_MEDICAMENTO, DESCRIBA_MEDICAMENTO) VALUES (?,?,?,"
									   "?,?)", datos_insertar_Gnr)										  

						db.commit()
						cursor.close()
						db.close()

						QMessageBox.information(self, "Discapacidad", "Datos guardados con exito."
												"   ", QMessageBox.Ok)
						self.close()
					except Exception as e:
						print(e)					
						QMessageBox.critical(self, "Discapacidad", "Error desconocidoAA.",
											 QMessageBox.Ok)

					#QMessageBox.critical(self, "Discapacidad", "No se encontro la base de "
										 #"datos.", QMessageBox.Ok)

				


	def insumomedico(self):
			if self.checkBox_sillarueda.isChecked():
				return "Necesita silla de rueda"
			elif self.checkBox_muletas.isChecked():
				return "Necesita muletas"
			elif self.checkBox_protesis.isChecked():
				return "Necesita protesis"
			elif self.checkBox_otros.isChecked():
				return "Otros..."
			else:
				None

	def necesita_medicamento(self):

			if self.radioButton_si_medicamentos.isChecked():
				return "Si"

			elif self.radioButton_no_medicamentos.isChecked():
				return "None"
			else:
				None

	def tipo_discapacidad(self):

			if self.checkBox_27.isChecked():
				return "Discapacidad Motriz"
			elif self.checkBox_26.isChecked():
				return "Discapacidad Auditiva"
			elif self.checkBox_25.isChecked():
				return "Discapacidad Visual"
			elif self.checkBox_23.isChecked():
				return "Discapacidad Intelectual o Mental"
			elif self.checkBox_24.isChecked():
				return "Discapacidad Visceral"
			elif self.checkBox_otras.isChecked():
				return "Otras..."
			else:
				None





#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ FIN DE BOTONES DE LA VENTANA DE DISCAPACIDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+	








#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ VENTANA DE ENFERMEDAD +/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+


class Window_enfermedad(QDialog):
	def __init__(self, parent = None):
		super(Window_enfermedad, self).__init__()

		self.setWindowTitle("Enfermedad")
		self.setObjectName("Dialog")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.resize(555, 294)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		#Group de enfermedad ========================================================================================================	           
		self.groupBox_datos_enfermedad = QGroupBox(self)
		self.groupBox_datos_enfermedad.setGeometry(QRect(160, 20, 381, 251))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Descripcion de enfermedad ========================================================================================================	           
		self.textEdit_dcrp_enfermedad = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_dcrp_enfermedad.setGeometry(QRect(230, 40, 141, 91))
		self.textEdit_dcrp_enfermedad.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_enfermedad.setObjectName("textEdit_dcrp_enfermedad")
		self.textEdit_dcrp_enfermedad.setPlaceholderText("Describa la enfermedad...")

		
		self.dcrp_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.dcrp_enfermedad.setGeometry(QRect(235, 20, 131, 16))
		self.dcrp_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.dcrp_enfermedad.setAlignment(Qt.AlignCenter)
		self.dcrp_enfermedad.setObjectName("dcrp_enfermedad")
		self.dcrp_enfermedad.setText("Describa la enfermedad:")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de enfermedad ========================================================================================================	           
		self.label_opciones_enfermedad = QLabel(self.groupBox_datos_enfermedad)
		self.label_opciones_enfermedad.setGeometry(QRect(10, 20, 201, 16))
		self.label_opciones_enfermedad.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opciones_enfermedad.setAlignment(Qt.AlignCenter)
		self.label_opciones_enfermedad.setObjectName("label_opciones_enfermedad")
		self.label_opciones_enfermedad.setText("Posee alguna de estas enfermedades:")

		self.checkBox_27 =QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_27.setGeometry(QRect(20, 120, 70, 17))
		self.checkBox_27.setText("Cáncer")
		self.checkBox_27.setObjectName("checkBox_27")

		self.checkBox_26 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_26.setGeometry(QRect(20, 80, 70, 17))
		self.checkBox_26.setText("Diabetes")
		self.checkBox_26.setObjectName("checkBox_26")

		self.checkBox_25 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_25.setGeometry(QRect(20, 60, 200, 17))
		self.checkBox_25.setText("Hipertensión arterial")
		self.checkBox_25.setObjectName("checkBox_25")

		self.checkBox_23 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_23.setGeometry(QRect(20, 40, 70, 17))
		self.checkBox_23.setText("Asma")
		self.checkBox_23.setObjectName("checkBox_23")

		self.checkBox_24 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_24.setGeometry(QRect(20, 100, 200, 17))
		self.checkBox_24.setText("Cardio Vascular")
		self.checkBox_24.setObjectName("checkBox_24")

		self.checkBox_28 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_28.setGeometry(QRect(20, 140, 70, 17))
		self.checkBox_28.setText("Gastritis")
		self.checkBox_28.setObjectName("checkBox_28")

		self.checkBox_29 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_29.setGeometry(QRect(20, 160, 70, 17))
		self.checkBox_29.setText("Bronquitis")
		self.checkBox_29.setObjectName("checkBox_29")

		self.checkBox_30 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_30.setGeometry(QRect(20, 180, 200, 17))
		self.checkBox_30.setText("Cálculos de riñón")
		self.checkBox_30.setObjectName("checkBox_30")

		self.checkBox_31 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_31.setGeometry(QRect(20, 200, 70, 17))
		self.checkBox_31.setText("Sinusitis")
		self.checkBox_31.setObjectName("checkBox_31")

		self.checkBox_32 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_32.setGeometry(QRect(20, 220, 70, 17))
		self.checkBox_32.setText("Otra...")
		self.checkBox_32.setObjectName("checkBox_32")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de medicamentos ========================================================================================================	           
		self.label_medicamentos = QLabel(self.groupBox_datos_enfermedad)
		self.label_medicamentos.setGeometry(QRect(235, 140, 131, 16))
		self.label_medicamentos.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")		
		self.label_medicamentos.setAlignment(Qt.AlignCenter)
		self.label_medicamentos.setObjectName("label_medicamentos")
		self.label_medicamentos.setText("Toma algun medicamento:")

		self.radioButton_si_medicamentos = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_si_medicamentos.setGeometry(QRect(260, 160, 41, 17))
		self.radioButton_si_medicamentos.setObjectName("radioButton_si_medicamentos")
		self.radioButton_si_medicamentos.setText("Si")

		self.radioButton_no_medicamentos = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_no_medicamentos.setGeometry(QRect(310, 160, 41, 17))
		self.radioButton_no_medicamentos.setObjectName("radioButton_no_medicamentos")
		self.radioButton_no_medicamentos.setText("No")

		self.textEdit_medicamento = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_medicamento.setGeometry(QRect(230, 180, 141, 61))
		self.textEdit_medicamento.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento.setObjectName("textEdit_medicamento")
		self.textEdit_medicamento.setPlaceholderText("Escriba el medicamento...")


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.frame_2 = QFrame(self)
		self.frame_2.setGeometry(QRect(20, 20, 121, 251))
		self.frame_2.setStyleSheet("QFrame{\n"
		"background-color:#12191D;\n"
		"border-radius:45px;\n"
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
		self.label_25.setText("Enfermedad")
		# ========================================================================================================	           

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ BOTONES DE LA VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		
		
		#Boton Aceptar ==========================================================================================      		
		self.pushButton_aceptar = QPushButton(self.frame_2)
		self.pushButton_aceptar.setGeometry(QRect(-10, 80, 141, 31))
		self.pushButton_aceptar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_aceptar.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar.setText("Aceptar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Boton Cancelar ==========================================================================================      		
		self.pushButton_cancelar = QPushButton(self.frame_2)
		self.pushButton_cancelar.setGeometry(QRect(-10, 120, 141, 31))
		self.pushButton_cancelar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_cancelar.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar.setText("Cancelar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ FIN DE BOTONES DE LA VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+# FIN DE VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		



















#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ VENTANA DE DETALLES DE REPARACION #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		


class Window_reparacionvivienda(QDialog):
	def __init__(self, parent = None):
		super(Window_reparacionvivienda, self).__init__()
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowTitle("Reparacion de vivienda")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setObjectName("Dialog")
		self.resize(649, 301)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()		

	def initUi(self):

		#GroupBox detalle de reparacion de vivienda ==========================================================================================      		
		self.groupBox_dcrp_reparacionvv = QGroupBox(self)
		self.groupBox_dcrp_reparacionvv.setGeometry(QRect(160, 10, 471, 281))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		

		#Descripcion de la reparacion de vivienda ==========================================================================================      		
		self.textEdit_dcrp_reparacionvv = QTextEdit(self.groupBox_dcrp_reparacionvv)
		self.textEdit_dcrp_reparacionvv.setGeometry(QRect(240, 50, 211, 181))
		self.textEdit_dcrp_reparacionvv.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_dcrp_reparacionvv.setObjectName("textEdit_dcrp_reparacionvv")
		self.textEdit_dcrp_reparacionvv.setPlaceholderText("Describa la reparación...")

		self.label_26 = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_26.setGeometry(QRect(290, 30, 121, 16))
		self.label_26.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_26.setAlignment(Qt.AlignCenter)
		self.label_26.setObjectName("label_26")
		self.label_26.setText("Describa la reparacion:")

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Opciones de reparacion de vivienda ==========================================================================================      		

		self.label_opc_reparacion = QLabel(self.groupBox_dcrp_reparacionvv)
		self.label_opc_reparacion.setGeometry(QRect(10, 30, 201, 16))
		self.label_opc_reparacion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_opc_reparacion.setAlignment(Qt.AlignCenter)
		self.label_opc_reparacion.setObjectName("label_opc_reparacion")
		self.label_opc_reparacion.setText("Necesita alguna de estas reparaciones:")

		self.checkBox = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox.setGeometry(QRect(20, 50, 70, 17))
		self.checkBox.setText("")
		self.checkBox.setObjectName("checkBox")
		self.checkBox_2 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_2.setGeometry(QRect(20, 70, 70, 17))
		self.checkBox_2.setText("")
		self.checkBox_2.setObjectName("checkBox_2")
		self.checkBox_3 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_3.setGeometry(QRect(20, 90, 70, 17))
		self.checkBox_3.setText("")
		self.checkBox_3.setObjectName("checkBox_3")
		self.checkBox_4 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_4.setGeometry(QRect(20, 110, 70, 17))
		self.checkBox_4.setText("")
		self.checkBox_4.setObjectName("checkBox_4")
		self.checkBox_5 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_5.setGeometry(QRect(20, 130, 70, 17))
		self.checkBox_5.setText("")
		self.checkBox_5.setObjectName("checkBox_5")
		self.checkBox_6 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_6.setGeometry(QRect(20, 150, 70, 17))
		self.checkBox_6.setText("")
		self.checkBox_6.setObjectName("checkBox_6")
		self.checkBox_7 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_7.setGeometry(QRect(20, 170, 70, 17))
		self.checkBox_7.setText("")
		self.checkBox_7.setObjectName("checkBox_7")
		self.checkBox_8 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_8.setGeometry(QRect(20, 190, 70, 17))
		self.checkBox_8.setText("")
		self.checkBox_8.setObjectName("checkBox_8")
		self.checkBox_9 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_9.setGeometry(QRect(20, 210, 70, 17))
		self.checkBox_9.setText("")
		self.checkBox_9.setObjectName("checkBox_9")
		self.checkBox_10 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_10.setGeometry(QRect(20, 230, 70, 17))
		self.checkBox_10.setText("")
		self.checkBox_10.setObjectName("checkBox_10")
		self.checkBox_11 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_11.setGeometry(QRect(20, 250, 70, 17))
		self.checkBox_11.setText("")
		self.checkBox_11.setObjectName("checkBox_11")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Botones para guardar y ver fotos  ==========================================================================================      		

		self.pushButton_anexarfotos = QPushButton(self.groupBox_dcrp_reparacionvv)
		self.pushButton_anexarfotos.setGeometry(QRect(300, 240, 101, 31))
		self.pushButton_anexarfotos.setStyleSheet("QPushButton{\n"
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
		self.pushButton_anexarfotos.setObjectName("pushButton_anexarfotos")
		self.pushButton_anexarfotos.setText("Anexar fotos")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(40)
		self.pushButton_anexarfotos.setGraphicsEffect(self.shadow)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.frame_2 = QFrame(self)
		self.frame_2.setGeometry(QRect(20, 10, 121, 281))
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


		#Boton Aceptar ==========================================================================================      		
		self.pushButton_aceptar = QPushButton(self.frame_2)
		self.pushButton_aceptar.setGeometry(QRect(-10, 70, 141, 31))
		self.pushButton_aceptar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_aceptar.setObjectName("pushButton_aceptar")
		self.pushButton_aceptar.setText("Aceptar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#Boton cancelar ==========================================================================================      		
		self.pushButton_cancelar = QPushButton(self.frame_2)
		self.pushButton_cancelar.setGeometry(QRect(-10, 110, 141, 31))
		self.pushButton_cancelar.setStyleSheet("QPushButton{\n"
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
		self.pushButton_cancelar.setObjectName("pushButton_cancelar")
		self.pushButton_cancelar.setText("Cancelar")
		

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Eventos ==========================================================================================      		

		self.pushButton_anexarfotos.clicked.connect(self.initalvisor)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#



	#Funcion de initalvisor ==========================================================================================      		

	def initalvisor(self):
		Visor_de_imagenes(self).exec_()

	#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ fIN DE VENTANA DE DETALLES DE  REPARACION DE VIVIENDA #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		












#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ VENTANA DE VISUALIZADOR DE IMAGENES #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+     

class Visor_de_imagenes(QDialog):
	def __init__(self, parent=None):
		super(Visor_de_imagenes, self).__init__()

		self.initUi()

	def initUi(self):
		#  ==========================================================================================           
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setWindowTitle("Cargar Foto")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setObjectName("Dialog")
		self.resize(770, 390)
		self.move(100, 100)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"\n"
		"")
		self.frame_3 = QFrame(self)
		self.frame_3.setGeometry(QRect(20, 10, 121, 370))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		# Parte del visualizador donde se mostrara la imagen ==========================================================================================             
		self.frame = QFrame(self)
		self.frame.setGeometry(QRect(160, 10, 591, 371))
		self.frame.setStyleSheet("QFrame{\n"
		"background-color:#E5E7EE;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setFrameShadow(QFrame.Raised)
		self.frame.setObjectName("frame")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		# Label de la miniatura de imagen ==========================================================================================            
		#Miniatura_1
		self.label_miniatura_1 = QLabelClickable(self.frame)
		self.label_miniatura_1.setGeometry(QRect(10, 20, 171, 121))
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
		self.label_miniatura_1_nombre = QLabel(self.frame)
		self.label_miniatura_1_nombre.setGeometry(QRect(20,120,151,16))
		self.label_miniatura_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		#Miniatura_2
		self.label_miniatura_2 = QLabelClickable(self.frame)
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
		self.label_miniatura_2_nombre = QLabel(self.frame)
		self.label_miniatura_2_nombre.setGeometry(QRect(220,120,151,16))
		self.label_miniatura_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")




		#Miniatura_3
		self.label_miniatura_3 = QLabelClickable(self.frame)
		self.label_miniatura_3.setGeometry(QRect(410, 20, 171, 121))
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
		self.label_miniatura_3_nombre = QLabel(self.frame)
		self.label_miniatura_3_nombre.setGeometry(QRect(420,120,151,16))
		self.label_miniatura_3_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_3_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		
		#Miniatura_4
		self.label_miniatura_4 = QLabelClickable(self.frame)
		self.label_miniatura_4.setGeometry(QRect(10, 200, 171, 121))
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
		self.label_miniatura_4_nombre = QLabel(self.frame)
		self.label_miniatura_4_nombre.setGeometry(QRect(20,300,151,16))
		self.label_miniatura_4_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_4_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		
		#Miniatura_5
		self.label_miniatura_5 = QLabelClickable(self.frame)
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
		self.label_miniatura_5_nombre = QLabel(self.frame)
		self.label_miniatura_5.setObjectName("label_miniatura_5_nombre")
		self.label_miniatura_5_nombre.setGeometry(QRect(220,300,151,16))
		self.label_miniatura_5_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")

		#Miniatura_6
		self.label_miniatura_6 = QLabelClickable(self.frame)
		self.label_miniatura_6.setGeometry(QRect(410, 200, 171, 121))
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
		self.label_miniatura_6_nombre = QLabel(self.frame)
		self.label_miniatura_6_nombre.setGeometry(QRect(420,300,151,16))
		self.label_miniatura_6_nombre.setAlignment(Qt.AlignCenter)

		self.label_miniatura_6_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_1  ==========================================================================================             
		self.pushButton_eliminar = QPushButton(self.frame)
		self.pushButton_eliminar.setGeometry(QRect(60, 150, 71, 21))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_2 ==========================================================================================             
		self.pushButton_eliminar_2 = QPushButton(self.frame)
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_3  ==========================================================================================             
		self.pushButton_eliminar_3 = QPushButton(self.frame)
		self.pushButton_eliminar_3.setGeometry(QRect(460, 150, 71, 21))
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_4 ==========================================================================================             
		self.pushButton_eliminar_4 = QPushButton(self.frame)
		self.pushButton_eliminar_4.setGeometry(QRect(60, 330, 71, 21))
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
		#Boton eliminar de miniatura_5  ==========================================================================================             
		self.pushButton_eliminar_5 = QPushButton(self.frame)
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
		#Boton eliminar de miniatura_6  ==========================================================================================             
		self.pushButton_eliminar_6 = QPushButton(self.frame)
		self.pushButton_eliminar_6.setGeometry(QRect(460, 330, 71, 21))
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
		#Boton aceptar  ==========================================================================================              
		self.pushButton_5 = QPushButton(self.frame_3)
		self.pushButton_5.setGeometry(QRect(0, 70, 121, 31))
		self.pushButton_5.setStyleSheet("QPushButton{\n"
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
		self.pushButton_5.setObjectName("pushButton_5")
		self.pushButton_5.setText("Aceptar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton cancelar  ==========================================================================================             
		self.pushButton_8 = QPushButton(self.frame_3)
		self.pushButton_8.setGeometry(QRect(0, 110, 121, 31))
		self.pushButton_8.setStyleSheet("QPushButton{\n"
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
		self.pushButton_8.setObjectName("pushButton_8")
		self.pushButton_8.setText("Cancelar")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Eventos==========================================================================================             
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


	def Eliminar(self):
		def establecerValores():
			labelConImagen.clear()
			# Limpiar la barra de estado
			#self.parent.statusBar.clearMessage()
					
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


	def Mostrar_5(self, label, imagen, nombre, posicionX= 390):
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
		self.animacionMostar.setEndValue(QRect(390, 200, 171, 121))
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

	def Mostrar_4 (self, label, imagen, nombre, posicionX= 200):
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
		self.animacionMostar.setEndValue(QRect(200, 200, 171, 121))
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


	def Mostrar_3 (self, label, imagen, nombre, posicionX= 10):
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
		self.animacionMostar.setEndValue(QRect(10, 200, 171, 121))
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


	def Mostrar_2 (self, label, imagen, nombre, posicionX= 390):
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
		self.animacionMostar.setEndValue(QRect(390, 20, 171, 121))
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

		else:
			None

	def Mostrar_1 (self, label, imagen, nombre, posicionX= 200):
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
		self.animacionMostar.setEndValue(QRect(200, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)



	def Cargar(self):

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
				self.Mostrar(self.label_miniatura_1, imagen, nombre)
				self.foto_1(imagen)

		else:
			None
			

	def foto_1(self,imagen):
		Ver_fotos(imagen,self).exec_()

	def Mostrar(self,label, imagen, nombre, posicionX=10):
		imagen = QPixmap.fromImage(imagen)
	
		# Escalar imagen a 169x119 si el ancho es mayor a 171 o el alto mayor a 121
		if imagen.width() > 171 or imagen.height() > 121:
			imagen = imagen.scaled(169, 119, Qt.KeepAspectRatio, Qt.SmoothTransformation)

		# Mostrar imagen
		label.setPixmap(imagen)
	

		# Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
		# y se desbloquean los botones).       
		self.animacionMostar = QPropertyAnimation(label, b"geometry")
		self.animacionMostar.finished.connect(lambda: (self.label_miniatura_1_nombre.setText(nombre)))

		self.animacionMostar.setDuration(200)
		self.animacionMostar.setStartValue(QRect(posicionX, 5, 171, 121))
		self.animacionMostar.setEndValue(QRect(10, 20, 171, 121))
		self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)





class QLabelClickable(QLabel):
	clicked = pyqtSignal()
	
	def __init__(self, parent=None):
		super(QLabelClickable, self).__init__(parent)

	def mousePressEvent(self, event):
		self.clicked.emit()


class Ver_fotos(QDialog):
	def __init__(self,imagen, parent=None):
		super(Ver_fotos, self).__init__()

		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)


		self.parent = parent
		self.imagen = imagen
		#self.nombre = nombre
		self.setWindowTitle("Foto")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		
		#  =========================================================================================           
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

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ FIN DE VENTANA DE VISUALIZADOR DE IMAGENES #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+   



















if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()