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




class Visor_de_imagenes(QDialog):
	def __init__(self, parent=None):
		super(Visor_de_imagenes, self).__init__()

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
		self.label_miniatura_1 = QLabelClickable(self)
		self.label_miniatura_1.setGeometry(QRect(170, 20, 171, 121))
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
		self.label_miniatura_1_nombre = QLabel(self)
		self.label_miniatura_1_nombre.setGeometry(QRect(180,120,151,16))
		self.label_miniatura_1_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_1_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		#Miniatura_2
		self.label_miniatura_2 = QLabelClickable(self)
		self.label_miniatura_2.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2.setGeometry(QRect(370, 20, 171, 121))
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
		self.label_miniatura_2_nombre = QLabel(self)
		self.label_miniatura_2_nombre.setGeometry(QRect(380,120,151,16))
		self.label_miniatura_2_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_2_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")




		#Miniatura_3
		self.label_miniatura_3 = QLabelClickable(self)
		self.label_miniatura_3.setGeometry(QRect(570, 20, 171, 121))
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
		self.label_miniatura_3_nombre = QLabel(self)
		self.label_miniatura_3_nombre.setGeometry(QRect(580,120,151,16))
		self.label_miniatura_3_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_3_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		
		#Miniatura_4
		self.label_miniatura_4 = QLabelClickable(self)
		self.label_miniatura_4.setGeometry(QRect(170, 200, 171, 121))
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
		self.label_miniatura_4_nombre = QLabel(self)
		self.label_miniatura_4_nombre.setGeometry(QRect(180,300,151,16))
		self.label_miniatura_4_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_4_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")


		
		#Miniatura_5
		self.label_miniatura_5 = QLabelClickable(self)
		self.label_miniatura_5.setGeometry(QRect(370, 200, 171, 121))
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
		self.label_miniatura_5_nombre = QLabel(self)
		self.label_miniatura_5.setObjectName("label_miniatura_5_nombre")
		self.label_miniatura_5_nombre.setGeometry(QRect(380,300,151,16))
		self.label_miniatura_5_nombre.setAlignment(Qt.AlignCenter)
		self.label_miniatura_5_nombre.setStyleSheet("QLabel{\n"
		"color: #333333;\n"
		"border-radius: 8px;\n"
		""
		"}")

		#Miniatura_6
		self.label_miniatura_6 = QLabelClickable(self)
		self.label_miniatura_6.setGeometry(QRect(570, 200, 171, 121))
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
		self.label_miniatura_6_nombre = QLabel(self)
		self.label_miniatura_6_nombre.setGeometry(QRect(580,300,151,16))
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
		self.pushButton_5.setGeometry(QRect(-2, 70, 121, 31))
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
		self.pushButton_5.setText("Guardar")
		self.pushButton_5.setIcon(QIcon("Imagenes-iconos/Guardar_blanco.png"))
		self.pushButton_5.setIconSize(QSize(18,18))
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
		self.pushButton_8.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_8.setIconSize(QSize(15,15))
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


	def Mostrar_5(self, label, imagen, nombre, posicionX= 570):
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
		self.animacionMostar.setEndValue(QRect(570, 200, 171, 121))
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

	def Mostrar_4 (self, label, imagen, nombre, posicionX= 370):
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
		self.animacionMostar.setEndValue(QRect(370, 200, 171, 121))
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


	def Mostrar_3 (self, label, imagen, nombre, posicionX= 170):
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
		self.animacionMostar.setEndValue(QRect(170, 200, 171, 121))
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


	def Mostrar_2 (self, label, imagen, nombre, posicionX= 570):
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
		self.animacionMostar.setEndValue(QRect(570, 20, 171, 121))
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

	def Mostrar_1 (self, label, imagen, nombre, posicionX= 370):
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
		self.animacionMostar.setEndValue(QRect(370, 20, 171, 121))
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

	def Mostrar(self,label, imagen, nombre, posicionX=170):
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
		self.animacionMostar.setEndValue(QRect(170, 20, 171, 121))
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
	interface = Visor_de_imagenes()
	interface.show()
	app.exec_()

