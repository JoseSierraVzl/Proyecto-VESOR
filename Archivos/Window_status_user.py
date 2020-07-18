import sqlite3
from os import getcwd, makedirs
from Source_rc import *

import sys, os
from random import randint
from PyQt5 import  uic, QtWidgets

from Window_visualizar_user import *

from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QByteArray,QIODevice,QBuffer,QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,)



class Window_status_user(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Editar usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setFixedSize(783, 460)
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		

		self.initUi()

	def initUi(self):
		#Estilos ==========================================================================================      		

		#Style del frame principal
		Style_frame_principal = ("QFrame#frame{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		###

		Style_label_menu = ("QLabel{\n"
							"color:rgb(255, 255, 255);\n"
							"font: 10pt 'Comic Sans MS';\n"
							"border-radius: 6px;\n"
							"text-align: center;"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
							"}")

		###
		#Style de frame menu

		Style_frame_menu = ("QFrame{\n"
							"background-color:#12191D;\n"
							"border-radius: 45px\n"
							"}")
		###
		#Style actualizar 

		Style_actualizar_button =("QPushButton{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
									"border-radIus: 3px\n"
									"}\n"
									"QPushButton:hover{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 204, 204, 129));\n"
									"border-radius:10px;\n"
									"}")
		###
		Style_qtable_contenido = ("QTableWidget::item{\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget::item:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget{\n"
									"background-color:#ced4da;\n"
									"border:5px solid #000000;\n"
									"border-radius:10px;\n"
									"color:#000000;\n"
									"}\n"
									"QHeaderView::section{\n"
									"background-color:#12191D;\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000;\n"
									"}\n"
									"QHeaderView::section:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000\n"									
									"}\n"
									"QHeaderView::section:checked{\n"
									"background-color: rgb(0, 170, 255);\n"
									"}")
		###

		#Style buttons
		Style_buttons = ("QPushButton{\n"
						"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
						"color:rgb(255, 255, 255);\n"
						"font-size: 12px\n"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:rgb(0, 170, 255);\n"
						"color:rgb(255, 255, 255);\n"
						"}")
		###

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		#Frame principal contenido
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(180,20,581,411))
		self.frame_principal_contenido.setObjectName("frame")
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)
		self.frame_principal_contenido.setGraphicsEffect(self.shadow)
		###

		#Frame menu
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(30,20,121,411))
		self.frame_menu.setStyleSheet(Style_frame_menu)
		self.frame_menu.setGraphicsEffect(self.shadow)
		###

		#Label de Título
		self.Label_titulo = QLabel(self)
		self.Label_titulo.setText("STATUS \nDE \nUSUARIO")
		self.Label_titulo.setGeometry(QRect(60,20,60,100))
		self.Label_titulo.setStyleSheet(Style_label_menu)
		self.Label_titulo.setAlignment(QtCore.Qt.AlignCenter)  

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		# Botones
		#Buttons actualizar       		
		self.actualizar = QPushButton(self.frame_menu)
		self.actualizar.setGeometry(QRect(50, 120, 23, 21))
		self.actualizar.setStyleSheet(Style_actualizar_button)
		self.actualizar.setIcon(QIcon(":/Icono_recargar/Imagenes-iconos/Recargar.png"))
		self.actualizar.setToolTip("Click para actualizar\nla lista de usuarios")
		###

		#Buttons aceptar
		self.aceptar = QPushButton(self.frame_menu)
		self.aceptar.setText("Aceptar")
		self.aceptar.setGeometry(QRect(0, 150, 121, 31))
		self.aceptar.setStyleSheet(Style_buttons)
		self.aceptar.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.aceptar.setIconSize(QSize(15,15))
		###

		#Buttons cancelar
		self.cancelar = QPushButton(self.frame_menu)
		self.cancelar.setText("Cancelar")
		self.cancelar.setGeometry(QRect(0, 190, 121, 31))
		self.cancelar.setStyleSheet(Style_buttons)
		self.cancelar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.cancelar.setIconSize(QSize(15,15))
		###

		#QTableWidget ==========================================================================================      		
		nombreColumnas = ("Usuario", "Cedula", "Fecha", "Hora",
		 "Modificación")
		self.Tabla_contenido = QTableWidget(self.frame_principal_contenido)
		self.Tabla_contenido.setToolTip("Click para ver usuario")
		self.Tabla_contenido.setGeometry(QRect(15,11,551,391))
		self.Tabla_contenido.setStyleSheet(Style_qtable_contenido)
		self.Tabla_contenido.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.Tabla_contenido.setDragDropOverwriteMode(False)
		self.Tabla_contenido.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.Tabla_contenido.setSelectionMode(QAbstractItemView.SingleSelection)
		self.Tabla_contenido.setTextElideMode(Qt.ElideRight)
		self.Tabla_contenido.setWordWrap(False)
		self.Tabla_contenido.setSortingEnabled(False)
		self.Tabla_contenido.setColumnCount(5)
		self.Tabla_contenido.setRowCount(0)
		self.Tabla_contenido.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.Tabla_contenido.horizontalHeader().setHighlightSections(False)
		self.Tabla_contenido.horizontalHeader().setStretchLastSection(True)
		self.Tabla_contenido.verticalHeader().setVisible(False)
		self.Tabla_contenido.setAlternatingRowColors(False)
		self.Tabla_contenido.verticalHeader().setDefaultSectionSize(20)
		self.Tabla_contenido.setHorizontalHeaderLabels(nombreColumnas)

		for indice, ancho in enumerate((110, 110, 110, 110, 130), start=0):
			self.Tabla_contenido.setColumnWidth(indice, ancho)


		#EVENTOS ==========================================================================================      		
		self.actualizar.clicked.connect(self.mostrar_datos)
	

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	def mostrar_datos(self):

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")

				self.cursor = self.con.cursor()

				self.cursor.execute("SELECT PRIMER_NOMBRE, CEDULA, FECHA, HORA, MODIFICACION FROM USUARIO_DT_GNR")


				datos_Devueltos = self.cursor.fetchall()
				self.Tabla_contenido.clearContents()
				self.Tabla_contenido.setRowCount(0)

				if datos_Devueltos:
					row = 0

					for datos in datos_Devueltos:
						self.Tabla_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.Tabla_contenido.setItem(row, 0, idDato)
						self.Tabla_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.Tabla_contenido.setItem(row, 2, QTableWidgetItem(datos[2]))
						self.Tabla_contenido.setItem(row, 3, QTableWidgetItem(datos[3]))
						self.Tabla_contenido.setItem(row, 4, QTableWidgetItem(datos[4]))
					
						row +=1
						
				# if datos_Devueltos_2:
				# 	row = 0
				# 	for  datos_2 in datos_Devueltos_2:
						
				# 		self.Tabla_contenido.setItem(row, 4, QTableWidgetItem(datos_2[0]))
				# 		row += 1

				else:   
					QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)

			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontro la base de datos.   ",
								 QMessageBox.Ok)







	def closeEvent(self, event):
		
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de VESOR?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar esta ventana?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
            
		cerrar.exec_()
            
		if cerrar.clickedButton() == botonSalir:
			event.accept()
		else:
			event.ignore()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_status_user()
	interface.show()
	app.exec_()
