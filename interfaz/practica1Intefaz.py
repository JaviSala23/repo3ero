#de la libreria PyQt5 importamos estos dos elem
from PyQt5 import QtWidgets, uic  

#creamos aplicacion QtWidegets
aplicacion=QtWidgets.QApplication([]) 

#clase que maneja la interfaz grafica
class InterfazGrafica: 
    #funcion constructora.
    def __init__(self):
        #atributo es el formulario generado en qt designer
        self.formulario=uic.loadUi('interfaz/practica1.ui') 
        
    def contar(self):
        #guardo en texto1 el contenido de mi line edit (cajaTexto1)
        texto1=self.formulario.cajaTexto1.text()
        #guardo en texto1 el contenido de mi line edit (cajaTexto2)
        letraAcontar=self.formulario.cajaTexto2.text()
        #cuento cuantas letras / palabras / o caracteres concatendados y ordenados
        cantidad=texto1.count(letraAcontar)
        #inserto la cantidad con un mensaje que dice resultado a mi label (resultado)
        self.formulario.resultado.text(f"Resultado: '{cantidad}'")
        
       
    
    #funcion para conectar los botones, y mostrar el formulario    
    def mostrarFormulario(self):
        #conectar el boton con una funcion (evento click)
        self.formulario.traer.clicked.connect(self.contar)
        self.formulario.show()
        
