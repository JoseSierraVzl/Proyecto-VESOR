###Holaaaa###
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 380)
        Dialog.setMaximumSize(QtCore.QSize(400, 380))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(243,243,243)\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:rgb(51,0,102)\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(243,243,243);\n"
"color:rgb(0, 0, 0);\n"
"font-size: 12px\n"
"}\n"
"\n"
"QPushButton#Button_register:hover{\n"
"background-color:rgb(75,75,75);\n"
"color:rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"}")
        self.Frame_start_window = QtWidgets.QFrame(Dialog)
        self.Frame_start_window.setGeometry(QtCore.QRect(0, 0, 400, 80))
        self.Frame_start_window.setMaximumSize(QtCore.QSize(400, 80))
        self.Frame_start_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_start_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_start_window.setObjectName("Frame_start_window")
        self.label_title = QtWidgets.QLabel(self.Frame_start_window)
        self.label_title.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.label_title.setObjectName("label_title")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(160, 320, 77, 45))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Button_register = QtWidgets.QPushButton(self.widget)
        self.Button_register.setObjectName("Button_register")
        self.verticalLayout_2.addWidget(self.Button_register)
        self.label_register_status = QtWidgets.QLabel(self.widget)
        self.label_register_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_register_status.setObjectName("label_register_status")
        self.verticalLayout_2.addWidget(self.label_register_status)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(100, 90, 197, 216))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_subtitle = QtWidgets.QLabel(self.widget1)
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout_3.addWidget(self.label_subtitle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_user = QtWidgets.QLabel(self.widget1)
        self.label_user.setObjectName("label_user")
        self.verticalLayout.addWidget(self.label_user)
        self.line_user = QtWidgets.QLineEdit(self.widget1)
        self.line_user.setObjectName("line_user")
        self.verticalLayout.addWidget(self.line_user)
        self.label_status_user = QtWidgets.QLabel(self.widget1)
        self.label_status_user.setObjectName("label_status_user")
        self.verticalLayout.addWidget(self.label_status_user)
        self.label_password = QtWidgets.QLabel(self.widget1)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.line_password = QtWidgets.QLineEdit(self.widget1)
        self.line_password.setObjectName("line_password")
        self.verticalLayout.addWidget(self.line_password)
        self.label_status_password = QtWidgets.QLabel(self.widget1)
        self.label_status_password.setObjectName("label_status_password")
        self.verticalLayout.addWidget(self.label_status_password)
        self.label_password2 = QtWidgets.QLabel(self.widget1)
        self.label_password2.setObjectName("label_password2")
        self.verticalLayout.addWidget(self.label_password2)
        self.line_password2 = QtWidgets.QLineEdit(self.widget1)
        self.line_password2.setObjectName("line_password2")
        self.verticalLayout.addWidget(self.line_password2)
        self.label_password2_status = QtWidgets.QLabel(self.widget1)
        self.label_password2_status.setObjectName("label_password2_status")
        self.verticalLayout.addWidget(self.label_password2_status)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "Titulo (Membrete)"))
        self.Button_register.setText(_translate("Dialog", "Registrar"))
        self.label_register_status.setText(_translate("Dialog", "STATUS"))
        self.label_subtitle.setText(_translate("Dialog", "Registra un un usuario"))
        self.label_user.setText(_translate("Dialog", "Usuario:"))
        self.label_status_user.setText(_translate("Dialog", "STATUS"))
        self.label_password.setText(_translate("Dialog", "Contraseña:"))
        self.label_status_password.setText(_translate("Dialog", "STATUS"))
        self.label_password2.setText(_translate("Dialog", "Ingresa la contraseña nuevamente:"))
        self.label_password2_status.setText(_translate("Dialog", "STATUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
