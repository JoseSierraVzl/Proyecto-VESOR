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







#/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+ Ventana de Discapacidad +/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+/+


class Window_discapacidad(QDialog):
	def __init__(self, parent = None):
		super(Window_discapacidad, self).__init__()

		self.setObjectName("Dialog")
		self.setWindowTitle("Discapacidad")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.resize(590, 294)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.initUi()

	def initUi(self):

		#Group de discapacidad ========================================================================================================	           
		self.groupBox_datosdiscapacidad = QGroupBox(self)
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
		self.textEdit_dcrp_discapacidad.setStyleSheet("QTextEdit{\n"
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

		self.checkBox_27 =QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_27.setGeometry(QRect(10, 120, 200, 17))
		self.checkBox_27.setText("Discapacidad Motriz")
		self.checkBox_27.setToolTip("Implica una disminución de la movilidad total o parcial \n" 
									"de uno o más miembros del cuerpo, la cual dificulta la realización\n"
									"de actividades motoras convencionales.")
		self.checkBox_27.setObjectName("checkBox_27")
		self.checkBox_27.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_26 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_26.setGeometry(QRect(10, 80, 200, 17))
		self.checkBox_26.setText("Discapacidad Auditiva")
		self.checkBox_26.setToolTip("Es un déficit total o parcial en la percepción que se evalúa\n" 
									"por el grado de pérdida de la audición en cada oído")
		self.checkBox_26.setObjectName("checkBox_26")
		self.checkBox_26.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_25 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_25.setGeometry(QRect(10, 60, 200, 17))
		self.checkBox_25.setText("Discapacidad Visual")
		self.checkBox_25.setObjectName("checkBox_25")
		self.checkBox_25.setToolTip("Es de acuerdo al grado de limitación de la visión, se suele distinguir entre personas ciegas,\n" 
									"que no obtienen información a través del canal visual; y personas con disminución visual,\n"
									"quienes en cambio sí la adquieren mediante dicho canal pero con algún déficit.")
		self.checkBox_25.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_23 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_23.setGeometry(QRect(10, 40, 220, 17))
		self.checkBox_23.setText("Discapacidad Intelectual o mental")
		self.checkBox_23.setObjectName("checkBox_23")
		self.checkBox_23.setToolTip("Las personas con discapacidad intelectual tienen algunas limitaciones\n"
									"para funcionar en su vida diaria; les cuesta más aprender habilidades\n"
									"sociales e intelectuales para acutar en diferentes situaciones.")
		self.checkBox_23.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
		"color: #000000;\n"
		"font-size: 12px}")

		self.checkBox_24 = QCheckBox(self.groupBox_datosdiscapacidad)
		self.checkBox_24.setGeometry(QRect(10, 100, 200, 17))
		self.checkBox_24.setText("Discapacidad visceral")
		self.checkBox_24.setObjectName("checkBox_24")
		self.checkBox_24.setToolTip("Las personas con discapacidad visceral son aquellos individuos que, debido a alguna deficiencia \n"
									"en la función de órganos internos, por ejemplo, el cardíaco o el diabético, se encuentran impedidas de \n"
									"desarrollar su vida con total plenitud (aunque no tengan complicaciones en el campo intelectual, \n"
									"en sus funciones sensoriales o motoras)")
		self.checkBox_24.setStyleSheet("QCheckBox{ background-color:#E5E7EE ;\n"
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

		self.radioButton_si_medicamentos = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_si_medicamentos.setGeometry(QRect(270, 160, 45, 17))
		self.radioButton_si_medicamentos.setObjectName("radioButton_si_medicamentos")
		self.radioButton_si_medicamentos.setText("Si")
		self.radioButton_si_medicamentos.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.radioButton_no_medicamentos = QRadioButton(self.groupBox_datosdiscapacidad)
		self.radioButton_no_medicamentos.setGeometry(QRect(330, 160, 45, 17))
		self.radioButton_no_medicamentos.setObjectName("radioButton_no_medicamentos")
		self.radioButton_no_medicamentos.setText("No")
		self.radioButton_no_medicamentos.setStyleSheet("QRadioButton{ background-color:#E5E7EE ;\n"
		"color: #000000;}")

		self.textEdit_medicamento = QTextEdit(self.groupBox_datosdiscapacidad)
		self.textEdit_medicamento.setGeometry(QRect(250, 180, 141, 61))
		self.textEdit_medicamento.setStyleSheet("QTextEdit{\n"
		"border: 0px\n"
		"}\n"
		"")
		self.textEdit_medicamento.setObjectName("textEdit_medicamento")
		self.textEdit_medicamento.setPlaceholderText("Escriba el medicamento...")

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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_discapacidad()
	interface.show()
	app.exec_()
