import sys
import time
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMessageBox,QApplication, QDialog, QLineEdit,
QMainWindow, QAction, QLabel, QFrame, QWidget, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import  uic
from Login_window import *
from Start_window_code import *

class CustomWindow(QMainWindow):

	Color = QColor(104, 189, 155)
	Clockwise = True
	Delta = 36


	def __init__(self, *args, color=None, clockwise=True, **kwargs):
		super(CustomWindow, self).__init__(*args, **kwargs)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_NoSystemBackground, True)
		self.setAttribute(Qt.WA_TranslucentBackground, True)


		self.Label = QtWidgets.QLabel(self)
		self.Label.setGeometry(QRect(390, 300, 200, 100))
		self.Label.setText("Bienvenidos a ")
		self.Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
				"font: 75 14pt \"MS Shell Dlg 2\";\n"
				"color: rgb(255, 255, 255);")


		self.label_tres = QtWidgets.QLabel(self)
		self.label_tres.setGeometry(QRect(420, 290, 341, 251))
		self.label_tres.setStyleSheet("QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png);}")

		self.Label_cuatro = QtWidgets.QLabel(self)
		self.Label_cuatro.setGeometry(QRect(590, 430, 340, 100))
		self.Label_cuatro.setText("El programa de gestion comunitaria")
		self.Label_cuatro.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
				"font: 75 13pt \"MS Shell Dlg 2\";\n"
				"color: rgb(255, 255, 255);")

		self.angle	= 0
		self.Clockwise = clockwise
		if color:
			self.Color = color
		self._timer = QTimer(self, timeout = self.update)
		self._timer.start(100)




	# def paintEvent(self, event = None):

			


	def paintEvent(self, event):

		pinturito = QPainter(self)
		pinturito.setRenderHint(QPainter.Antialiasing)
		pinturito.translate(650,650)
		side = min(self.width(), self.height())
		pinturito.scale(side / 100.0, side / 100.0)
		pinturito.rotate(self.angle)
		pinturito.save()
		pinturito.setPen(Qt.NoPen)
		color = self.Color.toRgb()
		for i in range(11):
			color.setAlphaF(1.0 * i / 10)
			pinturito.setBrush(color)
			#pinturito.drawEllipse(30, -10, 20, 20)
			pinturito.drawEllipse(5,-5,5,5)
			pinturito.rotate(36)
		pinturito.restore()
		self.angle += self.Delta if self.Clockwise else -self.Delta
		self.angle %= 360

		painter = QtGui.QPainter(self) 
		painter.setOpacity(0.3)
		painter.setBrush(Qt.black)
		painter.setPen(QPen(Qt.black))   
		painter.drawRect(self.rect())



		self._timer = QTimer()
		self._timer.singleShot(5000, self.Validator)


	def Validator(self):
		if os.path.isfile('Users_database.db'):
			self.login_window = Login_window()
			self.login_window.show()
			self.destroy() 
		else:
			self.startwindow = Start_window()
			self.startwindow.show()
			Window_ventana.hide()

	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	Window_ventana = CustomWindow()
	Window_ventana.showFullScreen()
	Window_ventana.show()
	sys.exit(app.exec())