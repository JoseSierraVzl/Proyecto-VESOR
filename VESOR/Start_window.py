# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_de_registro(object):
    def setupUi(self, Ventana_de_registro):
        Ventana_de_registro.setObjectName("Ventana_de_registro")
        Ventana_de_registro.setEnabled(True)
        Ventana_de_registro.resize(400, 492)
        Ventana_de_registro.setMaximumSize(QtCore.QSize(400, 500))
        Ventana_de_registro.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icono_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ventana_de_registro.setWindowIcon(icon)
        Ventana_de_registro.setStyleSheet("QDialog{\n"
"background-color: rgb(243,243,243);\n"
"border-image: url(:/FONDO/Fondo.jpg);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:rgb(51,0,102)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(226, 226, 226)\n"
"}\n"
"QPushButton#Button_register:hover{\n"
"background-color:rgb(75,75,75);\n"
"color:rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"}")
        self.Frame_start_window = QtWidgets.QFrame(Ventana_de_registro)
        self.Frame_start_window.setGeometry(QtCore.QRect(0, 0, 400, 80))
        self.Frame_start_window.setMaximumSize(QtCore.QSize(400, 80))
        self.Frame_start_window.setStyleSheet("")
        self.Frame_start_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_start_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_start_window.setObjectName("Frame_start_window")
        self.layoutWidget = QtWidgets.QWidget(Ventana_de_registro)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 420, 77, 45))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Button_register = QtWidgets.QPushButton(self.layoutWidget)
        self.Button_register.setObjectName("Button_register")
        self.verticalLayout_2.addWidget(self.Button_register)
        self.frame = QtWidgets.QFrame(Ventana_de_registro)
        self.frame.setGeometry(QtCore.QRect(50, 120, 301, 291))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0.068, y1:0.0854091, x2:0.915, y2:0.931818, stop:0.170455 rgba(0, 0, 0, 183), stop:0.596591 rgba(0, 0, 0, 183));\n"
"border-radius: 30px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_register_status = QtWidgets.QLabel(self.frame)
        self.label_register_status.setGeometry(QtCore.QRect(20, 240, 261, 31))
        self.label_register_status.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255)")
        self.label_register_status.setTextFormat(QtCore.Qt.RichText)
        self.label_register_status.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.label_register_status.setIndent(5)
        self.label_register_status.setObjectName("label_register_status")
        self.label_subtitle = QtWidgets.QLabel(self.frame)
        self.label_subtitle.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.label_subtitle.setStyleSheet("QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        self.label_user = QtWidgets.QLabel(self.frame)
        self.label_user.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_user.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 14px")
        self.label_user.setObjectName("label_user")
        self.line_user = QtWidgets.QLineEdit(self.frame)
        self.line_user.setEnabled(True)
        self.line_user.setGeometry(QtCore.QRect(20, 90, 261, 21))
        self.line_user.setAutoFillBackground(False)
        self.line_user.setStyleSheet("\n"
"border-radius: 5px;\n"
"color: rgb(2, 2, 2)")
        self.line_user.setInputMask("")
        self.line_user.setText("")
        self.line_user.setFrame(True)
        self.line_user.setObjectName("line_user")
        self.label_password = QtWidgets.QLabel(self.frame)
        self.label_password.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label_password.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 14px")
        self.label_password.setObjectName("label_password")
        self.line_password = QtWidgets.QLineEdit(self.frame)
        self.line_password.setGeometry(QtCore.QRect(20, 150, 261, 21))
        self.line_password.setStyleSheet("border-radius: 5px;\n"
"color: rgb(2, 2, 2)")
        self.line_password.setObjectName("line_password")
        self.label_password2 = QtWidgets.QLabel(self.frame)
        self.label_password2.setGeometry(QtCore.QRect(20, 190, 231, 16))
        self.label_password2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);\n"
"font-size: 14px")
        self.label_password2.setObjectName("label_password2")
        self.line_password2 = QtWidgets.QLineEdit(self.frame)
        self.line_password2.setGeometry(QtCore.QRect(20, 210, 261, 21))
        self.line_password2.setStyleSheet("border-radius: 5px;\n"
"color: rgb(2, 2, 2)")
        self.line_password2.setObjectName("line_password2")

        self.retranslateUi(Ventana_de_registro)
        QtCore.QMetaObject.connectSlotsByName(Ventana_de_registro)

    def retranslateUi(self, Ventana_de_registro):
        _translate = QtCore.QCoreApplication.translate
        Ventana_de_registro.setWindowTitle(_translate("Ventana_de_registro", "Registro"))
        self.Button_register.setText(_translate("Ventana_de_registro", "Registrar"))
        self.label_register_status.setText(_translate("Ventana_de_registro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_subtitle.setText(_translate("Ventana_de_registro", "Registra un usuario"))
        self.label_user.setText(_translate("Ventana_de_registro", "Usuario:"))
        self.label_password.setText(_translate("Ventana_de_registro", "Contraseña:"))
        self.label_password2.setText(_translate("Ventana_de_registro", "Ingresa la contraseña nuevamente:"))


from Source_rc import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_de_registro = QtWidgets.QDialog()
    ui = Ui_Ventana_de_registro()
    ui.setupUi(Ventana_de_registro)
    Ventana_de_registro.show()
    sys.exit(app.exec_())
