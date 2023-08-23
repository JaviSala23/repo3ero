from .basedatos import BaseDatos
import sqlite3

class Cliente:
    def __init__(self):
        self.id=""
        self.nombre="" 
        self.contrasena="" 
        self.email="" 
        self.telefono= "" 
        self.calle="" 
        self.numero="" 
        self.localidad="" 
        self.provincia="" 
        self.pais=""
        self.dni=""
        self.fechaNacimiento=""     
    
    def crearClientes(self):   
        base = BaseDatos()
        base.conectar()
        conBD=sqlite3.connect(base.bd)
        cursor = conBD.cursor()
        sentencia="""
        CREATE TABLE IF NOT EXISTS Clientes 
        ( id INTEGER,
        nombre VARCHAR(128), 
        contraseña VARCHAR(128),
        email VARCHAR(128),
        telefono VARCHAR(15),
        calle VARCHAR(15),
        numero INTEGER,
        localidad VARCHAR(128),
        provincia VARCHAR(128),
        pais VARCHAR(128),
        dni INTEGER
        )
        """
        cursor.execute(sentencia)
        conBD.close()
        del base
    
    def nuevoCliente(self):
        base = BaseDatos()
        sentencia=f"""INSERT INTO Clientes 
                VALUES 
                ({self.id},'{self.nombre}','{self.contrasena}',
                '{self.email}','{self.telefono}',
            '{self.calle}',{self.numero},
                '{self.localidad}','{self.provincia}',
                '{self.pais}',{self.dni});       
                """
        base.actualizarBD(sentencia)
        del base
    
    def consultarUltimoCliente(self):
        base= BaseDatos()
        sentencia="SELECT * FROM Clientes ORDER BY id DESC LIMIT 1"
        registro=base.consultar(sentencia,cantidad=1)
        return registro
    
    def consultarPrimerCliente(self):
        base=BaseDatos()
        sentencia="SELECT * FROM Clientes ORDER BY id LIMIT 1"
        registro=base.consultar(sentencia,cantidad=1)
        return registro 
    
    def consultarUnCliente(self):
        base= BaseDatos()
        sentencia=f"SELECT * FROM Clientes WHERE id={self.id}"
        registro=base.consultar(sentencia,cantidad=1)
        return registro
    
    def actualizarClientes(self):
        base = BaseDatos()
        sentencia=f"""UPDATE Clientes 
                SET
                id={self.id},
                nombre='{self.nombre}', 
                contraseña='{self.contrasena}',
                email='{self.email}',
                telefono='{self.telefono}',
                calle='{self.calle}',
                numero={self.numero},
                localidad='{self.localidad}',
                provincia='{self.provincia}',
                pais='{self.pais}',
                dni={self.dni}  
                WHERE id={self.id};
                """
        base.actualizarBD(sentencia)
        del base
    
    def eliminarCliente(self):
        base = BaseDatos()
        sentencia=f"""DELETE FROM Clientes
                    WHERE id={self.id};
        """
        base.actualizarBD(sentencia)
        del base
               
                
       
