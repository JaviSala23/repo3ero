#de la libreria PyQt5 importamos estos dos elem
from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem , QColor
from servidor.servidor import Servidor
import json
import ast
colores={
    "BLANCO":(255,255,255),
    "NEGRO":(0,0,0),
    "ROJO":(255,0,0),
    "VERDE":(0,255,0),
    "AZUL":(0,0,255),
    "ROSA":(255, 192, 203),
}
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
    def __init__(self, direccion):
        super().__init__(direccion)
        self.linea=0
        # Crear un temporizador para actualizar la lista
        self.timer = QTimer(self.formulario)
        self.timer.timeout.connect(self.recibir)
        self.timer.start(1000)  # Actualizar cada 1 segundo

        # Crear un modelo para la lista
        self.model = QStandardItemModel()
        self.formulario.chatList.setModel(self.model)
        
        
    def enviar(self,cliente):
        msj=self.formulario.msj.text()

        cliente.enviarMsj(msj)     
    def recibir(self):
        with open("chat.txt", "r") as archivo:
            lineas=archivo.readlines()
            cLineas=len(lineas)
            for i in range(self.linea,cLineas):
                
                lineaSplit=lineas[i].split("*/")
                colorPre = lineaSplit[0].replace("[", "").replace("]", "")

                color = [int(c) for c in colorPre.split(',')]
                if len(color) == 3:
                    r, g, b = color
                
                color_personalizado=QColor(r, g, b)
                item = QStandardItem(lineaSplit[1])
                item.setForeground(color_personalizado)
                self.model.appendRow(item)
               
            self.linea=cLineas

class crearCanal(InterfazVentana):
   
    nombre=""
    descripcion=""
    canal=""
    
    def crear(self):
        self.nombre=self.formulario.nombre.text()
        self.descripcion=self.formulario.descripcion.toPlainText()
        self.canal=Servidor(self.nombre,self.descripcion)
        self.canal.start() #ver mañana, todo
        self.ocultarVentana()
        print(self.canal)
    
class UnirCanal(InterfazVentana):
    
    nombre=""
        
    def unir():
        pass
    
class Perfil(InterfazVentana):
    nombre=""
    descripcion=""
    color=(0,0,0)
    
    
    def guardarPerfil(self):
        self.nombre=self.formulario.nombrePefil.text()
        self.descripcion=self.formulario.descripcionPerfil.text()
        self.color=colores[self.formulario.colores.currentText()]
        datos={
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "color":self.color
        }
        print(datos)
        
        # Abrir un archivo JSON en modo de escritura
        with open("chat/cliente/perfil.json", "w") as archivo_json:
            # Escribir el diccionario en el archivo JSON
            json.dump(datos, archivo_json)
        
        self.ocultarVentana()
    
    def leerPerfil(self):
        # Abrir un archivo JSON en modo de lectura
        with open("chat/cliente/perfil.json", "r") as archivo_json:
            # Cargar los datos desde el archivo JSON en un diccionario
            datos_cargados = json.load(archivo_json)

        # Ahora, los datos están en el diccionario "datos_cargados"
        print(datos_cargados['nombre'])
        self.nombre=self.formulario.nombrePefil.setText(datos_cargados['nombre'])
        self.descripcion=self.formulario.descripcionPerfil.setText(datos_cargados['descripcion'])
        
        for clave, valor in colores.items():
            if valor==tuple(datos_cargados['color']):
                self.formulario.colores.setCurrentText(clave)
                
        estilo="background-color:rgb"+str(tuple(datos_cargados['color']))+";border-color: rgb(255, 255, 255);border-style:solid;border-width:1px"
        
        self.formulario.colormuestra.setStyleSheet(estilo)
        
        self.mostrarVentana()
    
    def cambiarColorCuadro(self):
        color=colores[self.formulario.colores.currentText()]
        self.formulario.colormuestra.setStyleSheet("background-color:rgb"+str(color)+";border-color: rgb(255, 255, 255);border-style:solid;border-width:1px")
        
        
        
class Chat(InterfazVentana):
    
    nombreCanal=""
    
    
class UnirCanal(InterfazVentana):
    
    ip=""
    
    def aceptarCanal(self,cliente):
        self.ip=self.formulario.ip.text()
        cliente.canal=(self.ip,4000)
        cliente.start()
        self.ocultarVentana()
        return cliente
        
    

        
        
