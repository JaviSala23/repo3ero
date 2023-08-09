from clases.basedatos import BaseDatos

base = BaseDatos()
base.conectar()
sentencia="""
 CREATE TABLE IF NOT EXISTS Clientes 
( id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre VARCHAR(128), 
contraseña VARCHAR(128),
email VARCHAR(128),
telefono VARCHAR(15),
calle VARCHAR(15),
numero INTEGER,
localidad VARCHAR(128)
provincia VARCHAR(128)
pais VARCHAR(128),
dni INTEGETR,
fechaNacimiento DATE
)
"""
base.actualizarBD(sentencia)