from socket import *

serverAdress = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAdress, serverPort))
Byte_message = bytearray(input("Введите сообщение: "),encoding="utf-8")
clientSocket.send(Byte_message)
answer = str(clientSocket.recv(1024),encoding="utf-8")
print("Сервер ответил: ", answer)
clientSocket.close()

