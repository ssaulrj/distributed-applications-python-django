import sys, os
from socket import *
# Establece el nombre y el puerto del servidor (serán dos parámetros
# pasados por la línea de comandos).
if(len(sys.argv) > 2):
    server_name=sys.argv[1]
    server_port = int(sys.argv[2])
else:
    print("Uso: python cliente_basico server_name server_port")
    sys.exit(1)
# Obtiene la dirección IP correspondiente al servidor.
server_address = gethostbyname(server_name)
# Crea un socket.
connection_socket = socket(AF_INET,SOCK_STREAM)
# Conecta el socket al servidor.
connection_socket.connect((server_address, server_port))
# Crea los ficheros asociados con el socket. Permite leer y escribir del
# socket como si de un fichero se tratase.
incoming_stream = connection_socket.makefile("r")
outgoing_stream = connection_socket.makefile("w")
# Ahora el cliente puede comunicarse con el servidor.
# Lee la hora y la imprime en la salida estándar (monitor).
print(incoming_stream.read())
# Cierra la conexión y termina
incoming_stream.close()
outgoing_stream.close()
connection_socket.close()
