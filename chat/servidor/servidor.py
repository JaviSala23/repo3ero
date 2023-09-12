import socket
from netifaces import interfaces, ifaddresses, AF_INET
from threading import Thread

class Servidor():
    def __init__(self):
        self.protocolo=(socket.AF_INET, socket.SOCK_STREAM)
        self.anfitrion=""
        self.puerto=4000
        self.tamBuffer=1024
        self.enlase=""
        self.nombre=""
        self.direcciones={} #guarda la conexiones del canal
        
    def crearCanal(self):
        try:
            for ifaceName in interfaces():
                addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
                ip=addresses
            self.anfitrion=ip[0]
            print(self.anfitrion)
            self.enlase = socket.socket(self.protocolo[0],self.protocolo[1])
            self.enlase.bind((self.anfitrion, int(self.puerto)))
            return True
        except:
            return False
        
           
    def gestConEntr(self):
        while True:
            cliente, direccion_cliente = self.enlase.accept()
            print("%s:%s se ha conectado." % direccion_cliente)
            cliente.send(bytes("Bienvendio a el chat","utf-8"))
            self.direcciones[cliente] = direccion_cliente
            Thread(target=self.manejoCliente, args=(cliente,)).start()
        
    
    def manejoCliente(self,cliente):
        nombre = cliente.recv(self.tamBuffer).decode("utf8")
        msjBienvenda = 'Bienvendio %s! Si quiere salir escriba {quit} .' % nombre
        cliente.send(bytes(msjBienvenda,'utf-8'))
        msj = "%s se ha unido al chat!" % nombre
        self.broadcast(msj)
        self.direcciones[cliente] = nombre

        while True:
            msj = cliente.recv(self.tamBuffer)
            
            if msj != bytes("{quit}",'utf-8'):
                    msj=msj.decode('utf-8')
                    print(nombre+":"+ msj)
                    self.broadcast(msj,nombre+": ")
            else:
                cliente.send(bytes("{quit}"))
                cliente.close()
                del self.direcciones[cliente]
                self.broadcast("%s ha dejado el chat." % nombre.endswith())
                break
                
    
    def broadcast(self,msj, prefix=""):
        for sock in self.direcciones:
            sock.send(bytes(prefix+msj,'utf-8'))
        
    

