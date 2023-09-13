#de la libreria PyQt5 importamos estos dos elem
from PyQt5 import uic,QtWidgets
from servidor.servidor import Servidor

class InterfazVentana:
    def __init__(self,direccion):
        self.formulario=uic.loadUi(direccion)
    
        
    def mostrarVentana(self):
        #motrar formulario
        self.formulario.show()
    
    def ocultarVentana(self):
        #motrar formulario
        self.formulario.hide()
        

class ventanaPrincipal(InterfazVentana):
    
    def enviar():
        pass
    def recibir():
        pass

class crearCanal(InterfazVentana):
   
    nombre=""
    descripcion=""
    
    def crear(self):
        self.nombre=self.formulario.nombre.text()
        self.descripcion=self.formulario.descripcion.toPlainText()
        canal1=Servidor(self.nombre,self.descripcion)
        canal1.crearCanal()
        self.ocultarVentana()
    
class UnirCanal(InterfazVentana):
    
    nombre=""
        
    def unir():
        pass
    
        
        
        
