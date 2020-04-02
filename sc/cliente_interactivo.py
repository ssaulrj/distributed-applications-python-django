import sys, os
from socket import *
# Establece el nombre y el puerto del servidor (serán dos parámetros
# pasados por la línea de comandos).
if(len(sys.argv) > 2):
    server_name=sys.argv[1]
    server_port = int(sys.argv[2])
else:
    print ("Uso: python cliente_interactivo server_name server_port")
    sys.exit(1)
# Obtiene la dirección IP correspondiente al servidor.
server_address = gethostbyname(server_name)
# Crea un socket.
connection_socket = socket(AF_INET,SOCK_STREAM)
# Conecta el socket al servidor.
connection_socket.connect((server_address, server_port))
# El actual proceso se divide en dos:
# 1. Proceso padre: se encarga de leer los mensajes procedentes del
# servidor y de imprimirlos en pantalla
# 2. Proceso hijo: recoge mensajes de la entrada estándar y los envía al
# servidor
pid = os.fork()
if pid != 0:
    # Entrando en el proceso padre
    # Permite leer del socket como si de un fichero se tratase.
    incoming_stream = connection_socket.makefile("r")
    print ("El cliente acepta mensajes del servidor")
    # Se entra en un bucle: cada vez que el servidor envía un mensaje lo
    # imprimimos
    # Si el mensaje es salir el servidor quiere desconectarse por lo que
    # el cliente no aceptará más mensajes
    while True:
        msg = incoming_stream.readline()
        print (msg)
        if msg == "salir\n":
            break
    # Se cierran los sockets
    incoming_stream.close()
    connection_socket.close()
    print ("Servidor desconectado. Si no está desconectado escriba salir")
    os.waitpid(pid, 0)
else:
    # Entrando en el proceso hijo
    # Permite escribir en el socket como si de un fichero se tratase.
    outgoing_stream = connection_socket.makefile("w")
    print ("El cliente permite mandar mensajes al servidor")
    # Se entra en un bucle: se lee de la entrada estándar (teclado) los
    # mensajes y se envían al servidor. Para desconectar escribimos salir
    while True:
        msg = raw_input()
        outgoing_stream.write(msg + "\n")
        outgoing_stream.flush()
        if msg == "salir":
            break
    # Se cierran los sockets .
    outgoing_stream.close()
    connection_socket.close()
    # Fin del proceso hijo
    sys.exit(0)

