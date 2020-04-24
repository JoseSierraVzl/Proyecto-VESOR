import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QLineEdit,
QMainWindow, QAction, QLabel, QFrame)


 
class Interface(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("Ventana_inicial_menus.ui", self)


		# self.pushButton_4.clicked.connect(self.Exit)
		# self.actionCerrar.clicked.connect(self.Exit)




	def Exit(self):
		Question = QMessageBox.question(self, "¡¡Advertencia!!", "¿Seguro que desea salir?",
		QMessageBox.Yes | QMessageBox.No)
		if Question == QMessageBox.Yes:
			exit()
		else: pass   		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()