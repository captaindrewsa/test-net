from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("Сервер готов!")
while 1:
    connectionSocket, clientAdress = serverSocket.accept()
    Byte_ask = connectionSocket.recv(1024)
    connectionSocket.send(Byte_ask)
    connectionSocket.close()
