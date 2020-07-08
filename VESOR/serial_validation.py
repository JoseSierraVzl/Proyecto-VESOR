import sqlite3
from os import getcwd, makedirs
from Source_rc import *
import sys
import os
import time

from time import clock
from random import randint
from PyQt5 import uic

from PyQt5.QtGui import (QFont, QIcon, QResizeEvent, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
                         QRegExpValidator, QImage)
from PyQt5.QtCore import (pyqtSlot, Qt, QDir, QPoint, pyqtSignal,QTimer, QTime,QByteArray, QIODevice, QBuffer, QFile, QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator, QLocale,
                          QLocale, QLibraryInfo, QFileInfo, QDir, QPropertyAnimation, QTranslator, QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu,
                             QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
                             QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
                             QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog, QGraphicsEffect, QVBoxLayout,
                             QGraphicsDropShadowEffect, QGraphicsBlurEffect, QSpinBox)


class serial_validation(QDialog):

    def __init__(self, parent=None):
        super(serial_validation, self).__init__()
        self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))

        self.setWindowTitle("Validación de Vesor")
        self.setWindowFlags(
            Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.setFixedSize(530, 542)
        self.setStyleSheet("QDialog{\n"
                           "background-color: qlineargradient(spread:pad, x1:0.063, y1:0.346591, x2:0.982955, y2:0.477, stop:0 rgba(85, 85, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
                           "}\n"
                           "")
        self.initUi()
        #self.Mostrar_1()
        #self.Mostrar_imagenes()
        self.time_image()

    def initUi(self):

        #Style #############################################

        # Style de carousel
        style_frame_carousel = ("QFrame\n"
                                "{\n"
                                "color:#1b231f;\n"
                                "background-color: #E5E7EE;\n"
                                "font: 75 10pt Comic Sans MS;\n"
                                "border-radius: 22px;\n"
                                "}")
        ###

        # Style Label Vesor
        style_label_vesor = (
            "QLabel{border-image: url(:/Titulo_vesor/Imagenes-iconos/VESOR.png)}")
        ###

        # Style label text
        style_label_text = ("QLabel{\n"
                            "color:#12191D;\n"
                            "font: 12pt 'Arial';\n"
                            "border-radius: 6px;\n"
                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                            "}")
        ###

        # Style LineEdit_serial
        style_lineEdit_serial = ("QLineEdit{\n"
                                    "border-radius: 5px;\n"
                                    "color:  #000000;\n"
                                    "background-color:#ffffff;\n"
                                    "}\n"
                                    "QLineEdit:hover{\n"
                                    "border: 1px solid rgb(85, 0, 127);\n"
                                    "}")
        ###

        #Style QPushButton
        style_QPushButton = ("QPushButton{\n"
                            "background-color:rgb(255, 255, 255);\n"
                            "border-radius: 5px;\n"
                            "border: 1px solid rgb(85, 0, 255);\n"
                            "font-size: 12px;\n"
                            "color: #000000\n"
                            "}\n"
                            "QPushButton:hover{\n"
                            "background-color:qlineargradient(spread:pad, x1:0.068, y1:0.0854091, x2:0.915, y2:0.931818, stop:0.170455 rgba(0, 0, 0, 183), stop:0.596591 rgba(0, 0, 0, 183));\n"
                            "color:rgb(255, 255, 255);\n"
                            "font-size: 12px;\n"
                            "border-radius: 5px;\n"
                            "}")
        ###

        # Style_labelImagen_1
        style_labelImagen_1 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_1.png);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###
        # style_labelImagen_2
        style_labelImagen_2 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_2.png);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###
        # style_labelImagen_3
        style_labelImagen_3 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_3.png);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###

        # style_labelImagen_4
        style_labelImagen_4 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_4.jpg);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###

        # style_labelImagen_5
        style_labelImagen_5 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_5.jpg);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###

        # style_labelImagen_6
        style_labelImagen_6 = ("QLabel{\n"
                               "border-radius: 22px;\n"
                               "border-image: url(:/Imagenes/Imagenes-iconos/imagen_6.jpg);\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0));\n"
                               "}")
        ###
        #####################################################
        
        self.frame_carousel = QFrame(self)
        self.frame_carousel.setGeometry(QRect(20, 90, 491, 361))
        self.frame_carousel.setStyleSheet(style_frame_carousel)

        self.label_vesor = QLabel(self)
        self.label_vesor.setGeometry(QRect(80, -55, 361, 201))
        self.label_vesor.setStyleSheet(style_label_vesor)

        self.label_text = QLabel(self)
        self.label_text.setGeometry(QRect(20, 460, 411, 20))
        self.label_text.setStyleSheet(style_label_text)
        self.label_text.setText("Ingrese el serial para validar el programa")
        self.label_text.setAlignment(Qt.AlignCenter)

        self.lineEdit_serial = QLineEdit(self)
        self.lineEdit_serial.setGeometry(QRect(20, 490, 411, 32))
        self.lineEdit_serial.setAlignment(Qt.AlignCenter)
        self.lineEdit_serial.setStyleSheet(style_lineEdit_serial)
        self.lineEdit_serial.setToolTip("Ingrese el serial para la validación del programa")


        self.buttonAceptar = QPushButton(self)
        self.buttonAceptar.setGeometry(QRect(450,460,61,31))
        self.buttonAceptar.setStyleSheet(style_QPushButton)
        self.buttonAceptar.setText("Aceptar")

        self.buttonCancelar = QPushButton(self)
        self.buttonCancelar.setGeometry(QRect(450,500,61,31))
        self.buttonCancelar.setStyleSheet(style_QPushButton)
        self.buttonCancelar.setText("Cancelar")

        #Label description
        self.label_description_1 = QLabel(self)
        self.label_description_1.setGeometry(QRect(20, 100, 491, 20))
        self.label_description_1.setStyleSheet(style_label_text)
        self.label_description_1.setText("")
        self.label_description_1.setAlignment(Qt.AlignCenter)
        ###

        # Imagen_1
        self.label_Imagen_1 = QLabel(self.frame_carousel)
        self.label_Imagen_1.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_1.setStyleSheet(style_labelImagen_1)
        ###


        # Imagen_2
        self.label_Imagen_2 = QLabel(self.frame_carousel)
        self.label_Imagen_2.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_2.setStyleSheet(style_labelImagen_2)
        ###

        #Imagen_3
        self.label_Imagen_3 = QLabel(self.frame_carousel)
        self.label_Imagen_3.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_3.setStyleSheet(style_labelImagen_3)
        ###
  
        #Imagen_4
        self.label_Imagen_4 = QLabel(self.frame_carousel)
        self.label_Imagen_4.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_4.setStyleSheet(style_labelImagen_4)
        ###

        #Imagen_5
        self.label_Imagen_5 = QLabel(self.frame_carousel)
        self.label_Imagen_5.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_5.setStyleSheet(style_labelImagen_5)
        ###

        #Imagen_6
        self.label_Imagen_6 = QLabel(self.frame_carousel)
        self.label_Imagen_6.setGeometry(QRect(-520, 40, 451, 311))
        self.label_Imagen_6.setStyleSheet(style_labelImagen_6)
        ###

    def time_image(self):
        self.timer_imagen = QTimer()
        self.timer_imagen.singleShot(500, self.Mostrar_imagenes)
        self.timer_imagen.singleShot(69000, self.Mostrar_imagenes)
        self.timer_imagen.singleShot(138000, self.Mostrar_imagenes)
        self.timer_imagen.singleShot(276000, self.Mostrar_imagenes)
    
    def Mostrar_imagenes(self):

        self.timer = QTimer()
        self.timer.singleShot(500, self.Mostrar_1)        
        self.timer.singleShot(10000, self.Ocultar_1)

        self.timer.singleShot(11500, self.Mostrar_2)
        self.timer.singleShot(21500, self.Ocultar_2)

        self.timer.singleShot(23000, self.Mostrar_3)
        self.timer.singleShot(33000, self.Ocultar_3)

        self.timer.singleShot(34500, self.Mostrar_4)
        self.timer.singleShot(44500, self.Ocultar_4)

        self.timer.singleShot(46000, self.Mostrar_5)
        self.timer.singleShot(56000, self.Ocultar_5)

        self.timer.singleShot(57500, self.Mostrar_6)
        self.timer.singleShot(67500, self.Ocultar_6)





    def Mostrar_1(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_1, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("Vista general de datos")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)
    def Ocultar_1(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_1, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Mostrar_2(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_2, b"geometry")
        self.animacionMostar.finished.connect(lambda: (
            self.label_description_1.setText("Registro de usuarios de forma detallada")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Ocultar_2(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_2, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)


    def Mostrar_3(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_3, b"geometry")
        self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText(
            "Vista general de usuarios ordenados por numero de vivienda")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Ocultar_3(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_3, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)


    def Mostrar_4(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
        self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText("Opciones de búsqueda especificadas")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Ocultar_4(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_4, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)


    def Mostrar_5(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_5, b"geometry")
        self.animacionMostar.finished.connect(lambda: (self.label_description_1.setText(
            "Visualización de fecha y hora de registro del usuario")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Ocultar_5(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_5, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Mostrar_6(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_6, b"geometry")
        self.animacionMostar.finished.connect(lambda: (
            self.label_description_1.setText("Registro completo y detallado del usuario")))
        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(590, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(20, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

    def Ocultar_6(self):

        self.animacionMostar = QPropertyAnimation(self.label_Imagen_6, b"geometry")
        self.animacionMostar.finished.connect(lambda:(self.label_description_1.setText("")))

        self.animacionMostar.setDuration(500)
        self.animacionMostar.setStartValue(QRect(20, 40, 451, 311))
        self.animacionMostar.setEndValue(QRect(-590, 40, 451, 311))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)














if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = serial_validation()
    interface.show()
    app.exec_()
