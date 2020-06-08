#======================================================================================================
import sqlite3
from os import getcwd, makedirs
from Source_rc import *

#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import*

from Window_visor_de_imagenes import *

from Window_reparacion import *

from Window_enfermedad import * 

from Window_discapacidad import *

from Window_gas_bombona import *


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
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


#=====================================================================================================




#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+Ventana registro de usuario+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+

class Window_nv_users(QDialog):

	def __init__(self, parent = None):
		super(Window_nv_users, self).__init__()
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowTitle("Nuevo usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(920, 514)  
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
		
		self.groupBox_datosGnr.setObjectName("groupBox_datosGnr")
		self.groupBox_datosGnr.setTitle("				Datos Generales")
		self.groupBox_datosGnr.setAlignment(Qt.AlignHCenter)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosGnr.setGraphicsEffect(self.shadow)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#1ºNombre =====================================================================================================	
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

			

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#2ºNombre =====================================================================================================
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#1º Apellido =====================================================================================================		
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#2º Apellido =====================================================================================================		
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	   
		#Cedula de identidad =====================================================================================================		
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Telefono =====================================================================================================		
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Genero ========================================================================================================	      
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
				
		#Edad ========================================================================================================	      
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	  
		#Fecha de nacimiento ========================================================================================================	        
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de checkbox datos generales ========================================================================================================	      
		self.label_opciones = QLabel(self.groupBox_datosGnr)
		self.label_opciones.setGeometry(QRect(180, 260, 141, 19))
		self.label_opciones.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 10px")
		self.label_opciones.setAlignment(Qt.AlignCenter)
		self.label_opciones.setObjectName("label_opciones")
		self.label_opciones.setText("Posee alguna de las opciones:")

		self.checkBox_1 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_1.setGeometry(QRect(200, 280, 100, 17))
		self.checkBox_1.setObjectName("checkBox_1")
		self.checkBox_1.setText("Pensionado")
		self.checkBox_1.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")        
		
		self.checkBox_2 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_2.setGeometry(QRect(200, 300, 110, 17))
		self.checkBox_2.setObjectName("checkBox_2")
		self.checkBox_2.setText("Discapacidad")
		self.checkBox_2.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_3 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_3.setGeometry(QRect(200, 320, 100, 17))
		self.checkBox_3.setText("Enfermedad")
		self.checkBox_3.setObjectName("checkBox_3")
		self.checkBox_3.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  


		self.checkBox_4 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_4.setGeometry(QRect(200, 340, 100, 17))
		self.checkBox_4.setObjectName("checkBox_4")
		self.checkBox_4.setText("Embarazada")
		self.checkBox_4.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  

		self.checkBox_5 = QCheckBox(self.groupBox_datosGnr)
		self.checkBox_5.setGeometry(QRect(200, 360, 100, 17))
		self.checkBox_5.setObjectName("checkBox_5")
		self.checkBox_5.setText("Lactante")
		self.checkBox_5.setStyleSheet("QCheckBox{ background-color:#E5E7EE;\n"
		"color:#000000\n"
		"}")  


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
		'Profesor','Veterinario', 'Otro...'
		'']

		self.comboBox_profesion.addItems(self.items_list_profesion)

		


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Nivel de instruccion ========================================================================================================	      
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Parentesco ========================================================================================================	      
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

	   
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Estado civil ========================================================================================================	      

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
		#self.lineEdit_correo.setValidator(QRegExpValidator(QRegExp('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$+'),self.lineEdit_correo))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ubicacion geografica #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

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
		self.groupBox_datosUb.setTitle("				        Ubicación geográfica")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datosUb.setGraphicsEffect(self.shadow)
		#Estado ========================================================================================================	      
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Municipio ========================================================================================================	      
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Parroquia ========================================================================================================	      
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Nº de vivienda ========================================================================================================	      
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Direccion ========================================================================================================	      
		self.label_direccion = QLabel(self.groupBox_datosUb) 
		self.label_direccion.setGeometry(QRect(235, 20, 81, 16))
		self.label_direccion.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_direccion.setAlignment(Qt.AlignCenter)
		self.label_direccion.setObjectName("label_direccion")
		self.label_direccion.setText("<font color='#FF3300'>*</font>Dirección:")
		self.textEdit_direccion = QTextEdit(self.groupBox_datosUb)
		self.textEdit_direccion.setGeometry(QRect(193, 40, 161, 71))
		self.textEdit_direccion.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_direccion.setObjectName("textEdit_direccion")
		self.textEdit_direccion.setPlaceholderText("Ingresa la dirección...")
		self.textEdit_direccion.setToolTip("Ingresa la dirección donde se residencia")



		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Datos de la vivienda #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

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
		self.groupBox_datos_Vv.setTitle("				       Datos de la vivienda")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_datos_Vv.setGraphicsEffect(self.shadow)
		#Metros cuadrados ========================================================================================================	      
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Necesita alguna reparacion ========================================================================================================	      
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Servivcios que posee ========================================================================================================	           
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Descripcion de la vivienda ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Proteccion Social #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
	  
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
		self.groupBox_beneficios.setTitle("				     Proteccion social")
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
		self.line_10.setGeometry(QRect(193, 110, 161, 16))
		self.line_10.setFrameShape(QFrame.HLine)
		self.line_10.setFrameShadow(QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line bajo metros cuadrados ==========================================================================================      
		self.line_11 = QFrame(self.groupBox_datos_Vv)
		self.line_11.setGeometry(QRect(15, 63, 141, 16))
		self.line_11.setFrameShape(QFrame.HLine)
		self.line_11.setFrameShadow(QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Line bajo servicios que posee ==========================================================================================      
		self.line_12 = QFrame(self.groupBox_datos_Vv)
		self.line_12.setGeometry(QRect(180, 115, 181, 20))
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
		self.Button_register_user.setIcon(QIcon("Imagenes-iconos/Registrar.png"))
		self.Button_register_user.setIconSize(QSize(20,20))
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
		self.Button_cancel_user.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancel_user.setIconSize(QSize(17,17))	
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ FIN DE BOTONES DE LA VENTANA DE REGISTRO DE USUARIO #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

#========================================= #Eventos# ==================================================================

		self.Button_register_user.clicked.connect(self.Creater_base_datos)

		self.Button_register_user.clicked.connect(self.New_user)

		self.checkBox_2.clicked.connect(self.Descripcion_discapacidad)

		self.radioButton_rp_si.clicked.connect(self.Descripcion_reparacion)

		self.checkBox_3.clicked.connect(self.Descripcion_enfermedad)

		self.checkBox_gasbombona.clicked.connect(self.Window_gas_bombona)

		self.Button_cancel_user.clicked.connect(self.close)


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	
#========================================= #Funciones# ==================================================================

	#Abrir ventana de gas_bobombona ==========================================================================================      			

	def Window_gas_bombona(self):

		if self.checkBox_gasbombona.isChecked():

			Window_gas_bombona(self).exec_()
		else:
			None

	#Abrir ventana de Enfermedad ==========================================================================================      			

	def Descripcion_enfermedad(self):

		if self.checkBox_3.isChecked():
			self.interface = Window_enfermedad()
			Window_enfermedad(self).exec_()
		else:
			None

	#Funcion para abrir ventana de descripcion de reparacion de vivienda ==========================================================================================      			

	def Descripcion_reparacion(self):

		if self.radioButton_rp_si.isChecked():
			self.interface = Window_reparacionvivienda()
			Window_reparacionvivienda(self).exec_()
		else:
			None

	#Funcion para abrir ventan de descripcion de discapacidad ==========================================================================================      			
	
	def Descripcion_discapacidad(self):

		if self.checkBox_2.isChecked():

			self.interface = Window_discapacidad()		
			Window_discapacidad(self).exec_()

		else:
			None

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

																			"PENSIONADO TEXT, POSEE_DISCAPACIDAD TEXT,NECESITA_INSUMO_MEDICO TEXT,"

																			"DESCRIBA_DISCAPACIDAD TEXT, TOMA_MEDICAMENTO TEXT, DESCRIBA_MEDICAMENTO TEXT,"
																			
																			"POSEE_ENFERMEDAD TEXT, DESCRIBA_ENFERMEDAD TEXT,  EMBARAZADA TEXT, LACTANTE TEXT,"

																			"TOMA_MEDICAMENTO_ENF TEXT, DESCRIBA_MEDICAMENTO_ENF TEXT)")


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

		#Datos Generales
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
		numero_vivienda = self.lineEdit_N_vivienda.text()
		direccion = self.textEdit_direccion.toPlainText()


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
					print(idusuario)

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
				datos_insertar_Ubc = [estado, municipio,parroquia,direccion,numero_vivienda]

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
			self.checkBox_1.setChecked(False)
			self.checkBox_2.setChecked(False)
			self.checkBox_3.setChecked(False)
			self.checkBox_4.setChecked(False)
			self.checkBox_5.setChecked(False)
			self.comboBox_estadocivil.setCurrentIndex(-1)
			#self.RadioButton_rep.setChecked(False)
			self.lineEdit_correo.clear()

					#Ubicacion geografica			
			self.lineEdit_estado.clear()
			self.lineEdit_municipio.clear()
			self.lineEdit_parroquia.clear()
			self.lineEdit_N_vivienda.clear()
			self.textEdit_direccion.clear()


			#Datos de la vivienda
			self.lineEdit_M2.clear()
			self.textEdit_dcrp_vv.clear()
			#self.RadioButton_reparacion.setChecked(False)
			#self.CheckBox_aguapotable.setChecked(False)
			self.CheckBox_aguaservidas.setChecked(False)
			self.CheckBox_gasdirecto.setChecked(False)
			self.CheckBox_gasbombona.setChecked(False)
			self.CheckBox_internet.setChecked(False)
			self.CheckBox_electricidad.setChecked(False)
			self.CheckBox_telefonofijo.setChecked(False)

			#Proteccion Social
			self.CheckBox_hogaresdelapatria.setChecked(False)
			self.CheckBox_amormayor.setChecked(False)
			self.CheckBox_josegregorio.setChecked(False)
			self.CheckBox_partohumanizado.setChecked(False)
			#=============
			self.CheckBox_chambajuvenil.setChecked(False)
			self.CheckBox_somosvenezuela.setChecked(False)
			self.CheckBox_frentemiranda.setChecked(False)
			self.CheckBox_jpsuv.setChecked(False)
						

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




	def close(self):
		
		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("Cancelar")
		msg.setInformativeText("¿Estás seguro de que desea cancelar?")
		msg.setWindowTitle("¡Advertencia!")
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
			self.destroy()
		else:
			pass


	#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	

#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ Fin de la Ventana registro de usuario+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+









if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_nv_users()
	interface.show()
	app.exec_()