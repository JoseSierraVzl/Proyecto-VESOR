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




class Window_edit_elim_user(QDialog):
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

		#Style del menu del button buscar

		Style_button_menu =("QMenu{background-color:#12191D;\n"
		"color: #ffffff;}\n"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}") 


		#"QMenu:separator{height:0px;"
		#"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		#"stop:0 rgba(173, 181, 189, 95));"
		#"margin-left:0px;"
		#"margin-right:0px;}"

		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		#frames ==========================================================================================      				


		self.menu_buscar = QMenu()
		self.menu_buscar.setStyleSheet(Style_button_menu)
		self.buscar_estudiante = self.menu_buscar.addAction("Buscar estudiante")
		self.buscar_discapacidad = self.menu_buscar.addAction("Buscar discapacitados")
		self.buscar_enfermedad = self.menu_buscar.addAction("Buscar enfermos")
		self.buscar_pensionados = self.menu_buscar.addAction("Buscar pensionados")
		self.buscar_embarazadas = self.menu_buscar.addAction("Buscar embarazadas")
		self.buscar_lactantes = self.menu_buscar.addAction("Buscar lactantes")
		self.buscar_rep = self.menu_buscar.addAction("Buscar inscritos en el REP")
		#
		self.buscar_parentesco = self.menu_buscar.addMenu("Buscar por parentesco")
		self.buscar_parentesco.addAction("Jefe/a de familia")
		#
		self.buscar_genero = self.menu_buscar.addMenu("Buscar por genero")
		self.buscar_genero.addAction("Masculino")
		self.buscar_genero.addAction("Femenino")














		#frames ==========================================================================================      				
		#Frame principal contenido
		self.frame_principal_contenido = QFrame(self)
		self.frame_principal_contenido.setGeometry(QRect(180,20,581,411))
		self.frame_principal_contenido.setObjectName("frame")
		self.frame_principal_contenido.setStyleSheet(Style_frame_principal)
		###

		#Frame menus
		self.frame_menu = QFrame(self)
		self.frame_menu.setGeometry(QRect(30,20,121,411))
		self.frame_menu.setStyleSheet(Style_frame_menu)
		###
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
		
		#Labels ==========================================================================================
		#Labels de menu
		self.Label = QLabel(self.frame_menu)
		self.Label.setGeometry(QRect(30,30,121,51))
		self.Label.setText("ELIMINAR \nY EDITAR \nUSUARIO")
		self.Label.setStyleSheet(Style_label_menu)

		self.Label_4 = QLabel(self.frame_menu)
		self.Label_4.setGeometry(QRect(0,300,121,21))
		self.Label_4.setText("BÚSQUEDA")
		self.Label_4.setAlignment(Qt.AlignCenter)
		self.Label_4.setStyleSheet(Style_label_busqueda)	
		###
		
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Line Edit busqueda nombre ==========================================================================================
		self.line_edit_busqueda = QLineEdit(self.frame_menu)
		self.line_edit_busqueda.setObjectName("Enter")
		self.line_edit_busqueda.setGeometry(QRect(5,330,111,21))
		self.line_edit_busqueda.setToolTip("Ingresa el dato del usuario\npara la busqueda")
		self.line_edit_busqueda.setPlaceholderText("Ingresa dato")
		self.line_edit_busqueda.setStyleSheet(Style_line_edit_busqueda)
		#self.line_edit_busqueda.setMove(1000,330)


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#Buttons ==========================================================================================
		#Buttons actualizar       		
		self.actualizar = QPushButton(self.frame_menu)
		self.actualizar.setText("")
		self.actualizar.setGeometry(QRect(50, 120, 23, 21))
		self.actualizar.setStyleSheet(Style_actulizar_button)
		self.actualizar.setIcon(QIcon(":/Icono_recargar/Imagenes-iconos/Recargar.png"))
		self.actualizar.setToolTip("Click para actualizar\nla lista de usuarios")
		###

		# Buttons Buscar
		self.buscar = QPushButton(self.frame_menu)
		self.buscar.setObjectName("Buscar")
		self.buscar.setText("Buscar")
		self.buscar.setGeometry(QRect(-3,355,130,21))
		self.buscar.setStyleSheet(Style_buttons)
		self.buscar.setToolTip("Click para motrar opciones de busqueda")

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
		
		#Buttons opciones para buscar 
		self.opciones_de_busqueda = QPushButton(self.frame_menu)
		self.opciones_de_busqueda.setText("Opciones")
		self.opciones_de_busqueda.setGeometry(QRect(-12, 210, 151, 31))
		self.opciones_de_busqueda.setStyleSheet(Style_buttons)
		self.opciones_de_busqueda.setIcon(QIcon(":/Icono_lupa/Imagenes-iconos/Lupa_blanca.png"))
		self.opciones_de_busqueda.setIconSize(QSize(16,16))
		###

		#Buttons cancelar
		self.cancelar = QPushButton(self.frame_menu)
		self.cancelar.setText("Cancelar")
		self.cancelar.setGeometry(QRect(0, 240, 121, 31))
		self.cancelar.setStyleSheet(Style_buttons)
		self.cancelar.setIcon(QIcon(":/Icono_cancelar/Imagenes-iconos/Cancelar_blanco.png"))
		self.cancelar.setIconSize(QSize(15,15))
		###


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		#QTableWidget ==========================================================================================      		
		nombreColumnas = ("ID", "Primer nombre", "Primer apellido", "Cedula",
		 "N°Vivienda", "Vocera/o")
		self.QTableWidget_contenido = QTableWidget(self.frame_principal_contenido)
		self.QTableWidget_contenido.setToolTip("Click para ver usuario")
		self.QTableWidget_contenido.setGeometry(QRect(15,11,551,391))
		self.QTableWidget_contenido.setStyleSheet(Style_qtable_contenido)
		self.QTableWidget_contenido.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.QTableWidget_contenido.setDragDropOverwriteMode(False)
		self.QTableWidget_contenido.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.QTableWidget_contenido.setSelectionMode(QAbstractItemView.SingleSelection)
		self.QTableWidget_contenido.setTextElideMode(Qt.ElideRight)
		self.QTableWidget_contenido.setWordWrap(False)
		self.QTableWidget_contenido.setSortingEnabled(False)
		self.QTableWidget_contenido.setColumnCount(6)
		self.QTableWidget_contenido.setRowCount(0)
		self.QTableWidget_contenido.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.QTableWidget_contenido.horizontalHeader().setHighlightSections(False)
		self.QTableWidget_contenido.horizontalHeader().setStretchLastSection(True)
		self.QTableWidget_contenido.verticalHeader().setVisible(False)
		self.QTableWidget_contenido.setAlternatingRowColors(False)
		self.QTableWidget_contenido.verticalHeader().setDefaultSectionSize(20)
		self.QTableWidget_contenido.setHorizontalHeaderLabels(nombreColumnas)

		for indice, ancho in enumerate((5, 150, 150, 150, 80, 150), start=0):
			self.QTableWidget_contenido.setColumnWidth(indice, ancho)


		#EVENTOS ==========================================================================================      		
		
		#self.limpiar.clicked.connect(self.Ocultar_todos)

		self.actualizar.clicked.connect(self.mostrar_datos)

		self.eliminar.clicked.connect(self.eliminar_datos)

		self.line_edit_busqueda.returnPressed.connect(self.buscar_datos)
		self.buscar.clicked.connect(self.buscar_datos)
		self.opciones_de_busqueda.setMenu(self.menu_buscar)


		self.aceptar.clicked.connect(self.Item_click)
		self.QTableWidget_contenido.itemDoubleClicked.connect(self.Item_click)


		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
	def mostrar_datos(self):

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				self.con2 = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")
				self.cursor = self.con.cursor()
				self.cursor2 = self.con2.cursor()

				self.cursor.execute("SELECT ID, PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA FROM USUARIO_DT_GNR")
				self.cursor2.execute("SELECT N_VIVIENDA FROM USUARIO_UBCGEOG")

				datos_Devueltos = self.cursor.fetchall()
				datos_Devueltos_2 = self.cursor2.fetchall()
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
						#self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos[4]))
						row +=1
						
				if datos_Devueltos_2:
					row = 0
					for  datos_2 in datos_Devueltos_2:
						
						self.QTableWidget_contenido.setItem(row, 4, QTableWidgetItem(datos_2[0]))
						row += 1





				else:   
					QMessageBox.information(self, "Buscar usuaria", "No se encontraron usuarios"
											"información.   ", QMessageBox.Ok)

			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
											 QMessageBox.Ok)
		else:
			QMessageBox.critical(self, "Buscar usuarios", "No se encontro la base de datos.   ",
								 QMessageBox.Ok)




	def Item_click(self,celda):
		celda = self.QTableWidget_contenido.selectedItems()

		if celda:
			indice = celda[0].row()
			dato = [self.QTableWidget_contenido.item(indice,i).text()for i in range(4)]

			dato_buscar = dato[3]

			if dato_buscar:
				sql = "SELECT * FROM USUARIO_DT_GNR WHERE CEDULA LIKE ?", (dato_buscar,)
				print("Si")
			else:
				print("NO")

			if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):
				conexion = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				cursor = conexion.cursor()

				try:
					cursor.execute(sql[0],sql[1])
					datosdevueltos = cursor.fetchall()
					print(datosdevueltos)
					for dato in datosdevueltos:
						indice = dato[0]

					Window_visualizar_users(dato,self).exec_()
					conexion.close()
				except Exception as e:
					print("A1:",e)
		else:
			print("Error")




	def eliminar_datos(self):

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

			msg = QMessageBox()
			msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
			msg.setText("¿Está seguro de querer eliminar este usuario?")
			msg.setIcon(QMessageBox.Question)
			msg.setWindowTitle("Eliminar Usuario")
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

				try:

					self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
					self.con2 = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")
					self.con3 = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOS_VV.db")
					self.con4 = sqlite3.connect("Base de datos/DB_VESOR_USER_PROT_SOCIAL.db")

					self.cursor = self.con.cursor()
					self.cursor2 = self.con2.cursor()
					self.cursor3 = self.con3.cursor()
					self.cursor4 = self.con4.cursor()


					self.QTableWidget_contenido.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
					ID = self.QTableWidget_contenido.selectedIndexes()[0].data()
					print(f"has clickeado en {ID}")
					
					# Primera Instancia
					query = 'DELETE  FROM USUARIO_DT_GNR WHERE ID =?'
					self.cursor.execute(query, (ID,))
					self.con.commit()

					# Segunda Instancia
					query_2 = 'DELETE FROM USUARIO_UBCGEOG WHERE ID =?'
					self.cursor2.execute(query_2, (ID,))
					self.con2.commit()

					# Tercera Instancia
					query_3 = 'DELETE FROM USUARIO_DT_VV WHERE ID =?'
					self.cursor3.execute(query_3, (ID,))
					self.con3.commit()

					# Cuarta Instancia
					query_4 = 'DELETE FROM USUARIO_PROT_SOCIAL WHERE ID =?'
					self.cursor4.execute(query_4, (ID,))
					self.con4.commit()

					# Seleccionar fila
					self.Seleccion = self.QTableWidget_contenido.selectedItems()
					# Borrar seleccionado
					self.QTableWidget_contenido.removeRow(self.QTableWidget_contenido.currentRow())

				except Exception as e:
					print(e)
					QMessageBox.critical(self, "Error", "No existen usuarios para eliminar",
											 QMessageBox.Ok)

			else:
				pass	

		else:
			QMessageBox.critical(self, "Eliminar", "No se encontró la base de datos.   ",
									 		QMessageBox.Ok)





	def buscar_datos(self):

		try:
			widget = self.sender().objectName()

			if widget in ("Enter", "Buscar"):
				cliente = " ".join(self.line_edit_busqueda.text().split()).lower()

				if len(cliente)== 0:
					QMessageBox.critical(self, "Error", "No se ha escrito nada",
												 QMessageBox.Ok)
				if cliente:
					sql = "SELECT ID, PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA FROM USUARIO_DT_GNR WHERE PRIMER_NOMBRE LIKE ?", ("%"+cliente+"%",)
				else:
					self.line_edit_busqueda.setFocus()
					return
			else:
				self.line_edit_busqueda.clear()
				sql = "SELECT * FROM USUARIO_DT_GNR "

			if QFile.exists('Base de datos/DB_VESOR_USER_DATOSGENERALES.db'):
				conexion = sqlite3.connect('Base de datos/DB_VESOR_USER_DATOSGENERALES.db')
				cursor = conexion.cursor()
				print("Si")
	                
				try:
					if widget in ("Enter", "Buscar"):
						cursor.execute(sql[0], sql[1])
						
					else:
						cursor.execute(sql)
	                    
					datosDevueltos = cursor.fetchall()
					conexion.close()

					self.QTableWidget_contenido.clearContents()
					self.QTableWidget_contenido.setRowCount(0)

					if datosDevueltos:
						fila = 0
						for datos in datosDevueltos:
							self.QTableWidget_contenido.setRowCount(fila + 1)
	            
							idDato = QTableWidgetItem(str(datos[0]))
							idDato.setTextAlignment(Qt.AlignCenter)
	                        
							self.QTableWidget_contenido.setItem(fila, 0, idDato)
							self.QTableWidget_contenido.setItem(fila, 1, QTableWidgetItem(datos[1]))
							self.QTableWidget_contenido.setItem(fila, 2, QTableWidgetItem(datos[2]))
							self.QTableWidget_contenido.setItem(fila, 3, QTableWidgetItem(datos[3]))

							fila += 1
							ide_importante = datos[0]

							# Segunda conexion y numero de vivienda
							try:
								conexion2 = sqlite3.connect('Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db')
								cursor2 = conexion2.cursor()

								sql2 = "SELECT N_VIVIENDA FROM USUARIO_UBCGEOG WHERE ID LIKE ?"

								cursor2.execute(sql2, (ide_importante,))
								datos_Devueltos_2 = cursor2.fetchall()
								conexion2.close()

								fila = 0
								for  datos_2 in datos_Devueltos_2:
		            
									idDato = QTableWidgetItem(str(datos_2[0]))
									idDato.setTextAlignment(Qt.AlignCenter)

									self.QTableWidget_contenido.setItem(fila, 4, QTableWidgetItem(datos_2[0]))
									fila += 1

							except Exception as e:
								print(e)
								QMessageBox.information(self, "Buscar cliente", "No se pudo encontrar la base de datos geográfica",
																QMessageBox.Ok)

					else:   
						QMessageBox.information(self, "Buscar cliente", "No se encontro "
	                                            "información.   ", QMessageBox.Ok)
				except Exception as e:
					print(e)
					conexion.close()
					QMessageBox.critical(self, "Buscar clientes", "Error desconocido.   ",
	                                     QMessageBox.Ok)
			else:
				QMessageBox.critical(self, "Buscar clientes", "No se encontro la base de datos.   ",
	                                 QMessageBox.Ok)

			self.line_edit_busqueda.setFocus()
		except AttributeError:
			pass


	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			self.buscar_datos()

		elif event.key() == Qt.Key_Escape:

			cerrar = QMessageBox(self)
			cerrar.setWindowTitle("¿Salir de VESOR?")
			cerrar.setIcon(QMessageBox.Question)
			cerrar.setText("¿Estás seguro que desea cerrar esta ventana?   ")
			botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
			botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
	            
			cerrar.exec_()
	            
			if cerrar.clickedButton() == botonSalir:
				self.destroy()
			else:
				event.ignore()

	def closeEvent(self, event):
               
			cerrar = QMessageBox(self)
			cerrar.setWindowTitle("¿Salir de VESOR?")
			cerrar.setIcon(QMessageBox.Question)
			cerrar.setText("¿Estás seguro que desea cerrar esta ventana?   ")
			botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
			botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
            
			cerrar.exec_()





			
			
		#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_edit_elim_user()
	interface.show()
	app.exec_()


