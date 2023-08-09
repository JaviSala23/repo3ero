import sqlite3

class BaseDatos():
    def __init__(self):
        self.bd="practicasConBD/gestion.sqlite" 
        self.conexion=""
        self.cursor=""
        
    def conectar(self):
       self.conexion=sqlite3.connect(self.bd)
       self.cursor = self.conexion.cursor() 
    
    def actualizarBD(self,argumento):
        self.conectar()
        self.cursor.execute(argumento)
        self.conexion.commit()
        self.conexion.close()
    
    def consultar(self,argumento,cantidad=0):
        self.conectar()
        datos=self.cursor.execute(argumento)
        if cantidad ==1:
            fila=datos.fetchone()
            return fila
        else:
            fila=datos.fetchall()
            return fila
            

        
        
        