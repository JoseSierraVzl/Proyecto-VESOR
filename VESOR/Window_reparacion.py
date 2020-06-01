import sqlite3
from os import getcwd, makedirs
from Source_rc import *


#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import *

from Window_visor_de_imagenes import *

from Window_reparacion import *

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




#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ VENTANA DE DETALLES DE REPARACION #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		


class Window_reparacionvivienda(QDialog):
	def __init__(self, parent=None):
		super(Window_reparacionvivienda, self).__init__()
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowTitle("Reparacion de vivienda")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setObjectName("Dialog")
		self.resize(659, 301)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()		

	def initUi(self):

		#GroupBox detalle de reparacion de vivienda ==========================================================================================      		
		self.groupBox_dcrp_reparacionvv = QGroupBox(self)
		self.groupBox_dcrp_reparacionvv.setGeometry(QRect(170, 10, 481, 281))
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
		self.textEdit_dcrp_reparacionvv.setGeometry(QRect(260, 50, 211, 181))
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

		self.pushButton_anexarfotos = QPushButton(self)
		self.pushButton_anexarfotos.setGeometry(QRect(485, 250, 101, 31))
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
		self.pushButton_aceptar.setGeometry(QRect(-12, 70, 141, 31))
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
		self.pushButton_aceptar.setIcon(QIcon("Imagenes-iconos/Check_blanco.png"))
		self.pushButton_aceptar.setIconSize(QSize(15,15))
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
		self.pushButton_cancelar.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar.setIconSize(QSize(15,15))
		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Eventos =================================================================================================      		

		self.pushButton_anexarfotos.clicked.connect(self.inital_visor)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		#Funciones ================================================================================================

	def inital_visor(self):
		self.interface = Visor_de_imagenes()
		#self.interface.show()
		Visor_de_imagenes(self).exec_()
		
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ fIN DE VENTANA DE DETALLES DE  REPARACION DE VIVIENDA #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_reparacionvivienda()
	interface.show()
	app.exec_()
