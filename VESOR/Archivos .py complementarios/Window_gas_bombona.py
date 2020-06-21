import sys, os

import sqlite3 
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
from Window_nv_user import *

from Source_rc import *



class Window_gas_bombona(QDialog):
	def __init__(self, parent = None):
		super(Window_gas_bombona, self).__init__()


		self.setWindowTitle("Gas Bombona")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setObjectName("Dialog")
		self.resize(380, 294)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")

		self.initUi()


	def initUi(self):

		#Group de gas bombona ========================================================================================================	           
		self.groupBox_gas_bombona = QGroupBox(self)
		self.groupBox_gas_bombona.setGeometry(QRect(160, 20, 200, 251))
		self.groupBox_gas_bombona.setStyleSheet("QGroupBox{\n"
		"background-color:#E5E7EE;\n"
		"font: 75 10pt \"Comic Sans MS\";\n"
		"color: #1b231f;\n"
		"border-radius: 22px\n"
		"\n"
		"}")
		self.groupBox_gas_bombona.setAlignment(Qt.AlignCenter)
		self.groupBox_gas_bombona.setTitle("		        Gas Bombona")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_gas_bombona.setGraphicsEffect(self.shadow)

		#Opciones de discapacidad ========================================================================================================	           
		self.label_tipo_cilindro = QLabel(self.groupBox_gas_bombona)
		self.label_tipo_cilindro.setGeometry(QRect(20, 30, 160, 16))
		self.label_tipo_cilindro.setStyleSheet("background-color:#4466B8;\n"
		"color: rgb(255, 255, 255);\n"
		"border-radius: 5px;\n"
		"font-size: 12px;")
		self.label_tipo_cilindro.setAlignment(Qt.AlignCenter)
		self.label_tipo_cilindro.setText("Tipo de cilindro que posee: ")

		self.checkBox_27 =QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_27.setGeometry(QRect(50, 135, 200, 17))
		self.checkBox_27.setText("PDVSA Gas")
		self.checkBox_27.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26 = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_26.setGeometry(QRect(50, 95, 200, 17))
		self.checkBox_26.setText("Tropiven")
		self.checkBox_26.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25 = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_25.setGeometry(QRect(50, 75, 200, 17))
		self.checkBox_25.setText("Dani el gas")
		self.checkBox_25.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23 = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_23.setGeometry(QRect(50, 55, 220, 17))
		self.checkBox_23.setText("Hermagas")
		self.checkBox_23.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24 = QCheckBox(self.groupBox_gas_bombona)
		self.checkBox_24.setGeometry(QRect(50, 115, 200, 17))
		self.checkBox_24.setText("Autogas")

		self.checkBox_24.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		#QSpinBox de cantidad de bombonas  ==========================================================================================      		

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

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		#Frama de menu  ==========================================================================================      		

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
		self.label_25.setText("Gas Bombona")
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


		
		#Boton Aceptar ==========================================================================================      		
		self.pushButton_aceptar = QPushButton(self.frame_2)
		self.pushButton_aceptar.setGeometry(QRect(-12, 80, 141, 31))
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
		self.pushButton_cancelar.setIcon(QIcon("Imagenes-iconos/Cancelar_blanco.png"))
		self.pushButton_cancelar.setIconSize(QSize(15,15))
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#========================================= #Eventos# ==================================================================

		self.pushButton_cancelar.clicked.connect(self.close)

		self.pushButton_aceptar.clicked.connect(self.Guardar_datos)
		
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#======================================== #Funciones# ==================================================================


	def Guardar_datos(self):


			tipo_de_cilindro = self.Tipo_de_cilindro()
			cantidad_de_bombonas = int(self.num_bombonas.value())

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):
			

				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db') as db:
						cursor = db.cursor()

					datos_insertar_Gnr = [tipo_de_cilindro, cantidad_de_bombonas]

					cursor.execute("INSERT INTO USUARIO_DT_VV(TIPO_DE_CILINDRO, CANTIDAD_DE_BOMBONAS) VALUES(?,?)", datos_insertar_Gnr)

					conexion.commit()
					cursor.close()
					conexion.close()

					QMessageBox.information(self, "GAS Bombona", "Datos guardados con exito.",
											QMessageBox.Ok)
				except Exception as e:
					print(e)					
					QMessageBox.critical(self, "GAS Bombona", "Error desconocido.",
										 QMessageBox.Ok)

			else:
				if not QFile.exists("Base de datos"):
					makedirs("Base de datos")

				if QFile.exists("Base de datos"):
					try:

						with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db') as db:
							cursor = db.cursor()

						datos_insertar_Gnr = [tipo_de_cilindro, cantidad_de_bombonas]

							
						cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_DT_VV(ID INTEGER PRIMARY KEY,METROS_CUADRADOS TEXT, DESCRIPCION TEXT, NECESITA_REPARACION TEXT,"
									"AGUA_POTABLE TEXT, AGUA_SERVIDAS TEXT, GAS_DIRECTO TEXT, GAS_BOMBONA TEXT,"
									"TIPO_DE_CILINDRO TEXT, CANTIDAD_DE_BOMBONAS INT"
									"INTERNET TEXT, ElECTRICIDAD TEXT,"
									"TELEFONO_FIJO TEXT, DESCRIPCION_REPARACION TEXT, NECESITA_LINEBLANCA TEXT,"
									"FOTO_ANEXADA1 BLOB, FOTO_ANEXADA2 BLOB, FOTO_ANEXADA3 BLOB, FOTO_ANEXADA4 BLOB, FOTO_ANEXADA5,FOTO_ANEXADA6 BLOB)")

						cursor.execute("INSERT INTO USUARIO_DT_VV(TIPO_DE_CILINDRO, CANTIDAD_DE_BOMBONAS) VALUES(?,?)", datos_insertar_Gnr)

						db.commit()
						cursor.close()
						db.close()

						QMessageBox.information(self, "Gas Bombona", "Datos guardados con exito.",
												QMessageBox.Ok)


					except Exception as e:
						print(e)					
						QMessageBox.critical(self, "Gas Bombona", "Error desconocido.",
											 QMessageBox.Ok)








	def Tipo_de_cilindro(self):

		if self.checkBox_27.isChecked():
			return "PDVSA Gas"
		elif self.checkBox_26.isChecked():
			return "Tropiven"

		elif self.checkBox_25.isChecked():
			return "Dani el gas" 

		elif self.checkBox_23.isChecked():
			return "Hermagas" 

		elif self.checkBox_24.isChecked():
			return "Autogas" 

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

		#=#=#=#=#=#=#=#=#=#=self.destroy()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	interface = Window_gas_bombona()
	interface.show()
	app.exec_()
