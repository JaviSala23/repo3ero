from interfaz import *


#creamos aplicacion QtWidegets
aplicacion=QtWidgets.QApplication([]) 

#Creacion de objetos (Ventanas) de intefaz
principal=ventanaPrincipal('chat/cliente/interfaz/principal.ui')
crearCanal1=crearCanal('chat/cliente/interfaz/crearcanal.ui')




#apertura de ventana principal
principal.mostrarVentana()
#definimos los botones de la pantalla principal directamente en el archivo principal
principal.formulario.Crear_Canal.triggered.connect(crearCanal1.mostrarVentana)


#Conecto los botones de crear Canal
crearCanal1.formulario.cancelar.clicked.connect(crearCanal1.ocultarVentana)
crearCanal1.formulario.crear.clicked.connect(crearCanal1.crear)





aplicacion.exec()