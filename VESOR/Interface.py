#======================================================================================================
import sqlite3
from os import getcwd, makedirs
from Source_rc import *

#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import*



#from Window_visor_de_imagenes import *

#from Window_reparacion import *

#from Window_enfermedad import * 

#rom Window_discapacidad import *

from Window_nv_user import *

from Window_acerda_de_vesor import *

#rom Window_gas_bombona import *

from Window_vocero import*

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


#======================================================================================================


 
class Interface(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("Ventana_inicial_menus.ui", self)
		self.setWindowTitle("Menu principal")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)

		#Menu 1 =====================================================================================================	

		self.menuArchivo = QMenu()
		self.menuArchivo.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:1px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:5px;"
		"margin-right:5px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		
		self.acercade = self.menuArchivo.addAction("Acerca de VESOR", self.Abrir_window)
		
		self.ayuda = self.menuArchivo.addAction("Ayuda")
		#======================================================================================================

		#Menu de opcionesde usuario =====================================================================================================	

		self.menu_usuario = QMenu()
		self.menu_usuario.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_user = self.menu_usuario.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar usuario", self.Nuevo_user)
		self.Editar_usuario = self.menu_usuario.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Eliminar usuario", self.Editar_usuario)

		#Menu de opciones de vocero =====================================================================================================	

		self.menu_vocero = QMenu()
		self.menu_vocero.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar vocero", self.Nv_vocero)

		self.Editar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Elimina vocero")

#========================================= #Eventos# ==================================================================
		self.Button_menu.setMenu(self.menuArchivo)

		self.buttonNewUser.setMenu(self.menu_usuario)
		self.buttonNewUser.setToolTip("Click para ver opciones de usuario")

		self.buttonVoceroNew.setMenu(self.menu_vocero)
		self.buttonVoceroNew.setToolTip("Click para ver opciones de vocero")
		
		#self.buttonNewUser.clicked.connect(self.Nuevo_user)

		#self.buttonEditUser.clicked.connect(self.Editar_usuario)

		self.lineEditSearch.setToolTip("Ingresa la cedula de quien deseas buscar.")

#======================================== #Funciones# ==================================================================

	def Editar_usuario(self):
		self.interface = Window_edit_elim_user()
		self.interface.show()
		#Window_editar_user(self).exec_()
	
	def Nuevo_user(self):
		Window_nv_users(self).exec_()

	def Abrir_window(self):
		Acerca_de(self).exec_()

	def Nv_vocero(self):
		Window_vocero(self).exec_()

	def closeEvent(self, event):
		
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de VESOR?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar VESOR?   ")
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
#========================================== #Classes# ===================================================================


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()