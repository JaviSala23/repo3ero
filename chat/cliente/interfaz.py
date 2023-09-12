#de la libreria PyQt5 importamos estos dos elem
from PyQt5 import uic,QtWidgets

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
        pass
    
class UnirCanal(InterfazVentana):
    
    nombre=""
        
    def unir():
        pass
    
        
        
        
