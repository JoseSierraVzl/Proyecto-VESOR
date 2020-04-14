# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMessageBox,QApplication, QDialog, QLineEdit,
QMainWindow, QAction, QLabel, QFrame,)
from PyQt5.QtGui import QIcon,QImage, QColor, QPixmap
from PyQt5.QtCore import Qt
from Source_rc import *
import sys
import sqlite3


class Ui_Window_login(object):

#==================================================== #Ventana# ===============================================================
    def setupUi(self, Window_login):
        Window_login.setObjectName("Window_login")
        Window_login.resize(300, 350)
        Window_login.setMinimumSize(QtCore.QSize(300, 350))
        Window_login.setMaximumSize(QtCore.QSize(300, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icono_window/Icono_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window_login.setWindowIcon(icon)
        Window_login.setAutoFillBackground(False)
        Window_login.setStyleSheet("QDialog{\n"
"background-color: rgb(243,243,243);\n"
"border-image: url(:/FONDO/Fondo.jpg);\n"
"\n"
"}\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(Window_login)
        self.frame.setGeometry(QtCore.QRect(30, 80, 241, 211))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0.068, y1:0.0854091, x2:0.915, y2:0.931818, stop:0.170455 rgba(0, 0, 0, 183), stop:0.596591 rgba(0, 0, 0, 183));\n"
"border-radius: 30px\n"
"}\n"
"QFrame:hover{\n"
"border: 1px solid rgb(255, 255, 255)\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 10, 81, 31))
        self.label.setStyleSheet("QLabel{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"color:rgb(255, 255, 255);\n"
"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"color:rgb(255, 255, 255);\n"
"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 31))
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"color:rgb(255, 255, 255);\n"
"border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 201, 20))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-radius: 5px;\n"
"color: rgb(2, 2, 2);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85, 0, 127);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 140, 201, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-radius: 5px;\n"
"color: rgb(2, 2, 2);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 1px solid rgb(85, 0, 127);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 201, 31))
        self.label_7.setStyleSheet("QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"border: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Window_login)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 51, 51))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 35pt \"Lucida Handwriting\";\n"
"color:qlineargradient(spread:pad, x1:0.075, y1:0.977, x2:0.835, y2:0.170455, stop:0.0852273 rgba(255, 57, 107, 255), stop:0.676136 rgba(255, 241, 131, 255))")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Window_login)
        self.label_5.setGeometry(QtCore.QRect(120, 20, 101, 41))
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 20pt \"Lucida Handwriting\";\n"
"color:qlineargradient(spread:pad, x1:0.671, y1:0.108, x2:0.255045, y2:0.801, stop:0.0852273 rgba(255, 57, 107, 255), stop:0.676136 rgba(255, 241, 131, 255))")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Window_login)
        self.label_6.setGeometry(QtCore.QRect(80, 50, 161, 16))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(Window_login)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 301, 81))
        self.frame_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.505682, y1:0.011, x2:0.494, y2:0.994318, stop:0.3125 rgba(96, 49, 174, 189), stop:1 rgba(71, 77, 255, 0))")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Button_iniciar = QtWidgets.QPushButton(Window_login)
        self.Button_iniciar.setGeometry(QtCore.QRect(60, 310, 81, 21))
        self.Button_iniciar.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(85, 0, 255);\n"
"font-size: 12px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0.068, y1:0.0854091, x2:0.915, y2:0.931818, stop:0.170455 rgba(0, 0, 0, 183), stop:0.596591 rgba(0, 0, 0, 183));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.Button_iniciar.setObjectName("Button_iniciar")
        self.pushButton_2 = QtWidgets.QPushButton(Window_login)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 310, 81, 21))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(85, 0, 255);\n"
"font-size: 12px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0.068, y1:0.0854091, x2:0.915, y2:0.931818, stop:0.170455 rgba(0, 0, 0, 183), stop:0.596591 rgba(0, 0, 0, 183));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.Button_iniciar.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Window_login)
        QtCore.QMetaObject.connectSlotsByName(Window_login)

        self.Button_iniciar.clicked.connect(self.login_iniciar)

    def retranslateUi(self, Window_login):
        _translate = QtCore.QCoreApplication.translate
        Window_login.setWindowTitle(_translate("Window_login", "Iniciar"))
        self.label.setText(_translate("Window_login", "Iniciar secion"))
        self.label_2.setText(_translate("Window_login", "Usuario:"))
        self.label_3.setText(_translate("Window_login", "Contraseña:"))
        self.lineEdit.setPlaceholderText(_translate("Window_login", "Ingresa tu usuario"))
        self.lineEdit_2.setPlaceholderText(_translate("Window_login", "Ingresa tu contraseña"))
        self.label_4.setText(_translate("Window_login", "V"))
        self.label_5.setText(_translate("Window_login", "ESOR"))
        self.label_6.setText(_translate("Window_login", "Una sociedad organizada"))
        self.Button_iniciar.setText(_translate("Window_login", "Iniciar"))
        self.pushButton_2.setText(_translate("Window_login", "Cancelar"))
#===========================================================================================================================================

    def login_iniciar(self):

            with sqlite3.connect('Users_database.db') as db:
                cursor = db.cursor()
                
            User = str(self.lineEdit.text())
            Password = str(self.lineEdit_2.text())

            cursor.execute('SELECT * FROM DATA_USERS WHERE USERS = ? and PASSWORD = ?',(User,Password))
            data = cursor.fetchone()
            if data != None:
                info = '''
                    ¡Bienvenido! %s,
                    Presione Yes para continuar...
                    ''' %(data[0]) 
                QMessageBox.information(Window_login,"Iniciar",info, QMessageBox.Yes)
                sys.exit()

            else:
                QMessageBox.warning(Window_login,"Error","Usuario o contraseña inconrrectos", QMessageBox.Discard)

#============================================================================================================================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_login = QtWidgets.QDialog()
    ui = Ui_Window_login()
    ui.setupUi(Window_login)
    Window_login.show()
    sys.exit(app.exec_())
