import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creamos el socket

mysock.connect(("data.pr4e.org", 80)) # nos conectamos con el socket a la pagina data.pr4e.org a traves del puerto HTTP (80)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Creamos el comando que queremos enviarle al servidor a traves del socket

mysock.send(cmd) #Enviamos el comando

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close()