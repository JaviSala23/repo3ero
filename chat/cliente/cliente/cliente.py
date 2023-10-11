import socket
from PyQt5.QtCore import QThread, pyqtSignal

class Cliente(QThread):
    mensaje_recibido = pyqtSignal(str)
    protocolo = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    def __init__(self,nombre,descripcion,color=(0,0,0)):
        super().__init__()
        self.nombre=nombre
        self.decripcion=descripcion
        self.color=color
        self.canal=("",0)
        
    def run(self):
        # Conectar al servidor
        self.protocolo.connect(self.canal)
        self.protocolo.send(bytes(f'{self.color} - {self.nombre}', 'utf-8'))
        # Abre un archivo en modo de escritura ('w' para escribir).
        with open("chat.txt", "w") as archivo:
            archivo.write(f"{self.color} */ Se ha conectado al chat con ip: {self.canal[0]}\n")
            
            
        
        # Comunicación con el servidor
        while True:
            # Recibir y mostrar la respuesta del servidor
            respuesta = self.protocolo.recv(1024).decode('utf-8')
            with open("chat.txt", "a") as archivo:
                archivo.write(respuesta+"\n")
                
    def enviarMsj(self,mesj):
        self.protocolo.send(bytes(mesj, 'utf-8'))
    