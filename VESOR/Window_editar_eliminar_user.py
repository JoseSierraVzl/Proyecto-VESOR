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




if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Window_edit_elim_user()
	interface.show()
	app.exec_()


