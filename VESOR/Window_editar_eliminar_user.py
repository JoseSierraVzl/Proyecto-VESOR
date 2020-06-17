import sqlite3

from os import getcwd, makedirs
from Source_rc import *

import sys, os
from random import randint
from PyQt5 import  uic, QtWidgets, QtGui
from PyQt5.QtSql import *

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


class Window_edit_elim_user(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setWindowTitle("Editar usuario")
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

		self.setFixedSize(755, 460)  
		self.setStyleSheet("QDialog{\n"
		"background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}\n"
		"")
		# estilos
		botonStilo = ("QPushButton{\n"
		"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px\n"
		"}\n"
		"\n"
		"QPushButton:hover{\n"
		"background-color:rgb(0, 170, 255);\n"
		"color:rgb(255, 255, 255);\n"
		"font-size: 12px;\n"
		"\n"
		"}")


		self.frame = QFrame(self)
		self.frame.setGeometry(QtCore.QRect(30, 20, 121, 420))
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)
		self.frame.setStyleSheet("QFrame{\n"
        "\n"
        "background-color:#12191D;\n"
        "border-radius: 45px\n"
        "}")


		self.label = QLabel(self)
		self.label.setGeometry(QtCore.QRect(355, 30, 251, 21))
		self.label.setText("Seleccione el usuario a editar")
		font = QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setStyleSheet("color: black;")

		self.label_2 = QLabel(self)
		self.label_2.setGeometry(QtCore.QRect(57, 50, 131, 31))
		self.label_2.setText("VESOR")
		self.label_2.setStyleSheet("QLabel{\n"
		"color:rgb(255, 255, 255);\n"
		"font: 14pt \"Comic Sans MS\";\n"
		"border-radius: 6px;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
		"\n"
		"}")

		self.groupBox = QGroupBox(self)
		self.groupBox.setGeometry(QtCore.QRect(180, 60, 545, 373))
		self.groupBox.setStyleSheet("QGroupBox{\n"
		"color:#1b231f;\n"
		"background-color: #E5E7EE;\n"
		"font: 75 10pt Comic Sans MS;\n"
		"border-radius: 22px;\n"
		"\n"
		"}")

		self.btnEditar = QPushButton(self.frame)
		self.btnEditar.setText("Editar Usuario")
		self.btnEditar.setGeometry(QtCore.QRect(-10, 90, 131, 31))
		self.btnEditar.setStyleSheet(botonStilo)

		self.btnMostrar = QPushButton(self.frame)
		self.btnMostrar.setText("Mostrar/Ocultar")
		self.btnMostrar.setGeometry(QtCore.QRect(-10, 125, 131, 31))
		self.btnMostrar.setStyleSheet(botonStilo)

		self.btnCancelar = QPushButton(self.frame)
		self.btnCancelar.setText("Cancelar")
		self.btnCancelar.setGeometry(QtCore.QRect(-10, 160, 131, 31))
		self.btnCancelar.setStyleSheet(botonStilo)


		self.tableWidget = QTableWidget(self.groupBox)
		self.tableWidget.setGeometry(QtCore.QRect(20,20, 500, 340))
		self.tableWidget.setStyleSheet("QFrame{\n"
        "\n"
        "background-color:#5555FF;\n"
        "border-radius: 20px\n"
        "}")

		self.tableWidget.setColumnCount(6)

		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)

		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText("#")
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText("Nombre")
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText("Apellido")
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText("Cédula")
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText("Nro. Casa")
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText("Vocer@")


		self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget.setDragDropOverwriteMode(False)
		self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tableWidget.setTextElideMode(Qt.ElideRight)
		self.tableWidget.setWordWrap(False)
		self.tableWidget.setSortingEnabled(False)
		self.tableWidget.setRowCount(0)
		self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
		self.tableWidget.horizontalHeader().setHighlightSections(False)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.verticalHeader().setVisible(False)
		self.tableWidget.setAlternatingRowColors(True)

		self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        # Menú contextual
		self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

		# Lógica
		self.btnMostrar.clicked.connect(self.datosTabla)
		self.btnCancelar.clicked.connect(self.Salir)

	def datosTabla(self):
		try:
			self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
			self.con2 = sqlite3.connect("Base de datos/DB_VESOR_USER_UBICACIONGEOGRAFICA.db")

		except Exception as e:
			print(e)
			QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
										 QMessageBox.Ok)
			self.cursor = self.con.cursor()
			self.cursor2 = self.con2.cursor()
			self.cursor.execute("SELECT ID,PRIMER_NOMBRE, PRIMER_APELLIDO, CEDULA FROM 'USUARIO_DT_GNR' WHERE ID = 1")
			self.cursor2.execute("SELECT Nº_VIVIENDA FROM 'USUARIO_UBCGEOG' WHERE ID = 1" )

			for i in self.cursor:
				self.id = str(i[0])
				self.primer_nombre = str(i[1])
				self.primer_apellido = str(i[2])
				self.cedula = str(i[3])
				
			for i in self.cursor2:
				self.vivienda = str(i[0]) 

			datos = [(self.id ,self.primer_nombre, self.primer_apellido, self.cedula, self.vivienda)]
			
			self.tableWidget.clearContents()

			row = 0
			for endian in datos:
				self.tableWidget.setRowCount(row + 1)
		            
				idDato = QTableWidgetItem(endian[0])
				idDato.setTextAlignment(4)
		            
				self.tableWidget.setItem(row, 0, idDato)
				self.tableWidget.setItem(row, 1, QTableWidgetItem(endian[1]))
				self.tableWidget.setItem(row, 2, QTableWidgetItem(endian[2]))
				self.tableWidget.setItem(row, 3, QTableWidgetItem(endian[3]))
				self.tableWidget.setItem(row, 4, QTableWidgetItem(endian[4]))
				self.tableWidget.setItem(row, 5, QTableWidgetItem(endian[5]))

			row += 1



	def Salir(self):
		
		msg = QMessageBox()
		msg.setWindowIcon(QIcon('Imagenes-iconos/Icono_window.png'))
		msg.setText("Cancelar")
		msg.setInformativeText("¿Estás seguro de que desea cancelar?")
		msg.setWindowTitle("¡Advertencia!")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msg.setIcon(QMessageBox.Warning)
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
	interface = Window_edit_elim_user()
	interface.show()
	app.exec_()


