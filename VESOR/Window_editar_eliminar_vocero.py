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




class Window_edit_elim_vocero(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Editar vocero")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(783, 460)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")

		self.initUi()

	def initUi(self):
		#Stylos ==========================================================================================      		

		#Style del frame principal
		Style_frame_principal = ("QFrame#frame{\n"
								"color:#1b231f;\n"
								"background-color: #E5E7EE;\n"
								"font: 75 10pt Comic Sans MS;\n"
								"border-radius: 22px;\n"
								"}")
		###

		#Style de la QTable con el contenido

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

		#Style de frame menu

		Style_frame_menu = ("QFrame{\n"
							
							"background-color:#12191D;\n"
							"border-radius: 45px\n"
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
						"font-size: 12px;\n"
						"}")
		###

		#Style actualizar 

		Style_actulizar_button =	("QPushButton{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
									"border-radIus: 3px\n"
									"}\n"
									"QPushButton:hover{\n"
									"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 204, 204, 129));\n"
									"border-radius:10px;\n"
									"}")
		###

		#Style de label titulo

		Style_label_menu = ("QLabel{\n"
							"color:rgb(255, 255, 255);\n"
							"font: 10pt 'Comic Sans MS';\n"
							"border-radius: 6px;\n"
							"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"

							"}")

		###

		#Style de label busqueda
		Style_label_busqueda = ("QLabel{\n"
								"color:rgb(255, 255, 255);\n"
								"font: 8pt 'Comic Sans MS';\n"
								"background-color:#1C262D\n"
								"}")

		###

		#Style line Edit busqueda
		Style_line_edit_busqueda = ("QLineEdit{\n"
									"border-radius: 6px;\n"
									"}\n"
									"QLineEdit:hover{\n"
									"border:1px solid rgb(0, 170, 255);\n"
									"}")
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#frames ==========================================================================================      				
		#Frame principal contenido
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(180,20,581,411))
		self.frame_principal_contenido.setObjectName("frame")
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)
		###

		#Frame menu
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(30,20,121,411))
		self.frame_menu.setStyleSheet(Style_frame_menu)
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Labels ==========================================================================================
		#Labels de menu
		self.Label_1 = QLabel(self.frame_menu)
		self.Label_1.setGeometry(QRect(0,10,121,21))
		self.Label_1.setText("ELIMINAR")
		self.Label_1.setAlignment(Qt.AlignCenter)
		self.Label_1.setStyleSheet(Style_label_menu)

		self.Label_2 = QLabel(self.frame_menu)
		self.Label_2.setGeometry(QRect(0,30,121,21))
		self.Label_2.setText("Y EDITAR")
		self.Label_2.setAlignment(Qt.AlignCenter)
		self.Label_2.setStyleSheet(Style_label_menu)

		self.Label_3 = QLabel(self.frame_menu)
		self.Label_3.setGeometry(QRect(0,50,121,21))
		self.Label_3.setText("VOCERO")
		self.Label_3.setAlignment(Qt.AlignCenter)
		self.Label_3.setStyleSheet(Style_label_menu)

		self.Label_4 = QLabel(self.frame_menu)
		self.Label_4.setGeometry(QRect(0,310,121,21))
		self.Label_4.setText("BÚSQUEDA")
		self.Label_4.setAlignment(Qt.AlignCenter)
		self.Label_4.setStyleSheet(Style_label_busqueda)	
		###
		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line Edit ==========================================================================================
		self.line_edit_busqueda = QLineEdit(self.frame_menu)
		self.line_edit_busqueda.setGeometry(QRect(5,340,111,21))
		self.line_edit_busqueda.setToolTip("Ingresa la cedula de identidad\npara busqueda de vocero")
		self.line_edit_busqueda.setPlaceholderText("Ingresa cedula")
		self.line_edit_busqueda.setStyleSheet(Style_line_edit_busqueda)

		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Buttons ==========================================================================================
		#Buttons actualizar       		
		self.actualizar = QPushButton(self.frame_menu)
		self.actualizar.setText("")
		self.actualizar.setGeometry(QRect(50, 120, 23, 21))
		self.actualizar.setStyleSheet(Style_actulizar_button)
		self.actualizar.setIcon(QIcon(":/Icono_recargar/Imagenes-iconos/Recargar.png"))
		self.actualizar.setToolTip("Click para actualizar\nla lista de voceros")
		###

		#Buttons aceptar
		self.aceptar = QPushButton(self.frame_menu)
		self.aceptar.setText("Aceptar")
		self.aceptar.setGeometry(QRect(0, 150, 121, 31))
		self.aceptar.setStyleSheet(Style_buttons)
		self.aceptar.setIcon(QIcon(":/Icono_aceptar/Imagenes-iconos/Check_blanco.png"))
		self.aceptar.setIconSize(QSize(15,15))
		###

		#Buttons eliminar
		self.eliminar = QPushButton(self.frame_menu)
		self.eliminar.setText("Eliminar")
		self.eliminar.setGeometry(QRect(0, 180, 121, 31))
		self.eliminar.setStyleSheet(Style_buttons)
		self.eliminar.setIcon(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"))
		self.eliminar.setIconSize(QSize(17,17))
		###

		#Buttons cancelar
		self.cancelar = QPushButton(self.frame_menu)
		self.cancelar.setText("Cancelar")
		self.cancelar.setGeometry(QRect(0, 210, 121, 31))
		self.cancelar.setStyleSheet(Style_buttons)
		self.cancelar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.cancelar.setIconSize(QSize(15,15))
		###


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#EVENTOS ==========================================================================================      		
		self.actualizar.clicked.connect(self.mostrar_datos)

		#QTableWidget ==========================================================================================      		
		nombreColumnas = ("ID", "Primer nombre", "Primer apellido", "Cedula", "Usuarios que maneja")
		self.QTableWidget_contenido = QTableWidget(self.frame_principal_contenido)
		#self.QTableWidget_contenido.setToolTip("Click para ver usuario")
		self.QTableWidget_contenido.setGeometry(QRect(15,11,551,391))
		self.QTableWidget_contenido.setStyleSheet(Style_qtable_contenido)
		self.QTableWidget_contenido.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.QTableWidget_contenido.setDragDropOverwriteMode(False)
		self.QTableWidget_contenido.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.QTableWidget_contenido.setSelectionMode(QAbstractItemView.SingleSelection)
		self.QTableWidget_contenido.setTextElideMode(Qt.ElideRight)
		self.QTableWidget_contenido.setWordWrap(False)
		self.QTableWidget_contenido.setSortingEnabled(False)
		self.QTableWidget_contenido.setColumnCount(5)
		self.QTableWidget_contenido.setRowCount(0)
		self.QTableWidget_contenido.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.QTableWidget_contenido.horizontalHeader().setHighlightSections(False)
		self.QTableWidget_contenido.horizontalHeader().setStretchLastSection(True)
		self.QTableWidget_contenido.verticalHeader().setVisible(False)
		self.QTableWidget_contenido.setAlternatingRowColors(False)
		self.QTableWidget_contenido.verticalHeader().setDefaultSectionSize(20)
		self.QTableWidget_contenido.setHorizontalHeaderLabels(nombreColumnas)
		
		for indice, ancho in enumerate((5, 170,170, 130,170), start=0):
			self.QTableWidget_contenido.setColumnWidth(indice, ancho)


	def mostrar_datos(self):

		if QFile.exists("Voceros/DB_VOCEROS.db"):

			try: 
				self.con = sqlite3.connect("Voceros/DB_VOCEROS.db")

				self.cursor = self.con.cursor()

				self.cursor.execute("SELECT ID, PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA FROM DATOS_VOCEROS")

				datos_Devueltos = self.cursor.fetchall()
				self.QTableWidget_contenido.clearContents()
				self.QTableWidget_contenido.setRowCount(0)

				if datos_Devueltos:
					row = 0

					for datos in datos_Devueltos:
						self.QTableWidget_contenido.setRowCount(row + 1)
						
						idDato = QTableWidgetItem(str(datos[0]))
						idDato.setTextAlignment(Qt.AlignCenter)

						self.QTableWidget_contenido.setItem(row, 0, idDato)
						self.QTableWidget_contenido.setItem(row, 1, QTableWidgetItem(datos[1]))
						self.QTableWidget_contenido.setItem(row, 2, QTableWidgetItem(datos[2]))
						self.QTableWidget_contenido.setItem(row, 3, QTableWidgetItem(datos[3]))
						row +=1


				else:   
					QMessageBox.information(self, "Buscar Vocero", "No se encontraron voceros"
											"información.   ", QMessageBox.Ok)

			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar Voceros", "No se encontro la base de datos.   ",
								 QMessageBox.Ok)


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_edit_elim_vocero()
	interface.show()
	app.exec_()


