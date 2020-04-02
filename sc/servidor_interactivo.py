import sys, os
from socket import *
# Establece el puerto en el que va a escuchar el servidor (será un
# parámetro pasado por la línea de comandos).
if(len(sys.argv) > 1):
    port = int(sys.argv[1])
else:
    print ("Uso: python servidor_interactivo server_port")
    sys.exit(1)
# Crea un socket para escuchar en espera de nuevas conexiones.
listening_socket = socket(AF_INET,SOCK_STREAM)
# Conecta el socket a un puerto en el que escuchar. Sólo root puede
# escuchar en puertos por debajo de 1024.
listening_socket.bind(('', port))
# Dice al socket que comience a escuchar. El argumento es el número máximo
# de conexiones permitidas. Sólo se atiende una cada vez.
listening_socket.listen(1)
# Un socket que escucha sólo sirve para escuchar.
# Espera a que haya una conexión y la acepta.
# Cuando se establece una conexión se crea un nuevo socket para el
# intercambio de información.
accepted_socket, address = listening_socket.accept()
# El actual proceso se divide en dos:
# 1. Proceso padre: se encarga de leer los mensajes procedentes del cliente
# y de imprimirlos en pantalla
# 2. Proceso hijo: recoge mensajes de la entrada estándar y los envía al
# cliente
pid = os.fork()
if pid != 0:
    # Entrando en el proceso padre
    # Cerrar el socket de escucha
    listening_socket.close()
    # Permite leer del socket como si de un fichero se tratase.
    incoming_stream = accepted_socket.makefile("r")
    print ("El servidor acepta mensajes del cliente")
    # Se entra en un bucle: cada vez que el cliente envía un mensaje lo
    # imprimimos
    # Si el mensaje es salir el cliente quiere desconectarse por lo que
    # el servidor no aceptará más mensajes
    while True:
        msg = incoming_stream.readline()
        print (msg)
        if msg == "salir\n":
            break
    # Se cierran los sockets
    incoming_stream.close()
    accepted_socket.close()
    print ("Cliente desconectado. Si no está desconectado escriba salir")
    os.waitpid(pid, 0)
else:
    # Entrando en el proceso hijo
    # Cerrar el socket de escucha
    listening_socket.close()
    # Permite escribir en el socket como si de un fichero se tratase.
    outgoing_stream = accepted_socket.makefile("w")
    print ("El servidor permite mandar mensajes al cliente")
    # Se entra en un bucle: se lee de la entrada estándar (teclado) los
    # mensajes y se envían al cliente. Para desconectar escribimos salir
    while True:
        msg = raw_input()
        outgoing_stream.write(msg + "\n")
        outgoing_stream.flush()
        if msg == "salir":
            break
    # Se cierran los sockets
    outgoing_stream.close()
    accepted_socket.close()
    # Fin del proceso hijo
    sys.exit(0)
