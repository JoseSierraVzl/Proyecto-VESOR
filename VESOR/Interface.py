#======================================================================================================
import sqlite3
from Source_rc import *

#=============================== Ventans importadas =======================================================
from Window_editar_eliminar_user import*

from Window_status_user import *

from Window_nv_user import *

from Window_acerda_de_vesor import *

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
import sys
from PyQt5 import  uic 

from PyQt5.QtGui import (QIcon,QRegExpValidator)
from PyQt5.QtCore import (Qt,QFile, QTimer,QRegExp)

from PyQt5.QtWidgets import (QApplication, QMainWindow,QMenu,QMessageBox, QGraphicsDropShadowEffect)


#======================================================================================================


 
class Interface(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("Ventana_inicial_menus.ui", self)
		self.setWindowTitle("Menu principal")
		self.setWindowIcon(QIcon("Imagenes-iconos/Icono_window.png"))
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.frame.setGraphicsEffect(self.shadow)
		self.valor_1.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_1))
		self.valor_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self.valor_1_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self.valor_2_2.setValidator(QRegExpValidator(QRegExp("[0-9]+"),self.valor_2))
		self._timer = QTimer()
		self._timer.singleShot(1000, self.mostrar_datos)
		
		#Interacciones 
		self.operacion_1.setToolTip("Presione aquí para realizar la operación")
		self.operacion_2.setToolTip("Presione aquí para realizar la operación")

		self.Cantidad_m.setToolTip("Cantidad total de hombres registrados")
		self.Cantidad_f.setToolTip("Cantidad total de mujeres registradas")
		self.Cantidad_rep.setToolTip("Cantidad total de usuarios registrados\n"
									"en el Registro Electoral Permanente")
		self.Cantidad_estudiante.setToolTip("Cantidad total de estudiantes registrados")
		self.Cantidad_discapacidad.setToolTip("Cantidad total de discapacitados registrados")
		self.Cantidad_enfermedad.setToolTip("Cantidad total de enfermos registrados")
		self.Cantidad_pensionado.setToolTip("Cantidad total de pensionados registrados")
		self.Cantidad_embarazo.setToolTip("Cantidad total de embarazadas registradas")
		self.Cantidad_lactante.setToolTip("Cantidad total de lactantes registradas")
		self.groupBox_3.setToolTip("Cantidad total de usuarios registrados, distribuidos por edades")
		self.Button_menu_2.setToolTip("Click para actualizar la vista general de datos de usuario")

		##############

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_2.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_3.setGraphicsEffect(self.shadow)

		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.groupBox_5.setGraphicsEffect(self.shadow)
		#Menu 1 =====================================================================================================	

		self.menuArchivo = QMenu()
		self.menuArchivo.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:1px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:5px;"
		"margin-right:5px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		
		self.acercade = self.menuArchivo.addAction("Acerca de VESOR", self.Abrir_window)
		
		self.ayuda = self.menuArchivo.addAction("Ayuda")
		#======================================================================================================

		#Menu de opcionesde usuario =====================================================================================================	

		self.menu_usuario = QMenu()
		self.menu_usuario.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_user = self.menu_usuario.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar usuario", self.Nuevo_user)
		self.Editar_usuario = self.menu_usuario.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Eliminar usuario", self.Editar_usuario)

		#Menu de opciones de vocero =====================================================================================================	

		self.menu_vocero = QMenu()
		self.menu_vocero.setStyleSheet("QMenu{background-color:#12191D;\n"
		"color: #ffffff;\n"
		"height:57px;\n"
		"width:180px;\n"
		"margin:0px;\n}"

		"QMenu:separator{height:10px;"
		"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
		"stop:0 rgba(173, 181, 189, 95));"
		"margin-left:2px;"
		"margin-right:2px;}"

		"QMenu::item::selected{\n"
		"background-color:rgb(0, 170, 255);"
		"}")
		self.Registrar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_registrar/Imagenes-iconos/Registrar.png"),"Registrar vocero", self.Nv_vocero)

		self.Editar_vocero = self.menu_vocero.addAction(QIcon(":/Icono_papelera/Imagenes-iconos/Papelera_blanca.png"),"Editar o Elimina vocero")



#========================================= #Eventos# ==================================================================
		self.operacion_1.clicked.connect(self.realizar_operacion_1)
		self.operacion_2.clicked.connect(self.realizar_operacion_2)
	
		self.Button_menu.setMenu(self.menuArchivo)

		self.buttonNewUser.setMenu(self.menu_usuario)
		self.buttonNewUser.setToolTip("Click para ver opciones de usuario")

		self.buttonStatus.setToolTip("Click para ver estatus de los usuarios")
		self.buttonStatus.clicked.connect(self.Abrir_ventana)

		#self.buttonVoceroNew.setMenu(self.menu_vocero)
		#self.buttonVoceroNew.setToolTip("Click para ver opciones de vocero")
		
		#self.buttonNewUser.clicked.connect(self.Nuevo_user)

		#self.buttonEditUser.clicked.connect(self.Editar_usuario)

		#self.lineEditSearch.setToolTip("Ingresa la cedula de quien deseas buscar.")

		self.Button_menu_2.clicked.connect(self.mostrar_datos)
		self.Button_menu_2.setToolTip("Click para actualizar la vista general de datos de usuario")
#======================================== #Funciones# ==================================================================


	def mostrar_datos(self):

		if QFile.exists("Base de datos/DB_VESOR_USER_DATOSGENERALES.db"):

			try: 
				self.con = sqlite3.connect("Base de datos/DB_VESOR_USER_DATOSGENERALES.db")
				self.cursor_masculino = self.con.cursor()
				self.cursor_femenino = self.con.cursor()
				self.cursor_edad_0 = self.con.cursor()
				self.cursor_edad_13 = self.con.cursor()
				self.cursor_edad_18 = self.con.cursor()
				self.cursor_edad_30 = self.con.cursor()
				self.cursor_edad_55 = self.con.cursor()
				self.cursor_estud = self.con.cursor()
				self.cursor_rep = self.con.cursor()
				self.cursor_pensionado = self.con.cursor()
				self.cursor_discapacidad = self.con.cursor()
				self.cursor_enfermedad = self.con.cursor()
				self.cursor_enbarazo = self.con.cursor()
				self.cursor_lactante = self.con.cursor()

				#Cursor masculino
				self.cursor_masculino.execute("SELECT COUNT(GENERO) FROM USUARIO_DT_GNR WHERE GENERO = 'Masculino'")
				dato_masculino = self.cursor_masculino.fetchall()
				for m in dato_masculino:
					dato_m = m[0]
				print(dato_m)
				mostrar_m = str(dato_m)
				self.Cantidad_m.setText(mostrar_m)

				#Cursor femenino
				self.cursor_femenino.execute("SELECT COUNT(GENERO) FROM USUARIO_DT_GNR WHERE GENERO = 'Femenino'")
				dato_femenino = self.cursor_femenino.fetchall()
				for f in dato_femenino:
					dato_f = f[0]
				print(dato_f)
				mostrar_f = str(dato_f)
				self.Cantidad_f.setText(mostrar_f)

				#Cursor edad  >= 0 años
				self.cursor_edad_0.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 0 AND EDAD <= 12 ")
				dato_edad_0 = self.cursor_edad_0.fetchall()
				for e_0 in dato_edad_0:
					dato_e_0 = e_0[0]
				print(dato_e_0)
				dato_0_12 = str(dato_e_0)
				self.Cantidad_0_12.setText(dato_0_12)

				#Cursor edad  >= 13 años
				self.cursor_edad_13.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 13 AND EDAD <= 18")
				dato_edad_13 = self.cursor_edad_13.fetchall()
				for e_13 in dato_edad_13:
					dato_e_13 = e_13[0]
				print(dato_e_13)
				dato_12_18 =str(dato_e_13)
				self.Cantidad_12_18.setText(dato_12_18)

				#Cursor edad  >= 18 años
				self.cursor_edad_18.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 19 AND EDAD <= 30")
				dato_edad_18 = self.cursor_edad_18.fetchall()
				for e_18 in dato_edad_18:
					dato_e_18 = e_18[0]
				print(dato_e_18)
				dato_19_30 = str(dato_e_18)
				self.Cantidad_19_30.setText(dato_19_30)

				#Cursor edad  >= 30 años
				self.cursor_edad_30.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 31 AND EDAD <= 54")
				dato_edad_30 = self.cursor_edad_30.fetchall()
				for e_30 in dato_edad_30:
					dato_e_30 = e_30[0]
				print(dato_e_30)
				dato_31_54 = str(dato_e_30)
				self.Cantidad_31_54.setText(dato_31_54)

				#Cursor edad  >= 55 años
				self.cursor_edad_55.execute("SELECT COUNT(EDAD) FROM USUARIO_DT_GNR WHERE EDAD >= 55")
				dato_edad_55 = self.cursor_edad_55.fetchall()
				for e_55 in dato_edad_55:
					dato_e_55 = e_55[0]
				print(dato_e_55)
				dato_mayor_55 = str(dato_e_55)
				self.Cantidad_55.setText(dato_mayor_55)

				#Cursor estudiante
				self.cursor_estud.execute("SELECT COUNT(PROFESION_OFICIO) FROM USUARIO_DT_GNR WHERE PROFESION_OFICIO = 'Estudiante'")
				dato_estudiante = self.cursor_estud.fetchall()
				for estudiante in dato_estudiante:
					dato_de_estudiante = estudiante[0]
				print(dato_de_estudiante) 
				dato_mostrar_estudiante = str(dato_de_estudiante)
				self.Cantidad_estudiante.setText(dato_mostrar_estudiante)


				#Inscrito en el REP
				self.cursor_rep.execute("SELECT COUNT(INSCRITO_REP) FROM USUARIO_DT_GNR WHERE INSCRITO_REP = 'Si'")
				dato_rep= self.cursor_rep.fetchall()
				for rep in dato_rep:
					dato_de_rep = rep[0]
				print(dato_de_rep) 
				dato_mostrar_rep = str(dato_de_rep)
				self.Cantidad_rep.setText(dato_mostrar_rep)



				#Si esta pensionado 
				self.cursor_pensionado.execute("SELECT COUNT(PENSIONADO) FROM USUARIO_DT_GNR WHERE PENSIONADO = 'Pensionado'")
				dato_pensionado= self.cursor_pensionado.fetchall()
				for pensionado in dato_pensionado:
					dato_de_pensionado = pensionado[0]
				print(dato_de_pensionado) 
				dato_mostrar_pensionado = str(dato_de_pensionado)
				self.Cantidad_pensionado.setText(dato_mostrar_pensionado)

				#Si posee discapacidad
				self.cursor_discapacidad.execute("SELECT COUNT(DESCRIBA_DISCAPACIDAD) FROM USUARIO_DT_GNR WHERE DESCRIBA_DISCAPACIDAD != '' ")
				dato_discapacidad = self.cursor_discapacidad.fetchall()

				for discapacidad in dato_discapacidad:
					dato_de_discapacidad = discapacidad[0]
				if dato_de_discapacidad > 0:
					print(dato_de_discapacidad)
					dato_mostrar_discapacidad = str(dato_de_discapacidad)
					self.Cantidad_discapacidad.setText(dato_mostrar_discapacidad)
				else:
					print (dato_de_discapacidad)
					self.Cantidad_discapacidad.setText("0")
					"0"
						
					 #"0"
					

				#Si posee enfermedad
				self.cursor_enfermedad.execute("SELECT COUNT(DESCRIBA_ENFERMEDAD) FROM USUARIO_DT_GNR WHERE DESCRIBA_ENFERMEDAD != '' ")
				dato_enfermedad = self.cursor_enfermedad.fetchall()

				for enfermedad in dato_enfermedad:
					dato_de_enfermedad = enfermedad[0]
				if dato_de_enfermedad > 0:
					print(dato_de_enfermedad)
					datos_mostrar_enfermedad = str(dato_de_enfermedad)
					self.Cantidad_enfermedad.setText(datos_mostrar_enfermedad)
				else:
					print(dato_de_enfermedad)
					self.Cantidad_enfermedad.setText("0")
					"0"
					

				#Si esta en estado de embarazo
				self.cursor_enbarazo.execute("SELECT COUNT(EMBARAZADA) FROM USUARIO_DT_GNR WHERE EMBARAZADA = 'Si' ")
				dato_enbarazo = self.cursor_enbarazo.fetchall()

				for enbarazo in dato_enbarazo:
					dato_de_enbarazo = enbarazo[0]
				print(dato_de_enbarazo)
				datos_mostrar_embarazo = str(dato_de_enbarazo)
				self.Cantidad_embarazo.setText(datos_mostrar_embarazo)

				#Si esta en estado de lactante
				self.cursor_lactante.execute("SELECT COUNT(LACTANTE) FROM USUARIO_DT_GNR WHERE LACTANTE = 'Si' ")
				dato_lactante = self.cursor_lactante.fetchall()

				for lactante in dato_lactante:
					dato_de_lactante = lactante[0]
				print(dato_de_lactante)
				datos_mostrar_lactante = str(dato_de_lactante)
				self.Cantidad_lactante.setText(datos_mostrar_lactante)



			


					

				
			except Exception as e:
				print(e)
				QMessageBox.critical(self, "Error", "No se ha podido conectar a la base de datos o no existe la base de datos",
										 QMessageBox.Ok)				

		else:   
			QMessageBox.information(self, "Buscar usuario", "No se encontraron usuarios"
										"información.   ", QMessageBox.Ok)





	def realizar_operacion_1(self):		
		valor_1 = self.valor_1.text()
		valor_2 = self.valor_2.text()

		if not valor_1:
			self.valor_1.setFocus()
		elif not valor_2:
			self.valor_2.setFocus()
		else:

			operacion = (int(valor_1) * int(valor_2))
			division = (int(operacion) // 100)
			mostrar_resultado_1 = str(division)

			self.resultado_1.setText(mostrar_resultado_1)


	def realizar_operacion_2(self):		
		valor_1_2 = self.valor_1_2.text()
		valor_2_2 = self.valor_2_2.text()

		if not valor_1_2:
			self.valor_1_2.setFocus()
		elif not valor_2_2:
			self.valor_2_2.setFocus()
		else:

			operacion = (100 * int(valor_1_2))
			division = (int(operacion) // int(valor_2_2))
			mostrar_resultado_2= str(division)

			self.resultado_2.setText(mostrar_resultado_2 + "%")




	def Abrir_ventana(self):
		Window_status_user(self).exec_()

	def Editar_usuario(self):
		self.interface = Window_edit_elim_user()
		self.interface.show()
		#Window_editar_user(self).exec_()
	
	def Nuevo_user(self):
		Window_nv_users(self).exec_()

	def Abrir_window(self):
		Acerca_de(self).exec_()

	def Nv_vocero(self):
		Window_vocero(self).exec_()

	def closeEvent(self, event):
		
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de VESOR?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar VESOR?   ")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
            
		cerrar.exec_()
            
		if cerrar.clickedButton() == botonSalir:
			event.accept()
		else:
			event.ignore()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
#========================================== #Classes# ===================================================================


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()