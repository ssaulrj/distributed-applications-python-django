import sys, os
from socket import *
from time import *
# Establece el puerto en el que va a escuchar el servidor (será un
# parámetro pasado por la línea de comandos).
if(len(sys.argv) > 1):
    port = int(sys.argv[1])
else:
    print("Uso: python servidor_basico server_port")
    sys.exit(1)
# Crea un socket para escuchar en espera de nuevas conexiones.
listening_socket = socket(AF_INET,SOCK_STREAM)
# Conecta el socket a un puerto en el que escuchar. Sólo root puede
# escuchar en puertos por debajo de 1024.
listening_socket.bind(('', port))
# Dice al socket que comience a escuchar. El argumento es el número
# máximo de conexiones permitidas. Sólo se atiende una cada vez.
listening_socket.listen(1)
# Un socket que escucha sólo sirve para escuchar. Cuando se establece una
# conexión se crea un nuevo socket para el intercambio de información.
while 1:
    # Espera a que haya una conexión y la acepta.
    accepted_socket, address = listening_socket.accept()
    # Al aceptar una conexión se crea un nuevo socket de forma que el
    # servidor puede seguir escuchando en el socket de escucha en espera
    # de nuevas conexiones. En nuestro caso, se muestra un mensaje, se
    # cierra la conexión y se espera una nueva conexión.
    # Crea los ficheros asociados con el socket. Permite leer y escribir
    # del socket como si de un fichero se tratase.
    incoming_stream = accepted_socket.makefile("r")
    outgoing_stream = accepted_socket.makefile("w")
    # Crea un texto con la hora local.
    local_time = ctime()
    # Envía la hora al cliente
    outgoing_stream.write(local_time + "\n")
    # Deja un registro de la conexión del cliente
    print("Conexión desde", address, "en", local_time)
    # Cierra la conexión y repite el bucle
    incoming_stream.close()
    outgoing_stream.close()
    accepted_socket.close()

