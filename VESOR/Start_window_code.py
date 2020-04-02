from Start_window import *
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton, QFrame
from PyQt5.QtCore import Qt
import sys

class Start_window(Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	############################################################################	
		self.line_user.textChanged.connect(self.Validate_User)



	#############################################################################	
	def Validate_User(self):
		line_user = self.line_user.text()
		validate = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', line_user, re.I)
		if line_user == "":
			self.line_user.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validate:
			self.line_user.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.line_user.setStyleSheet("border: 1px solid green;")
			return True


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Start_window()
	window.show()
	app.exec_()







