from socket import *

serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("Сервер работает!")
while 1:
    Byte_ask, clientAdress = serverSocket.recvfrom(2048)
    ask = str(Byte_ask, encoding = "utf-8")
    answer = bytearray(("Сервер отвечает тебе: "+ask), encoding="utf-8")
    serverSocket.sendto(answer, (clientAdress))

