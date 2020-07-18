from Source_rc import *
import webbrowser
import sys
#from PyQt5 import  uic 

from PyQt5.QtGui import (QIcon)
from PyQt5.QtCore import (Qt,QSize, QRect)
from PyQt5.QtWidgets import (QApplication,QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit,QCheckBox, QTextEdit,QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect,QTextBrowser)




class Acerca_de(QDialog):
	def __init__(self, parent = None):
		super(Acerca_de, self).__init__()


		self.setWindowTitle("Acerca de VESOR")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
		self.setObjectName("Dialog")
		self.resize(519,671)
		self.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591,\n" 
		"x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
		"}")

		self.initUi()


	def initUi(self):
#====== Frame principal de fondo ==========================================================================================
		self.frame_contenido = QFrame(self)
		self.frame_contenido.setGeometry(QRect(10,10,500,650))
		self.frame_contenido.setStyleSheet("QFrame{background-color:#E5E7EE;\n"
		"border-radius: 20px;\n"
		"}")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#====== Label con el nombre vesor ==========================================================================================

		self.label_imagen = QLabel(self)
		self.label_imagen.setGeometry(QRect(-20,-70,361,291))
		self.label_imagen.setStyleSheet("QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png);\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"}")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#====== texto de descripcion de vesor ==========================================================================================

		self.frame_texto = QFrame(self)
		self.frame_texto.setGeometry(QRect(320,20,181,111))
		self.frame_texto.setStyleSheet("QFrame{background-color: #12191D;\n"
		"border-radius: 20px;\n"
		"}")
		self.label_descripcion = QLabel(self)
		self.label_descripcion.setGeometry(QRect(305,-25,210,210))
		self.label_descripcion.setStyleSheet("QLabel{\n"
		"border-image: url(:/Icono_descipcion/Imagenes-iconos/descripcion.png);\n"
		"}")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#====== Iamgen central ==========================================================================================

		self.label_imagen_central = QLabel(self)
		self.label_imagen_central.setGeometry(QRect(20,140,481,341))
		self.label_imagen_central.setStyleSheet("QLabel{border-radius:25px;\n"
		"border-image: url(:/Acerca_de/Imagenes-iconos/Acerca de .png);\n"
		"}")
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#====== Parte de datos de diseñadores y desarrolladores ==========================================================================================

		self.frame_disenadores = QFrame(self)
		self.frame_disenadores.setGeometry(QRect(20,490,481,161))
		self.frame_disenadores.setStyleSheet("QFrame{border-radius: 20px;\n"
		"background-color:#12191D;\n"
		"}")

		self.label_texto = QLabel(self.frame_disenadores)
		self.label_texto.setGeometry(QRect(150,0,181,31))
		self.label_texto.setText("Desarrolladores y Diseñadores")
		self.label_texto.setStyleSheet("QLabel{color: #ffffff}")

		self.Button_facebook = QPushButton(self.frame_disenadores)
		self.Button_facebook.setGeometry(QRect(-3,20,148,32))
		self.Button_facebook.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}"	)
		self.Button_facebook.setText("Jose Alejandro")
		self.Button_facebook.setIcon(QIcon("Imagenes-iconos/Facebook.png"))
		self.Button_facebook.setIconSize(QSize(30,30))
		self.Button_facebook.setToolTip("Click para ir al perfil")


		self.Button_gmail = QPushButton(self.frame_disenadores)
		self.Button_gmail.setGeometry(QRect(0,50,300,32))
		self.Button_gmail.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"font:10pt Arial;"
		"}"	)
		self.Button_gmail.setText("sierramendezjosealejandro@gmail.com")
		self.Button_gmail.setIcon(QIcon("Imagenes-iconos/gmail.png"))
		self.Button_gmail.setIconSize(QSize(30,30))


		self.Button_github = QPushButton(self.frame_disenadores)
		self.Button_github.setGeometry(QRect(140,20,141,32))
		self.Button_github.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}"	)
		self.Button_github.setText("JoseSierraVzl")
		self.Button_github.setIcon(QIcon("Imagenes-iconos/Githup.png"))
		self.Button_github.setIconSize(QSize(30,30))
		self.Button_github.setToolTip("Click para ir al perfil")

		self.line = QFrame(self.frame_disenadores)
		self.line.setGeometry(QRect(15, 85, 270, 1))
		self.line.setStyleSheet("QFrame{background-color: #E5E7EE;}")


		self.Button_facebook_2 = QPushButton(self.frame_disenadores)
		self.Button_facebook_2.setGeometry(QRect(-5,90,141,32))
		self.Button_facebook_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}"	)
		self.Button_facebook_2.setText("Cristian Cala")
		self.Button_facebook_2.setIcon(QIcon("Imagenes-iconos/Facebook.png"))
		self.Button_facebook_2.setIconSize(QSize(30,30))
		self.Button_facebook_2.setToolTip("Click para ir al perfil")

		self.Button_gmail_2 = QPushButton(self.frame_disenadores)
		self.Button_gmail_2.setGeometry(QRect(-15,120,271,32))
		self.Button_gmail_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"font:10pt Arial;"
		"}")
		self.Button_gmail_2.setText("cristiancala@protonmail.com")
		self.Button_gmail_2.setIcon(QIcon("Imagenes-iconos/gmail.png"))
		self.Button_gmail_2.setIconSize(QSize(30,30))


		self.Button_github_2 = QPushButton(self.frame_disenadores)
		self.Button_github_2.setGeometry(QRect(135,90,141,32))
		self.Button_github_2.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt;\n"
		"}"	)

		self.Button_github_2.setText("CristianCala")
		self.Button_github_2.setIcon(QIcon("Imagenes-iconos/Githup.png"))
		self.Button_github_2.setIconSize(QSize(30,30))
		self.Button_github_2.setToolTip("Click para ir al perfil")

		self.texto_instagram = QTextBrowser(self.frame_disenadores)
		self.texto_instagram.setGeometry(QRect(355,20,211,101))
		self.texto_instagram.setText("   Síguenos\nen Instagram")
		self.texto_instagram.setStyleSheet("QTextBrowser{font: 11pt;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"	
		"color: #ffffff;\n"
		"}")

		self.Button_instagram = QPushButton(self.frame_disenadores)
		self.Button_instagram.setGeometry(QRect(330,65,140,32))
		self.Button_instagram.setStyleSheet("QPushButton{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"
		"border: 0px;\n"
		"color: #ffffff;\n"
		"}\n"
		"QPushButton:hover{\n"
		"font:11pt Arial;\n"
		"}"	)
		self.Button_instagram.setText("@_codeloid")
		self.Button_instagram.setIcon(QIcon("Imagenes-iconos/Instagram.png"))
		self.Button_instagram.setToolTip("Click para ir al perfil")

		self.texto_instagram_2 = QTextBrowser(self.frame_disenadores)
		self.texto_instagram_2.setGeometry(QRect(330,95,211,101))
		self.texto_instagram_2.setText("Para que estés al tanto\n"
										"  de nuestros trabajos")
		self.texto_instagram_2.setStyleSheet("QTextBrowser{font: 10pt;\n"
		"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(255, 255, 255, 0));\n"	
		"color: #ffffff;\n"
		"}")

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

#== Eventos para abrir enlaces ============================================================================================	

		self.Button_facebook.clicked.connect(self.enlace_facebook_1)

		self.Button_github.clicked.connect(self.enlance_github_1)

		self.Button_facebook_2.clicked.connect(self.enlace_facebook_2)

		self.Button_github_2.clicked.connect(self.enlace_github_2)
		
		self.Button_instagram.clicked.connect(self.enlace_instagram)
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
	
#== Funciones para abrir enlaces ============================================================================================	

	def enlace_facebook_1(self):

		url = "https://www.facebook.com/JAMSCMD"

		webbrowser.open(url)

	def enlance_github_1(self):

		url = "https://github.com/JoseSierraVzl"

		webbrowser.open(url)

	def enlace_facebook_2(self):

		url = "https://www.facebook.com/rafael.sierra.31542841"

		webbrowser.open(url)

	def enlace_github_2(self):

		url = "https://github.com/CristianCala"

		webbrowser.open(url)

	def enlace_instagram(self):
		url = "https://www.instagram.com/_codeloid/"

		webbrowser.open(url)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Acerca_de()
	interface.show()
	app.exec_()