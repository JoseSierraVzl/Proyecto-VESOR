# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_inicial_menus.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 462)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 462))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes-iconos/Icono_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
        "background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
        "}\n"
        "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, 0, 161, 441))
        self.frame.setStyleSheet("QFrame{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.176136 rgba(0, 0, 0, 90));\n"
        "border-radius: 15px\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 230, 141, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes-iconos/Usuario_blanco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagenes-iconos/Vocero_blanco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 141, 20))
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Imagenes-iconos/Lapiz_blanco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 150, 141, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Imagenes-iconos/Papelera_blanca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 180, 141, 2))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 141, 20))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 260, 151, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 290, 141, 31))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
        "border:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(0, 170, 255);\n"
        "color:rgb(255, 255, 255);\n"
        "font-size: 12px;\n"
        "\n"
        "}")
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(20, 330, 141, 2))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 141, 20))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 390, 121, 20))
        self.lineEdit.setStyleSheet("border-radius: 8px")
        self.lineEdit.setObjectName("lineEdit")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(20, 420, 141, 2))
        self.line_6.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 30, 31, 31))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
        "border-image: url(Imagenes-iconos/Engranaje_blanco.png);\n"
        "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 20))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Nuevo usuario"))
        self.pushButton_4.setText(_translate("MainWindow", "Nuevo vocero"))
        self.label.setText(_translate("MainWindow", "VOCEROS"))
        self.pushButton_5.setText(_translate("MainWindow", " Editar vocero"))
        self.pushButton_6.setText(_translate("MainWindow", "  Eliminar vocero"))
        self.label_3.setText(_translate("MainWindow", "USUARIOS"))
        self.pushButton_3.setText(_translate("MainWindow", "Editar usuario"))
        self.pushButton_7.setText(_translate("MainWindow", "Eliminar usuario"))
        self.label_4.setText(_translate("MainWindow", "Busqueda rapida"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ingrese cedula"))
        self.label_2.setText(_translate("MainWindow", "PANEL DE OPCIONES"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
import Source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
