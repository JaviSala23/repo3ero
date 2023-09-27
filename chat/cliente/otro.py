import socket

# Configuración del servidor al que el cliente se conectará
host = '10.16.154.51'  # Reemplaza con la dirección IP del servidor
puerto = 4000  # Reemplaza con el puerto en el que el servidor está escuchando

# Crear un socket para el cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
cliente.connect((host, puerto))
print("Conexión establecida con el servidor")

# Comunicación con el servidor
while True:
    mensaje = input("Escribe tu mensaje (o 'salir' para salir): ")

    # Enviar el mensaje al servidor
    cliente.send(bytes(mensaje, 'utf-8'))

    if mensaje.lower() == 'salir':
        break

    # Recibir y mostrar la respuesta del servidor
    respuesta = cliente.recv(1024).decode('utf-8')
    print("Respuesta del servidor:", respuesta)

# Cerrar la conexión
cliente.close()
