import socket
from PyQt5.QtCore import QThread, pyqtSignal

class Cliente(QThread):
    def __init__(self,nombre,descripcion,color=(0,0,0)):
        super().__init__()
        self.nombre=nombre
        self.decripcion=descripcion
        self.color=color
        self.canal=(0,0)
    
    def run(self):
        canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar al servidor
        canal.connect(self.canal)
        print("Conexión establecida con el servidor")
        # Comunicación con el servidor
        while True:
            # Recibir y mostrar la respuesta del servidor
            respuesta = canal.recv(1024).decode('utf-8')
            print("Respuesta del servidor:", respuesta)
