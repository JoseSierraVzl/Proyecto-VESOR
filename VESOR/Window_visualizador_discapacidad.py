import sqlite3
from os import getcwd, makedirs
from Source_rc import *


from Window_visualizar_user import *

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
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,QSpinBox,QTextBrowser)





#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ Ventana de Discapacidad +/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+

class Window_visualizar_discapacidad(QDialog):
	def __init__(self, parent = None):
		super(Window_visualizar_discapacidad, self).__init__()
		self

		self.setObjectName("Dialog")
		self.setWindowTitle("Discapacidad")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.resize(548, 421)
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
						"font: 11pt Comic Sans MS;\n"
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

		#TextBrowser

		QTextBrowserStyle = ("QTextBrowser{background-color:#12191D;\n"
							"border-radius: 22px;\n"
							"}")

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
		self.label_titulo_menu_1.setGeometry(QRect(5,20, 121,31))
		self.label_titulo_menu_1.setText("DISCAPACIDAD")
		self.label_titulo_menu_1.setStyleSheet(Label_titulo)	
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Label titulo ========================================================================================================	           				
		
		#Label datos discapacidad
		self.label_titulo_discapacidad = QLabel(self.frame_principal)
		self.label_titulo_discapacidad.setGeometry(QRect(50,20,271,16))
		self.label_titulo_discapacidad.setStyleSheet(Style_titulos_de_grupo)
		self.label_titulo_discapacidad.setText("Datos de Discapacidad")
		self.label_titulo_discapacidad.setAlignment(Qt.AlignCenter)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Label contenidos de datas discapacidad ========================================================================================================	           

		#label posee discapacidad
		self.label_posee_discapacidad = QLabel(self.frame_principal)
		self.label_posee_discapacidad.setGeometry(QRect(40, 50,141,16))
		self.label_posee_discapacidad.setStyleSheet(Label_titulo_de_contenidos)
		self.label_posee_discapacidad.setText("Posee Discapacidad:")
		self.label_posee_discapacidad.setAlignment(Qt.AlignCenter)

		self.label_posee_discapacida_contenido = QLabel(self.frame_principal)
		self.label_posee_discapacida_contenido.setGeometry(QRect(40, 70,141,16))
		self.label_posee_discapacida_contenido.setStyleSheet(Label_contenido)
		self.label_posee_discapacida_contenido.setAlignment(Qt.AlignCenter)
		###

		#label toma medicamento
		self.label_medicamento = QLabel(self.frame_principal)
		self.label_medicamento.setGeometry(QRect(190,50,141,16))
		self.label_medicamento.setStyleSheet(Label_titulo_de_contenidos)
		self.label_medicamento.setText("Toma medicamento:")
		self.label_medicamento.setAlignment(Qt.AlignCenter)

		self.label_medicamento_contenido = QLabel(self.frame_principal)
		self.label_medicamento_contenido.setGeometry(QRect(190, 70,141,16))
		self.label_medicamento_contenido.setStyleSheet(Label_contenido)
		self.label_medicamento_contenido.setAlignment(Qt.AlignCenter)
		###

		#label Insumo medico
		self.label_insumo_medico = QLabel(self.frame_principal)
		self.label_insumo_medico.setGeometry(QRect(110,100,141,16))
		self.label_insumo_medico.setStyleSheet(Label_titulo_de_contenidos)
		self.label_insumo_medico.setText("Insumo medico:")
		self.label_insumo_medico.setAlignment(Qt.AlignCenter)

		self.label_insumo_medico_contenido = QLabel(self.frame_principal)
		self.label_insumo_medico_contenido.setGeometry(QRect(110, 120,141,16))
		self.label_insumo_medico_contenido.setStyleSheet(Label_contenido)
		self.label_insumo_medico_contenido.setAlignment(Qt.AlignCenter)
		###

		#Descripcion de discapacidad
		self.label_descripcion_discapacidad = QLabel(self.frame_principal)
		self.label_descripcion_discapacidad.setGeometry(QRect(90,150,191,16))
		self.label_descripcion_discapacidad.setStyleSheet(Label_titulo_de_contenidos)
		self.label_descripcion_discapacidad.setText("Descripcion de Discapacidad:")
		self.label_descripcion_discapacidad.setAlignment(Qt.AlignCenter)

		self.Text_descripcion = QTextBrowser(self.frame_principal)
		self.Text_descripcion.setGeometry(QRect(40,170,291,81))
		self.Text_descripcion.setStyleSheet(QTextBrowserStyle)
		###

		#Descripcion de medicamento
		self.label_descripcion_medicamento = QLabel(self.frame_principal)
		self.label_descripcion_medicamento.setGeometry(QRect(90,270,191,16))
		self.label_descripcion_medicamento.setStyleSheet(Label_titulo_de_contenidos)
		self.label_descripcion_medicamento.setText("Descripcion de Medicamento:")
		self.label_descripcion_medicamento.setAlignment(Qt.AlignCenter)

		self.Text_descripcion = QTextBrowser(self.frame_principal)
		self.Text_descripcion.setGeometry(QRect(40,290,291,81))
		self.Text_descripcion.setStyleSheet(QTextBrowserStyle)
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#Push Button del menu (frame principal) ========================================================================================================	           

		#Button Volver atras
		self.PushButton_volver_atras = QPushButton(self.frame_menu)
		self.PushButton_volver_atras.setGeometry(QRect(0,90,121,31))
		self.PushButton_volver_atras.setText("Volver atras")
		self.PushButton_volver_atras.setStyleSheet(QPushButtonStyle)
		###

if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_visualizar_discapacidad()
	interface.show()
	app.exec_()
