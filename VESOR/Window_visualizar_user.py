import sqlite3
from os import getcwd, makedirs
from Source_rc import *


#from Window_visualizador_discapacidad import *

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
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,QSpinBox)





class Window_visualizar_users(QDialog):
	def __init__(self, parent = None):
		super(Window_visualizar_users, self).__init__()

		self.setObjectName("Dialog")
		self.setWindowTitle("Datos de usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.resize(548, 425)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()


	def initUi(self):

	
		#Stylos ========================================================================================================	           
		#Frame princiapl
		Frame_principal_SetStyleSheet = ("QFrame{background-color:#E5E7EE;\n"		
										"border-radius: 22px}")
		###

		#Frame menu
		Frame_menu = ("QFrame{\n"
					  "background-color:#12191D;\n"
					  "border-radius: 45px;\n"
					  "}")

		Label_titulo = ("QLabel{\n"
						"color:rgb(255, 255, 255);\n"
						"font: 12pt Comic Sans MS;\n"
						"border-radius: 6px;\n"
						"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"

						"}")
		###

		#Frame menu
		Style_titulos_de_grupo = ("QLabel{background-color:#E5E7EE;\n"
								 "color:#000000;\n"
								 "border-radius: 5px\n"
								 "}")

		###

		#Label titulos de los contenidos

		Label_titulo_de_contenidos = ("QLabel{background-color:#4466B8;\n"
										"color: rgb(255, 255, 255);\n"
										"border-radius: 5px\n"
										"}")

		Label_contenido =  ("QLabel{background-color:#12191D;\n"
										"color:#ffffff;\n"
										"border-radius: 5px\n"
										"}")
		###

		#QPushButton menu (Frame principal)
		QPushButtonStyle = 		("QPushButton{\n"
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

		###

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Frame princiapl ========================================================================================================	           
		self.frame_principal = QFrame(self)
		self.frame_principal.setGeometry(QRect(160,20,371,381))
		self.frame_principal.setStyleSheet(Frame_principal_SetStyleSheet)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Frame Menu ========================================================================================================	           
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(20,20,121,381))
		self.frame_menu.setStyleSheet(Frame_menu)

		self.label_titulo_menu_1 = QLabel(self.frame_menu)
		self.label_titulo_menu_1.setGeometry(QRect(35,10, 81,31))
		self.label_titulo_menu_1.setText("DATOS")
		self.label_titulo_menu_1.setStyleSheet(Label_titulo)

		self.label_titulo_menu_2 = QLabel(self.frame_menu)
		self.label_titulo_menu_2.setGeometry(QRect(10,35, 121,31))
		self.label_titulo_menu_2.setText("DE USUARIO")
		self.label_titulo_menu_2.setStyleSheet(Label_titulo)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Label titulo ========================================================================================================	           		
		#Label datos generales
		self.label_titulo_datosgenerales = QLabel(self.frame_principal)
		self.label_titulo_datosgenerales.setGeometry(QRect(50,20,271,16))
		self.label_titulo_datosgenerales.setStyleSheet(Style_titulos_de_grupo)
		self.label_titulo_datosgenerales.setText("Datos generales")
		self.label_titulo_datosgenerales.setAlignment(Qt.AlignCenter)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Label contenidos de datos generales ========================================================================================================	           

		#label 1°Nombre 
		self.label_1_nombre = QLabel(self.frame_principal)
		self.label_1_nombre.setGeometry(QRect(50, 60,131,16))
		self.label_1_nombre.setStyleSheet(Label_titulo_de_contenidos)
		self.label_1_nombre.setText("1°Nombre:")
		self.label_1_nombre.setAlignment(Qt.AlignCenter)

		self.label_1_nombre_contenido = QLabel(self.frame_principal)
		self.label_1_nombre_contenido.setGeometry(QRect(50, 80,131,16))
		self.label_1_nombre_contenido.setStyleSheet(Label_contenido)
		self.label_1_nombre_contenido.setAlignment(Qt.AlignCenter)
		###

		#label 2°Nombre 
		self.label_2_nombre = QLabel(self.frame_principal)
		self.label_2_nombre.setGeometry(QRect(50,110,131,16))
		self.label_2_nombre.setStyleSheet(Label_titulo_de_contenidos)
		self.label_2_nombre.setText("2°Nombre:")
		self.label_2_nombre.setAlignment(Qt.AlignCenter)

		self.label_2_nombre_contenido = QLabel(self.frame_principal)
		self.label_2_nombre_contenido.setGeometry(QRect(50, 130,131,16))
		self.label_2_nombre_contenido.setStyleSheet(Label_contenido)
		self.label_2_nombre_contenido.setAlignment(Qt.AlignCenter)
		###

		#label 1°Apellido
		self.label_1_apellido = QLabel(self.frame_principal)
		self.label_1_apellido.setGeometry(QRect(190,60,131,16))
		self.label_1_apellido.setStyleSheet(Label_titulo_de_contenidos)
		self.label_1_apellido.setText("1°Apellido:")
		self.label_1_apellido.setAlignment(Qt.AlignCenter)

		self.label_1_apellido_contenido = QLabel(self.frame_principal)
		self.label_1_apellido_contenido.setGeometry(QRect(190, 80,131,16))
		self.label_1_apellido_contenido.setStyleSheet(Label_contenido)
		self.label_1_apellido_contenido.setAlignment(Qt.AlignCenter)
		###

		#label 2°Apellido
		self.label_2_apellido = QLabel(self.frame_principal)
		self.label_2_apellido.setGeometry(QRect(190,110,131,16))
		self.label_2_apellido.setStyleSheet(Label_titulo_de_contenidos)
		self.label_2_apellido.setText("2°Apellido:")
		self.label_2_apellido.setAlignment(Qt.AlignCenter)

		self.label_2_apellido_contenido = QLabel(self.frame_principal)
		self.label_2_apellido_contenido.setGeometry(QRect(190, 130,131,16))
		self.label_2_apellido_contenido.setStyleSheet(Label_contenido)
		self.label_2_apellido_contenido.setAlignment(Qt.AlignCenter)
		###

		#label cedula
		self.label_cedula = QLabel(self.frame_principal)
		self.label_cedula.setGeometry(QRect(50,160,131,16))
		self.label_cedula.setStyleSheet(Label_titulo_de_contenidos)
		self.label_cedula.setText("Cedula:")
		self.label_cedula.setAlignment(Qt.AlignCenter)

		self.label_cedula_contenido = QLabel(self.frame_principal)
		self.label_cedula_contenido.setGeometry(QRect(50, 180,131,16))
		self.label_cedula_contenido.setStyleSheet(Label_contenido)
		self.label_cedula_contenido.setAlignment(Qt.AlignCenter)
		###

		#label fecha de nacimiento
		self.label_fhc_nacimiento = QLabel(self.frame_principal)
		self.label_fhc_nacimiento.setGeometry(QRect(190,160,131,16))
		self.label_fhc_nacimiento.setStyleSheet(Label_titulo_de_contenidos)
		self.label_fhc_nacimiento.setText("Fecha de nacimiento:")
		self.label_fhc_nacimiento.setAlignment(Qt.AlignCenter)

		self.label_fhc_nacimiento_contenido = QLabel(self.frame_principal)
		self.label_fhc_nacimiento_contenido.setGeometry(QRect(190, 180,131,16))
		self.label_fhc_nacimiento_contenido.setStyleSheet(Label_contenido)
		self.label_fhc_nacimiento_contenido.setAlignment(Qt.AlignCenter)
		###

		#label 1° Telefono
		self.label_1_telefono = QLabel(self.frame_principal)
		self.label_1_telefono.setGeometry(QRect(50,210,131,16))
		self.label_1_telefono.setStyleSheet(Label_titulo_de_contenidos)
		self.label_1_telefono.setText("1°Telefono:")
		self.label_1_telefono.setAlignment(Qt.AlignCenter)

		self.label_1_telefono_contenido = QLabel(self.frame_principal)
		self.label_1_telefono_contenido.setGeometry(QRect(50, 230,131,16))
		self.label_1_telefono_contenido.setStyleSheet(Label_contenido)
		self.label_1_telefono_contenido.setAlignment(Qt.AlignCenter)
		###

		#label 2° Telefono
		self.label_2_telefono = QLabel(self.frame_principal)
		self.label_2_telefono.setGeometry(QRect(190,210,131,16))
		self.label_2_telefono.setStyleSheet(Label_titulo_de_contenidos)
		self.label_2_telefono.setText("2°Telefono:")
		self.label_2_telefono.setAlignment(Qt.AlignCenter)

		self.label_2_telefono_contenido = QLabel(self.frame_principal)
		self.label_2_telefono_contenido.setGeometry(QRect(190, 230,131,16))
		self.label_2_telefono_contenido.setStyleSheet(Label_contenido)
		self.label_2_telefono_contenido.setAlignment(Qt.AlignCenter)
		###
		

		#label Cedula
		self.label_cedula = QLabel(self.frame_principal)
		self.label_cedula.setGeometry(QRect(50,260,131,16))
		self.label_cedula.setStyleSheet(Label_titulo_de_contenidos)
		self.label_cedula.setText("Cedula:")
		self.label_cedula.setAlignment(Qt.AlignCenter)

		self.label_cedula_contenido = QLabel(self.frame_principal)
		self.label_cedula_contenido.setGeometry(QRect(50, 280,131,16))
		self.label_cedula_contenido.setStyleSheet(Label_contenido)
		self.label_cedula_contenido.setAlignment(Qt.AlignCenter)
		###

		#label Embarazada:
		self.label_embarazada = QLabel(self.frame_principal)
		self.label_embarazada.setGeometry(QRect(190,260,131,16))
		self.label_embarazada.setStyleSheet(Label_titulo_de_contenidos)
		self.label_embarazada.setText("Embarazada:")
		self.label_embarazada.setAlignment(Qt.AlignCenter)

		self.label_embarazada_contenido = QLabel(self.frame_principal)
		self.label_embarazada_contenido.setGeometry(QRect(190, 280,131,16))
		self.label_embarazada_contenido.setStyleSheet(Label_contenido)
		self.label_embarazada_contenido.setAlignment(Qt.AlignCenter)
		###
		
		#label Lactante
		self.label_lactante = QLabel(self.frame_principal)
		self.label_lactante.setGeometry(QRect(50,310,131,16))
		self.label_lactante.setStyleSheet(Label_titulo_de_contenidos)
		self.label_lactante.setText("Lactante:")
		self.label_lactante.setAlignment(Qt.AlignCenter)

		self.label_lactante_contenido = QLabel(self.frame_principal)
		self.label_lactante_contenido.setGeometry(QRect(50, 330,131,16))
		self.label_lactante_contenido.setStyleSheet(Label_contenido)
		self.label_lactante_contenido.setAlignment(Qt.AlignCenter)
		###

		#label Pensionado
		self.label_pensionado = QLabel(self.frame_principal)
		self.label_pensionado.setGeometry(QRect(190,310,131,16))
		self.label_pensionado.setStyleSheet(Label_titulo_de_contenidos)
		self.label_pensionado.setText("Pensionado:")
		self.label_pensionado.setAlignment(Qt.AlignCenter)

		self.label_pensionado_contenido = QLabel(self.frame_principal)
		self.label_pensionado_contenido.setGeometry(QRect(190, 330,131,16))
		self.label_pensionado_contenido.setStyleSheet(Label_contenido)
		self.label_pensionado_contenido.setAlignment(Qt.AlignCenter)
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#Push Button del menu (frame principal) ========================================================================================================	           

		#Button Volver atras
		self.PushButton_volver_atras = QPushButton(self.frame_menu)
		self.PushButton_volver_atras.setGeometry(QRect(0,90,121,31))
		self.PushButton_volver_atras.setText("Volver atras")
		self.PushButton_volver_atras.setStyleSheet(QPushButtonStyle)
		self.PushButton_volver_atras.setIcon(QIcon("Imagenes-iconos/Flecha_izquierda.png"))
		self.PushButton_volver_atras.setIconSize(QSize(20,20))
		###
		
		#Button Discapacidad
		self.PushButton_discapacidad = QPushButton(self.frame_menu)
		self.PushButton_discapacidad.setGeometry(QRect(0,160,121,31))
		self.PushButton_discapacidad.setText("Discapacidad")
		self.PushButton_discapacidad.setStyleSheet(QPushButtonStyle)
		self.PushButton_discapacidad.setIcon(QIcon("Imagenes-iconos/discapacidad_blanco.png"))
		self.PushButton_discapacidad.setIconSize(QSize(23,23))		
		###

		#Button Enfermedad
		self.PushButton_enfermedad = QPushButton(self.frame_menu)
		self.PushButton_enfermedad.setGeometry(QRect(0,190,121,31))
		self.PushButton_enfermedad.setText(" Enfermedad")
		self.PushButton_enfermedad.setStyleSheet(QPushButtonStyle)
		self.PushButton_enfermedad.setIcon(QIcon("Imagenes-iconos/Enfermedad.png"))
		self.PushButton_enfermedad.setIconSize(QSize(18,18))		
		###

		#Button Ubicacion
		self.PushButton_ubicacion = QPushButton(self.frame_menu)
		self.PushButton_ubicacion.setGeometry(QRect(-8,220,121,31))
		self.PushButton_ubicacion.setText("Ubicacion")
		self.PushButton_ubicacion.setStyleSheet(QPushButtonStyle)
		self.PushButton_ubicacion.setIcon(QIcon("Imagenes-iconos/ubicacion.png"))
		self.PushButton_ubicacion.setIconSize(QSize(18,18))		
		###

		#Button Vivienda
		self.PushButton_vivienda = QPushButton(self.frame_menu)
		self.PushButton_vivienda.setGeometry(QRect(-10,250,121,31))
		self.PushButton_vivienda.setText(" Vivienda")
		self.PushButton_vivienda.setStyleSheet(QPushButtonStyle)
		self.PushButton_vivienda.setIcon(QIcon("Imagenes-iconos/casa_blanco.png"))
		self.PushButton_vivienda.setIconSize(QSize(15,15))

		###

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Eventos ========================================================================================================	           

		self.PushButton_discapacidad.clicked.connect(self.Open_discapacidad)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Funciones ========================================================================================================	           

	def Open_discapacidad(self):

		Window_visualizar_discapacidad(self).exec_()

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#




if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_visualizar_users()
	interface.show()
	app.exec_()
