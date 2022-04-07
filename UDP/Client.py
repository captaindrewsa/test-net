from socket import *

serverAdress = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:    
    Byte_message = bytearray(input("Введите сообщение: "), encoding="utf-8")
    clientSocket.sendto(Byte_message, (serverAdress, serverPort))
    answer, serverAdress = clientSocket.recvfrom(2048)
    print(str(answer, encoding="utf-8"))
clientSocket.close()
