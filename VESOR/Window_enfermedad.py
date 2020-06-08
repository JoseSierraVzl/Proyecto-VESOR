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






#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ VENTANA DE ENFERMEDAD +/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+


class Window_enfermedad(QDialog):
	def __init__(self, parent = None):
		super(Window_enfermedad, self).__init__()

		self.setWindowTitle("Enfermedad")
		self.setObjectName("Dialog")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)


		self.resize(600, 294)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		#Group de enfermedad ========================================================================================================	           
		self.groupBox_datos_enfermedad = QGroupBox(self)
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

		self.checkBox_27 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_27.setGeometry(QRect(40, 120, 70, 17))
		self.checkBox_27.setText("Cáncer")
		self.checkBox_27.setObjectName("checkBox_27")
		self.checkBox_27.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_26.setGeometry(QRect(40, 80, 100, 17))
		self.checkBox_26.setText("Diabetes")
		self.checkBox_26.setObjectName("checkBox_26")
		self.checkBox_26.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_25.setGeometry(QRect(40, 60, 200, 17))
		self.checkBox_25.setText("Hipertensión arterial")
		self.checkBox_25.setObjectName("checkBox_25")
		self.checkBox_25.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_23.setGeometry(QRect(40, 40, 70, 17))
		self.checkBox_23.setText("Asma")
		self.checkBox_23.setObjectName("checkBox_23")
		self.checkBox_23.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_24.setGeometry(QRect(40, 100, 200, 17))
		self.checkBox_24.setText("Cardio Vascular")
		self.checkBox_24.setObjectName("checkBox_24")
		self.checkBox_24.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_28 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_28.setGeometry(QRect(40, 140, 70, 17))
		self.checkBox_28.setText("Gastritis")
		self.checkBox_28.setObjectName("checkBox_28")
		self.checkBox_28.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_29 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_29.setGeometry(QRect(40, 160, 100, 17))
		self.checkBox_29.setText("Bronquitis")
		self.checkBox_29.setObjectName("checkBox_29")
		self.checkBox_29.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_30 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_30.setGeometry(QRect(40, 180, 200, 17))
		self.checkBox_30.setText("Cálculos de riñón")
		self.checkBox_30.setObjectName("checkBox_30")
		self.checkBox_30.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_31 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_31.setGeometry(QRect(40, 200, 70, 17))
		self.checkBox_31.setText("Sinusitis")
		self.checkBox_31.setObjectName("checkBox_31")
		self.checkBox_31.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_32 = QCheckBox(self.groupBox_datos_enfermedad)
		self.checkBox_32.setGeometry(QRect(40, 220, 70, 17))
		self.checkBox_32.setText("Otra...")
		self.checkBox_32.setObjectName("checkBox_32")
		self.checkBox_32.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
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

		self.radioButton_si_medicamentos = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_si_medicamentos.setGeometry(QRect(280, 160, 41, 17))
		self.radioButton_si_medicamentos.setObjectName("radioButton_si_medicamentos")
		self.radioButton_si_medicamentos.setText("Si")
		self.radioButton_si_medicamentos.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos = QRadioButton(self.groupBox_datos_enfermedad)
		self.radioButton_no_medicamentos.setGeometry(QRect(350, 160, 51, 17))
		self.radioButton_no_medicamentos.setObjectName("radioButton_no_medicamentos")
		self.radioButton_no_medicamentos.setText("No")
		self.radioButton_no_medicamentos.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento = QTextEdit(self.groupBox_datos_enfermedad)
		self.textEdit_medicamento.setGeometry(QRect(265, 180, 141, 61))
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

		#Eventos ==========================================================================================      			

		self.pushButton_cancelar.clicked.connect(self.close)

		self.pushButton_aceptar.clicked.connect(self.Guardar_datos)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#



	def Guardar_datos(self):

			tipo_de_enfermedad = self.Tipo_de_enfermedad()
			descripcion_enfermedad=  self.textEdit_dcrp_enfermedad.toPlainText()
			necesita_algun_medicamento = self.necesita_medicamento()
			descripcion_medicamento = self.textEdit_medicamento.toPlainText()


			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

				try:
					with sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db') as db:
						cursor = db.cursor()

					datos_insertar_Gnr = [tipo_de_enfermedad, descripcion_enfermedad, necesita_algun_medicamento,
										  descripcion_medicamento]


					cursor.execute("INSERT INTO USUARIO_DT_GNR (POSEE_ENFERMEDAD, DESCRIBA_ENFERMEDAD, TOMA_MEDICAMENTO_ENF,"
								   "DESCRIBA_MEDICAMENTO_ENF) VALUES(?,?,?,?)", datos_insertar_Gnr)

					db.commit()
					cursor.close()
					db.close()

					QMessageBox.information(self, "Enfermedad", "Datos guardados con exito.",
											QMessageBox.Ok)
				except Exception as e:
					print(e)					
					QMessageBox.critical(self, "Enfermedad", "Error desconocido.",
										 QMessageBox.Ok)

			else:
				if not QFile.exists("Base de datos"):
					makedirs("Base de datos")

				if QFile.exists("Base de datos"):
					
					try:

						datos_insertar_Gnr = [tipo_de_enfermedad, descripcion_enfermedad, necesita_algun_medicamento,
										  descripcion_medicamento]


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


						cursor.execute("INSERT INTO USUARIO_DT_GNR (POSEE_ENFERMEDAD, DESCRIBA_ENFERMEDAD, TOMA_MEDICAMENTO_ENF,"
								   		"DESCRIBA_MEDICAMENTO_ENF) VALUES(?,?,?,?)", datos_insertar_Gnr)								  

						db.commit()
						cursor.close()
						db.close()

						QMessageBox.information(self, "Enfermedad", "Datos guardados con exito.",
												QMessageBox.Ok)


					except Exception as e:
						print(e)					
						QMessageBox.critical(self, "Enfermedad", "Error desconocido.",
											 QMessageBox.Ok)



			self.textEdit_dcrp_enfermedad.clear()
			self.textEdit_medicamento.clear()
			self.checkBox_27.setChecked(False)

			self.checkBox_26.setChecked(False)
			self.checkBox_25.setChecked(False)
			self.checkBox_23.setChecked(False)
			self.checkBox_24.setChecked(False)
			self.checkBox_28.setChecked(False)		
			self.checkBox_29.setChecked(False)
			self.checkBox_30.setChecked(False)
			self.checkBox_31.setChecked(False)
			self.checkBox_32.setChecked(False)
		









	def Tipo_de_enfermedad(self):
		
		if self.checkBox_27.isChecked():
			return "Cáncer"

		elif self.checkBox_26.isChecked():
			return "Diabetes" 

		elif self.checkBox_25.isChecked():
			return "Hipertensión arterial"

		elif self.checkBox_23.isChecked():
			return "Asma"

		elif self.checkBox_24.isChecked():
			return "Cardio Vascular"

		elif self.checkBox_28.isChecked():
			return "Gastritis"

		elif self.checkBox_29.isChecked():
			return "Bronquitis"

		elif self.checkBox_30.isChecked():
			return "Cálculos de riñón"

		elif self.checkBox_31.isChecked():
			return "Sinusitis"

		elif self.checkBox_32.isChecked():
			return "Otra..."

		else:
			None



	def necesita_medicamento(self):

			if self.radioButton_si_medicamentos.isChecked():
				return "Si"

			elif self.radioButton_no_medicamentos.isChecked():
				return "No"

			else:
				None










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



if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_enfermedad()
	interface.show()
	app.exec_()
