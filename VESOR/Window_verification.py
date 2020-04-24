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
QMainWindow, QAction, QLabel, QFrame,)
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import  uic
from Login_window import *
from Start_window_code import *

class CustomWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.Label = QtWidgets.QLabel(self)
        self.Label.setGeometry(QRect(460, 300, 200, 100))
        self.Label.setText("Bienvenidos a ")
        self.Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                "font: 75 14pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);")

        self.label_dos = QtWidgets.QLabel(self)
        self.label_dos.setGeometry(QRect(520, 380, 72, 80))
        self.label_dos.setText("V")
        self.label_dos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                "font: 70pt \"Lucida Handwriting\";\n"
                "color:qlineargradient(spread:pad, x1:0.075, y1:0.977, x2:0.835, y2:0.170455, stop:0.0852273 rgba(255, 57, 107, 255), stop:0.676136 rgba(255, 241, 131, 255))")

        self.label_tres = QtWidgets.QLabel(self)
        self.label_tres.setGeometry(QRect(590, 400, 200, 59))
        self.label_tres.setText("ESOR")
        self.label_tres.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                "font: 50pt \"Lucida Handwriting\";\n"
                "color:qlineargradient(spread:pad, x1:0.671, y1:0.108, x2:0.255045, y2:0.801, stop:0.0852273 rgba(255, 57, 107, 255), stop:0.676136 rgba(255, 241, 131, 255))")

        self.Label_cuatro = QtWidgets.QLabel(self)
        self.Label_cuatro.setGeometry(QRect(650, 430, 300, 100))
        self.Label_cuatro.setText("El programa de gestion comunitaria")
        self.Label_cuatro.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
                "font: 75 13pt \"MS Shell Dlg 2\";\n"
                "color: rgb(255, 255, 255);")

    def paintEvent(self, event = None):
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