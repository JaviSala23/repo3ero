import socket
import sys
from netifaces import interfaces, ifaddresses, AF_INET
from PyQt5.QtCore import QThread, pyqtSignal

class Servidor(QThread):
    # Define una señal llamada mensaje_recibido que emite cadenas (str)
    mensaje_recibido = pyqtSignal(str)  # Señal para emitir mensajes recibidos

    # Constructor de la clase Servidor, recibe nombre y descripción como parámetros
    def __init__(self, nombre, descripcion):
        super().__init__()  # Llama al constructor de la clase base QThread
        self.protocolo = (socket.AF_INET, socket.SOCK_STREAM)  # Configura el protocolo de socket
        self.anfitrion = ""  # Inicializa la dirección IP del anfitrión
        self.puerto = 4000  # Puerto en el que escuchará el servidor
        self.tamBuffer = 1024  # Tamaño del búfer para recibir datos
        self.clientes = []  # Lista de conexiones de clientes
        self.nombre = nombre  # Nombre del servidor
        self.descripcion = descripcion  # Descripción del servidor

    # Método run que se ejecutará cuando se inicie el hilo del servidor
    def run(self):
        try:
            # Obtiene la dirección IP del anfitrión
            for ifaceName in interfaces():
                addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
                ip = addresses
            print(self.anfitrion)
            print(self.nombre, self.descripcion)

            # Crea un socket y lo enlaza a la dirección IP y puerto
            self.enlace = socket.socket(self.protocolo[0], self.protocolo[1])
            self.enlace.bind((self.anfitrion, int(self.puerto)))

            while True:
                self.enlace.listen(3)  # Escucha hasta 3 conexiones entrantes
                cliente, direccion_cliente = self.enlace.accept()
                print("%s:%s se ha conectado." % direccion_cliente)
                cliente.send(bytes("Bienvenido al chat", "utf-8"))

                # Agrega el cliente a la lista de conexiones
                self.clientes.append(cliente)

                # Inicia un hilo para manejar al cliente
                cliente_thread = ClienteHilo(cliente, self, self.tamBuffer)
                cliente_thread.start()

        except Exception as e:
            print("Error en el servidor:", e)
            return False



    # Método para eliminar un cliente de la lista de conexiones
    def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            cliente.close()

    # Método para enviar un mensaje a todos los clientes conectados
    def broadcast(self, msj, prefix=""):
        for cliente in self.clientes:
            try:
                cliente.send(bytes(prefix + msj, 'utf-8'))
            except:
                # Si hay un error al enviar el mensaje, elimina el cliente de la lista
                self.eliminar_cliente(cliente)

class ClienteHilo(QThread):
    # Constructor de la clase, recibe el cliente, el servidor y el tamaño del búfer
    def __init__(self, cliente, servidor, tamBuffer):
        super().__init__()  # Llama al constructor de la clase base QThread
        self.cliente = cliente  # Almacena la referencia al cliente que este hilo manejará
        self.servidor = servidor  # Almacena la referencia al servidor
        self.tamBuffer = tamBuffer  # Tamaño del búfer para recibir datos

    # Método run que se ejecutará cuando se inicie este hilo
    def run(self):
        nombre = self.cliente.recv(self.tamBuffer).decode("utf8")  # Recibe el nombre del cliente
        msjBienvenda = 'Bienvenido %s! Si quiere salir escriba {quit} .' % nombre
        self.cliente.send(bytes(msjBienvenda, 'utf-8'))  # Envía un mensaje de bienvenida al cliente
        msj = "%s se ha unido al chat!" % nombre
        self.servidor.broadcast(msj)  # Envía un mensaje de unión del cliente al servidor para ser transmitido a todos

        while True:
            msj = self.cliente.recv(self.tamBuffer)  # Recibe un mensaje del cliente

            if msj != bytes("{quit}", 'utf-8'):
                msj = msj.decode('utf-8')
                self.servidor.mensaje_recibido.emit(nombre + ": " + msj)  # Emite el mensaje recibido al servidor
                self.servidor.broadcast(msj, nombre + ": ")  # Transmite el mensaje a todos los clientes
            else:
                self.cliente.send(bytes("{quit}", 'utf-8'))  # Envia un mensaje de salida al cliente
                self.servidor.eliminar_cliente(self.cliente)  # Llama al método del servidor para eliminar al cliente
                break