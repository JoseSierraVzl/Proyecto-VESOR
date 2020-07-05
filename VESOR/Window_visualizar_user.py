import sqlite3
from os import getcwd, makedirs
from Source_rc import *


from Window_visualizador_discapacidad import *

import sys, os, time
from random import randint
from PyQt5 import  uic 

from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QByteArray,QIODevice,QBuffer,QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,QSpinBox)





class Window_visualizar_users(QDialog):
	def __init__(self,dato, parent = None):
		super(Window_visualizar_users, self).__init__()

		self.parent = parent
		self.datos = dato
		#self.indice = indice

		self.setObjectName("Dialog")
		self.setWindowTitle("Datos de usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setFixedSize(920, 514)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()
		self.Mostrar_Datos()


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
		'Profesor','Veterinario','Estudiante','Otro...'
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=




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
		self.line_9.setGeometry(QRect(180, 350, 141, 16))
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
		self.line_20.setGeometry(QRect(180, 420, 141, 16))
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
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ BOTONES DE LA VENTANA DE REGISTRO DE USUARIO #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
		#Boton educacion ==========================================================================================      		
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


		#Boton datos vivienda==========================================================================================      		
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


		#Boton Enfermedad ==========================================================================================      		
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



		#Boton Discapacidad ==========================================================================================      		
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


		
		#Boton registrar ==========================================================================================      		
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton cancelar ==========================================================================================      		
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
		self.Button_cancel_user.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancel_user.setIconSize(QSize(17,17))	
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
























		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ventana de Discapacidad #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#

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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
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
		# ========================================================================================================	          

		#Group de discapacidad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Descripcion de discapacidad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de discapacidad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de medicamentos ========================================================================================================	           
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         

		#BOTONES DE LA VENTANA DE DISCAPACIDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		
		
		#Boton Aceptar ==========================================================================================      		
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
		self.pushButton_aceptar_discapacidad.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_discapacidad.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Boton Cancelar ==========================================================================================      		
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
		self.pushButton_cancelar_discapacidad.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_discapacidad.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




























		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ventana de ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#

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

		#Group de enfermedad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Descripcion de enfermedad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de enfermedad ========================================================================================================	           
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Opciones de medicamentos ========================================================================================================	           
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


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
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
		# ========================================================================================================	           

		#+ BOTONES DE LA VENTANA DE ENFERMEDAD #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		
		
		#Boton Aceptar ==========================================================================================      		
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
		self.pushButton_aceptar_Enfermedad.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_Enfermedad.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Boton Cancelar ==========================================================================================      		
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
		self.pushButton_cancelar_Enfermedad.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_Enfermedad.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

















		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ventana de Reparacion vivienda #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#
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


		#GroupBox detalle de reparacion de vivienda ==========================================================================================      		
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		

		#Descripcion de la reparacion de vivienda ==========================================================================================      		
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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Opciones de reparacion de vivienda ==========================================================================================      		

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


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Datos de bombona ==========================================================================================      		
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

		#QSpinBox de cantidad de bombonas  ==========================================================================================      		

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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		
		#Botones para guardar y ver fotos  ==========================================================================================      		

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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
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


		#Boton Aceptar ==========================================================================================      		
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
		self.pushButton_aceptar_rpr_vv.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar_rpr_vv.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#Boton cancelar ==========================================================================================      		
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
		self.pushButton_cancelar_rpr_vv.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar_rpr_vv.setIconSize(QSize(15,15))
		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#























		#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Ventana de Reparacion vivienda #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#

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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		# Label de la miniatura de imagen ==========================================================================================            
		#Miniatura_1
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


		#Miniatura_2
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





		#Miniatura_3
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


		
		#Miniatura_4
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


		
		#Miniatura_5
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

		#Miniatura_6
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




		#Boton eliminar de miniatura_1  ==========================================================================================             
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_2 ==========================================================================================             
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_3  ==========================================================================================             
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
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton eliminar de miniatura_4 ==========================================================================================             
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
		#Boton eliminar de miniatura_5  ==========================================================================================             
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
		#Boton eliminar de miniatura_6  ==========================================================================================             
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

		#Boton aceptar  ==========================================================================================              
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
		self.pushButton_visualizador_aceptar.setIcon(QIcon("Imagenes-iconos/Guardar_blanco.png"))
		self.pushButton_visualizador_aceptar.setIconSize(QSize(18,18))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Boton cancelar  ==========================================================================================             
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
		self.pushButton_visualizador_cancelar.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_visualizador_cancelar.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




		#Buttons para ver imagenes==========================================================================================             

		#Ver foto 1
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
		###

		#Ver foto 2
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
		###



		#Ver foto 3
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
		###

		#Ver foto 4
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
		###

		#Ver foto 5
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
		###

		#Ver foto 6
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
		###
		
		#Frame contenedor de foto 
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

		#Mostrador de fotos

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
		###

		###




		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		self.pushButton_cerrar.clicked.connect(self.Bajar_foto_label)

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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


















#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ Datos de estudiante #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

		self.frame_principal_estudiante = QFrame(self)
		self.frame_principal_estudiante.setGeometry(QRect(200,100,613,303))
		self.frame_principal_estudiante.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477,\n"
		"stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"border-radius:30px}")
		self.frame_principal_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(10)
		self.frame_principal_estudiante.move(200,1000)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		#Menu ========================================================================================================	           
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
		
		#Buttons de menu
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
		self.Button_aceptar_estudiante.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
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
		self.Button_cancelar_estudiante.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.Button_cancelar_estudiante.setIconSize(QSize(15,15))



		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		self.frame_contenido_estudiante = QFrame(self.frame_principal_estudiante)
		self.frame_contenido_estudiante.setGeometry(QRect(170,20,421,261))
		self.frame_contenido_estudiante.setStyleSheet("color:#1b231f;\n"
		"background-color: #E5E7EE;\n"
		"font: 75 10pt Comic Sans MS;\n"
		"border-radius: 22px;")
		self.frame_contenido_estudiante.setGraphicsEffect(self.shadow)
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		#Nivel de instruccion ========================================================================================================	           

		#label nivel de estudio:
		self.label_nivel_de_estudio = QLabel(self.frame_contenido_estudiante)
		self.label_nivel_de_estudio.setGeometry(QRect(70,10,125,16))
		self.label_nivel_de_estudio.setText("Nivel de estudio:")
		self.label_nivel_de_estudio.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		self.label_nivel_de_estudio.setAlignment(Qt.AlignHCenter)
		###

		#CheckBox de niveles de estudio primaria

		self.checkbox_primaria = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_primaria.setGeometry(QRect(20,30,121,21))
		self.checkbox_primaria.setText("Primaria")
		###


		#CheckBox de niveles de estudio bachillerato

		self.checkbox_bachillerato = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_bachillerato.setGeometry(QRect(20,50,121,21))
		self.checkbox_bachillerato.setText("Bachillerato")
		###

		#CheckBox de niveles de estudio tecnico superior

		self.checkbox_tcn_superior = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_tcn_superior.setGeometry(QRect(20,70,221,21))
		self.checkbox_tcn_superior.setText("Técnico superior universitario")
		###

		#CheckBox de niveles de estudio universitario

		self.checkbox_universitario = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_universitario.setGeometry(QRect(20,90,111,21))
		self.checkbox_universitario.setText("Universitario")
		###

		#CheckBox de niveles de estudio especializacion

		self.checkbox_especializacion = QCheckBox(self.frame_contenido_estudiante)
		self.checkbox_especializacion.setGeometry(QRect(20,110,131,21))
		self.checkbox_especializacion.setText("Especialización ")
		###
		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Carrera que estudia ========================================================================================================	           

		#Label de tipo de carrera
		self.label_carrera_que_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_carrera_que_estudia.setGeometry(QRect(255,10,145,16))
		self.label_carrera_que_estudia.setText("Carrera que estudia:")
		self.label_carrera_que_estudia.setAlignment(Qt.AlignHCenter)
		self.label_carrera_que_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		###

		#QTextEdit de carrera que estudia
		self.texedit_carrera = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_carrera.setGeometry(QRect(250,30,161,81))
		self.texedit_carrera.setPlaceholderText("Carrera que cursa...")
		self.texedit_carrera.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Donde estudia ========================================================================================================	           

		#Qlabel de donde estudia
		self.label_donde_estudia = QLabel(self.frame_contenido_estudiante)
		self.label_donde_estudia.setGeometry(QRect(160,140,111,16))
		self.label_donde_estudia.setText("Donde estudia:")
		self.label_donde_estudia.setAlignment(Qt.AlignHCenter)
		self.label_donde_estudia.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px")
		###

		#QTextEdit de donde estudia
		self.texedit_donde_estudia = QTextEdit(self.frame_contenido_estudiante)
		self.texedit_donde_estudia.setGeometry(QRect(40,160,341,81))
		self.texedit_donde_estudia.setPlaceholderText("Dirección y universidad donde estudia...")
		self.texedit_donde_estudia.setStyleSheet("QTextEdit{background-color: #12191D;\n"
		"border-radius:20px;\n"
		"color:#ffffff\n"
		"}")
		###

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


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



		#Eventos ========================================================================================================	           
		self.Button_cancel_user.clicked.connect(self.close)
		
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
		#self.pushButton_ver_foto6.clicked.connect(self.Subir_foto_label)				
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#



	def Desbloquear_buttons(self):

		self.Button_discapacidad.setEnabled(True)
		self.Button_enfermedad.setEnabled(True)
		self.Button_vivienda.setEnabled(True)
		#self.pushButton_ver_fotos.setEnabled(True)
		self.Button_educacion.setEnabled(True)




	def Bloquear_buttons(self):



		self.Button_discapacidad.setEnabled(False)
		self.Button_enfermedad.setEnabled(False)
		self.Button_vivienda.setEnabled(False)
		#self.pushButton_ver_fotos.setEnabled(False)
		self.Button_educacion.setEnabled(False)


		#Eventos mostrar datos de la base de datos  ========================================================================================================	           
	def Mostrar_Datos(self):
		#datos generales
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



		#Ventana de discapacidad

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


		#Ventana de enfermedad

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


		###


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
				print(datosdevueltos)
				for dato in datosdevueltos:
					#indice = dato[0]
					print(dato[0])
					self.estado = dato[1]
					print(dato[1])
					self.municipio = dato[2]
					print(dato[2])
					self.parroquia = dato[3]
					print(dato[3])
					self.direccion = dato[4]
					print(dato[4])

					#self.n_vivienda = dato[5]
					#print(dato[5])
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
				print(datosdevueltos)
				for dato in datosdevueltos:
					#indice = dato[0]
					self.metrosdevivieda = dato[1]
					print(dato[1])
					self.descripciondecasa = dato[2]
					print(dato[2])
					self.reparacionvivienda = dato[3]
					print(dato[3])
					self.reparaciondetechos = dato[4]
					print(dato[4])
					self.reparaciondepared = dato[5]
					print(dato[5])
					self.reparaciondepintura = dato[6]
					print(dato[6])
					self.reparaciondepisos = dato[7]
					print(dato[7])
					self.reparaciondeelectricidad = dato[8]
					print(dato[8])
					self.reparaciondeaguas = dato[9]
					print(dato[9])
					self.reparaciondeaguasservidas = dato[10]
					print(dato[10])
					self.reparaciondeventanas= dato[11]
					print(dato[11])
					self.reparaciondepuertas = dato[12]
					print(dato[12])
					self.reparacionotras = dato[13]
					print(dato[13])
					self.aguapotable= dato[14]
					print(dato[14])
					self.aguaservida = dato[15]
					print(dato[15])
					self.gasdirecto = dato[16]
					print(dato[16])
					self.gasbombona = dato[17]
					print(dato[17])
					self.tipodecilindro = dato[18]
					print(dato[18])
					self.cantidaddebombona = dato[19]
					print(dato[19])
					self.internet = dato[20]
					print(dato[20])
					self.electricidad = dato[21]
					print(dato[21])
					self.telefonofijo = dato[22]
					print(dato[22])
					self.tiporeparaciondcrp = dato[23]
					print(dato[23])
					self.necesitalineablanca = dato[24]
					print(dato[24])
					self.foto1 = dato[25]
					print("fotoa",dato[25])
					self.foto2 = dato[26]
					print("fotob",dato[26])
					self.foto3 = dato[27]
					print("fotoc",dato[27])
					self.foto4 = dato[28]
					print("fotod",dato[28])
					self.foto5 = dato[29]
					print("fotoe",dato[29])
					self.foto6 = dato[30]
					print("fotof",dato[30])
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


		#Tipo de reparaciones 


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


		#Ventana de estudiante



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
				print(datosdevueltos)
				for dato in datosdevueltos:
					self._hogaresdelapatria = dato[1]
					print(dato[1])

					self._amormayor = dato[2]
					print(dato[2])

					self._josegregorio = dato[3]
					print(dato[3])

					self._partohumanizado = dato[4]
					print(dato[4])

					self._chambajuvenil = dato[5]
					print(dato[5])

					self._somosvenezuela = dato[6]
					print(dato[6])

					self._frentemiranda = dato[7]
					print(dato[7])
					self._jpsuv = dato[8]
					print(dato[8])
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
		opcion_pensionado = self.pensionado()
		#opcion_discapacidad = self.checkBox_2_discapacidad.text()
		#opcion_enfermedad = self.checkBox_3_enfer.text()
		opcion_embarazada = self.opcion_de_embarazada()
		opcion_lactante = self.opcion_de_lactante()
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
		#reparaciones = self.RadioButton_reparacion()
		servicio_aguapotable = self.CheckBox_aguapotable()
		servicio_aguaservidas = self.CheckBox_aguaservidas()
		servicio_gasdirecto = self.CheckBox_gasdirecto()
		servicio_gasbombona = self.gas_bombona_servicio()
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


		#Ventana de discapacidad

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
		#insumos_medicos = self.insumomedico()

		#Ventana de enfermedad
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

		#Ventana de reparacion de vivienda:

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

		#Ventana bombona 
		tipo_de_cilindro = self.Tipo_de_cilindro()
		cantidad_de_bombonas = int(self.num_bombonas.value())

		#Ventana estudiante

		nivel_estudio = self.nivel_estudio()
		carrera_cursando = self.texedit_carrera.toPlainText()
		donde_estudia = self.texedit_donde_estudia.toPlainText()

		#Venta de visualizador de fotos 

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
					print(idusuario)

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


		self.destroy()









			





		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#





		






		#Funciones ========================================================================================================	           
	#funcion mostar imagen en label =======================================================================================

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

	###########
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




	###########
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


	###########

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


	###########

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


	###########

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


	
	#funcion de estudiante nivel de estudio =======================================================================================

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
	#funcion de estudiante =======================================================================================

	def Estudiante(self,i):

			if i == 15:
				self.Mostrar_estudiante()
			else:
				return "No esta estudiando"

	#opcion de lactante =======================================================================================
	
	def opcion_de_lactante(self):
		if self.checkBox_5_lactante.isChecked():
			return "Si"
		else: 
	
			return "No esta en estado de lactancia"
	#opcion de embarazada =======================================================================================
	def opcion_de_embarazada(self):

		if self.checkBox_4_Embarazada.isChecked():
			return "Si"

		else:
			return "No esta en estado de embarazo"


	#opcion de servicio gas bombona =======================================================================================
	def gas_bombona_servicio(self):

		if self.checkBox_gasbombona.isChecked():
			return "Si"
		else:
			return "No"

	#opcion pensionado  =======================================================================================c
	def pensionado(self):

		if self.checkBox_1_pensionado.isChecked():
			return "Pensionado"
		else:
			return "No esta pensionado"

	#Ventana reparacion de vivienda  =======================================================================================

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

	#TIPOS DE REPARACION

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

	#Ventana de Enfermedad =======================================================================================

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





	#Ventana de discapacidad =======================================================================================

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

	#Tipo de discapacidades		

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
	###############


	###################################### Funciones para los radio button y Checkbox #########################################
	#Funcion para el RadioButton de si necesita alguna reparacion ==========================================================================================      			
	"""def RadioButton_reparacion(self):
		
		if self.radioButton_rp_si.isChecked():
			
			return "Si"

		elif self.radioButton_rp_no.isChecked():
			return "No"

		else:
			return "No necesita reparacion"""

	#Funcion de si esta inscrito en el REP =============================================================================================
	def RadioButton_rep(self):

		if self.radiobutton_si_inscrito.isChecked():
			return "Si"

		elif self.radiobutton_no_inscrito.isChecked():
			return "No esta inscrito"

		else:
			return "No"

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

		
		
 
    #Funciones para discapacidad
	def Aceptar_discapacidad(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_Discapacidad()
			self.Desbloquear_buttons()

		else:
			pass

	def Cancelar_Discapacidad(self):
		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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

	###

	#Funciones para enfermedad
	def Aceptar_enfermedad(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_Enfermedad()
			self.Desbloquear_buttons()

		else:
			pass
	def Cancelar_enfermedad(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
	###

	#Funciones vivienda
	def Aceptar_reparacion_vv(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_rpr_vv()
			self.Desbloquear_buttons()

		else:
			pass
	def Cancelar_rpr_vv(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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

	#Funcion parte de ver imagenes
	def Aceptar_visualizador(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_visualizador()
			self.Desbloquear_buttons()

		else:
			pass
	def Cancelar_visualizador(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_visualizador()
			self.Desbloquear_buttons()


		else:
			pass	
	def Mostrar_visualizador(self,):
  
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

	###

	#Funcion para estudiante
	def Aceptar_estudiante(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que ha colocado\nlos datos correctamente?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
			self.Ocultar_estudiante()
			self.Desbloquear_buttons()

		else:
			pass
	def Cancelar_estudiante(self):

		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Verificar Datos")
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
	###




		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#














	def Eliminar(self):
		def establecerValores():
			labelConImagen.clear()
			label_imagen1.clear()
		if self.label_imagen_1_1.pixmap():
			label_imagen1 = self.label_imagen_1_1
		if label_imagen1:
			label_imagen1.clear()
			self.label_imagen_1_1.clear()

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
				#imagen_6 = QPixmap(nombreImagen)				
			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_5(self.label_miniatura_6, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_6 = imagen
				#self.Guardar_datos(imagen_6)
				#self.Guardar_datos(imagen_6)


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
				##imagen_5 = QPixmap(nombreImagen)				
			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_4(self.label_miniatura_5, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_5 = imagen
				#self.Guardar_datos(imagen_5)
				##self.Guardar_datos(imagen_5)


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
				#imagen_4 = QPixmap(nombreImagen)				
			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_3(self.label_miniatura_4, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_4 = imagen
				#self.Guardar_datos(imagen_4)
				#self.Guardar_datos(imagen_4)


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
				##imagen_3 = QPixmap(nombreImagen)				
			
				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_2(self.label_miniatura_3, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_3 = imagen
				#self.Guardar_datos(imagen_3)
				##self.Guardar_datos(imagen_3)


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
				#imagen_2 = QPixmap(nombreImagen)				

				nombre = QFileInfo(nombreImagen).fileName()
				imagen = QImage(nombreImagen)
				self.Mostrar_1(self.label_miniatura_2, imagen, nombre)
				self.foto_1(imagen)
				self.imagen_2 = imagen
				#self.Guardar_datos(imagen_2)


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

				
				#self.Guardar_datos(imagen_1)


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

	def close(self):
		
		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("¿Estás seguro de que desea cancelar?")
		msg.setIcon(QMessageBox.Question)
		#msg.setInformativeText("¿Estás seguro de que ha colocado las datos correctamente?")
		msg.setWindowTitle("Cancelar")
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


#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+




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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_visualizar_users()
	interface.show()
	app.exec_()
