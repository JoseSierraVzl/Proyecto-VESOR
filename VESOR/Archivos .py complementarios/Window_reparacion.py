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

		self.checkBox = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox.setGeometry(QRect(20, 60, 180, 17))
		self.checkBox.setText("Arreglo o falta de techos")
		self.checkBox.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_2 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_2.setGeometry(QRect(20, 80, 180, 17))
		self.checkBox_2.setText("Friso de pared")
		self.checkBox_2.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_3 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_3.setGeometry(QRect(20, 100, 180, 17))
		self.checkBox_3.setText("Falta de pintura ")
		self.checkBox_3.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_4 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_4.setGeometry(QRect(20, 120, 180, 17))
		self.checkBox_4.setText("Arreglo de pisos")
		self.checkBox_4.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_5 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_5.setGeometry(QRect(20, 140, 180, 17))
		self.checkBox_5.setText("Sistema eléctrico")
		self.checkBox_5.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_6 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_6.setGeometry(QRect(20, 160, 180, 17))
		self.checkBox_6.setText("Sistema de agua")
		self.checkBox_6.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_7 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_7.setGeometry(QRect(20, 180, 180, 17))
		self.checkBox_7.setText("Sistema de aguas servida")
		self.checkBox_7.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_8 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_8.setGeometry(QRect(20, 200, 180, 17))
		self.checkBox_8.setText("Falta de ventanas")
		self.checkBox_8.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_9 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_9.setGeometry(QRect(20, 220, 180, 17))
		self.checkBox_9.setText("Falta de puertas")
		self.checkBox_9.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_10 = QCheckBox(self.groupBox_dcrp_reparacionvv)
		self.checkBox_10.setGeometry(QRect(20, 240, 180, 17))
		self.checkBox_10.setText("Otras...")
		self.checkBox_10.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Botones para guardar y ver fotos  ==========================================================================================      		

		self.pushButton_anexarfotos = QPushButton(self)
		self.pushButton_anexarfotos.setGeometry(QRect(490, 250, 101, 31))
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

		self.pushButton_cancelar.clicked.connect(self.close)

		self.pushButton_aceptar.clicked.connect(self.Guardar_datos)

		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	


	#Funcion para guardar los datos de la vivienda ==========================================================================		

	def Guardar_datos(self):

			Descripcion_de_reparacion = self.textEdit_dcrp_reparacionvv.toPlainText()
			Tipo_de_reparacion = self.Opcion_reparacion_vivienda()
			Linea_blanca = self.Linea_blanca()

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOS_VV.db"):

				

				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db') as db:
						cursor = db.cursor()

					datos_insertar_Gnr = [Descripcion_de_reparacion, Tipo_de_reparacion, Linea_blanca]

					cursor.execute("INSERT INTO USUARIO_DT_VV(DESCRIPCION_REPARACION, NECESITA_REPARACION, NECESITA_LINEBLANCA) VALUES(?,?,?)", datos_insertar_Gnr)

					conexion.commit()
					cursor.close()
					conexion.close()

					QMessageBox.information(self, "Reparación de Vivienda", "Datos guardados con exito.",
											QMessageBox.Ok)
				except Exception as e:
					print(e)					
					QMessageBox.critical(self, "Reparación de Vivienda", "Error desconocido.",
										 QMessageBox.Ok)

			else:
				if not QFile.exists("Base de datos"):
					makedirs("Base de datos")

				if QFile.exists("Base de datos"):
					try:
						datos_insertar_Gnr = [Descripcion_de_reparacion, Tipo_de_reparacion, Linea_blanca]

						with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOS_VV.db') as db:
							cursor = db.cursor()
							
						cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO_DT_VV(ID INTEGER PRIMARY KEY,METROS_CUADRADOS TEXT, DESCRIPCION TEXT, NECESITA_REPARACION TEXT,"
									"AGUA_POTABLE TEXT, AGUA_SERVIDAS TEXT, GAS_DIRECTO TEXT, GAS_BOMBONA TEXT,"
									"TIPO_DE_CILINDRO TEXT, CANTIDAD_DE_BOMBONAS INT"
									"INTERNET TEXT, ElECTRICIDAD TEXT,"
									"TELEFONO_FIJO TEXT, DESCRIPCION_REPARACION TEXT, NECESITA_LINEBLANCA TEXT,"
									"FOTO_ANEXADA1 BLOB, FOTO_ANEXADA2 BLOB, FOTO_ANEXADA3 BLOB, FOTO_ANEXADA4 BLOB, FOTO_ANEXADA5,FOTO_ANEXADA6 BLOB)")

						cursor.execute("INSERT INTO USUARIO_DT_VV(DESCRIPCION_REPARACION, NECESITA_REPARACION, NECESITA_LINEBLANCA) VALUES(?,?,?)", datos_insertar_Gnr)

						db.commit()
						cursor.close()
						db.close()

						QMessageBox.information(self, "Reparación de Vivienda", "Datos guardados con exito.",
												QMessageBox.Ok)


					except Exception as e:
						print(e)					
						QMessageBox.critical(self, "Reparación de Vivienda", "Error desconocido.",
											 QMessageBox.Ok)


			self.textEdit_dcrp_reparacionvv.clear()

			self.checkBox.setChecked(False)
			self.checkBox_2.setChecked(False)
			self.checkBox_3.setChecked(False)
			self.checkBox_4.setChecked(False)
			self.checkBox_5.setChecked(False)
			self.checkBox_6.setChecked(False)
			self.checkBox_7.setChecked(False)
			self.checkBox_8.setChecked(False)
			self.checkBox_9.setChecked(False)
			self.checkBox_10.setChecked(False)

			self.checkBox_Lavadora.setChecked(False)
			self.checkBox_Nevera.setChecked(False)
			self.checkBox_Cocina.setChecked(False)
			self.checkBox_Aireacondicionado.setChecked(False)



















	#Funciones ================================================================================================


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
			return "No"


	def Opcion_reparacion_vivienda(self):

		if self.checkBox.isChecked():
			return "Arreglo o falta de techos"
		elif self.checkBox_2.isChecked():
			return "Friso de pared"
		elif self.checkBox_3.isChecked():
			return " Falta de pintura"
		elif self.checkBox_4.isChecked():
			return "Arreglo de pisos"
		elif self.checkBox_5.isChecked():
			return "Sistema eléctrico"
		elif self.checkBox_6.isChecked():
			return "Sistema de agua"
		elif self.checkBox_7.isChecked():
			return "Sistema de aguas servida"
		elif self.checkBox_8.isChecked():
			return "Falta de Ventanas"
		elif self.checkBox_9.isChecked():
			return "Falta de puertas"
		elif self.checkBox_10.isChecked():
			return "Otras..."
		else:
			"No"


	def inital_visor(self):
		self.interface = Visor_de_imagenes()
		#self.interface.show()
		Visor_de_imagenes(self).exec_()


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
		
#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+ fIN DE VENTANA DE DETALLES DE  REPARACION DE VIVIENDA #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_reparacionvivienda()
	interface.show()
	app.exec_()
