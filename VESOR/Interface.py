#======================================================================================================
import sqlite3
from os import getcwd, makedirs
from Source_rc import *

#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import*



from Window_visor_de_imagenes import *

from Window_reparacion import *

from Window_enfermedad import * 

from Window_discapacidad import *

from Window_nv_user import *

from Window_acerda_de_vesor import *

from Window_gas_bombona import *

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
		#abrir.setShortcutVisibleInContextMenu(True)
		
		self.ayuda = self.menuArchivo.addAction("Ayuda")
		#guardar.setShortcutVisibleInContextMenu(True)
		
		#self.menuArchivo.addSeparator()
		
		#self.salir = self.menuArchivo.addAction("Salir")


#========================================= #Eventos# ==================================================================
		self.Button_menu.setMenu(self.menuArchivo)
		
		self.buttonNewUser.clicked.connect(self.Nuevo_user)

		self.buttonEditUser.clicked.connect(self.Editar_usuario)

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

		


#========================================== #Classes# ===================================================================


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()