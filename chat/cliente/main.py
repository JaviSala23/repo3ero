from interfaz import *




#creamos aplicacion QtWidegets
aplicacion=QtWidgets.QApplication([]) 

#Creacion de objetos (Ventanas) de intefaz
principal=ventanaPrincipal('chat/cliente/interfaz/principal.ui')
crearCanal1=crearCanal('chat/cliente/interfaz/crearcanal.ui')
modificarPerfil=Perfil('chat/cliente/interfaz/perfil.ui')
ventanaChat=Chat('chat/cliente/interfaz/chat.ui')
unircanal1=UnirCanal




#apertura de ventana principal
principal.mostrarVentana()
#definimos los botones de la pantalla principal directamente en el archivo principal
principal.formulario.Crear_Canal.triggered.connect(crearCanal1.mostrarVentana)
principal.formulario.actionModificar_Perfil.triggered.connect(modificarPerfil.leerPerfil)
principal.formulario.actionventanaChat.triggered.connect(ventanaChat.mostrarVentana)


#Conecto los botones de crear Canal
crearCanal1.formulario.cancelar.clicked.connect(crearCanal1.ocultarVentana)
crearCanal1.formulario.crear.clicked.connect(crearCanal1.crear)

#Conecto los botones de midificarPefil
'''
modificarPerfil.formulario.Aceptar.clicked.connect(modificarPerfil.guardarPerfil)
modificarPerfil.formulario.Cancelar.clicked.connect(modificarPerfil.ocultarVentana)
modificarPerfil.formulario.colores.activated.connect(modificarPerfil.cambiarColorCuadro)
'''
aplicacion.exec()