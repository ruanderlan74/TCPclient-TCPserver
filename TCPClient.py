from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

#three-way handshaking
clientSocket.connect((serverName, serverPort))

sentence = input('1 - Gerar Historia \n 2 - Sair\n')

if sentence=="1":
	gera = True;
    clientSocket.send(gera.encode())
elif sentence=="2":
    

sentence = input('Gerar Historia')

#não precisa indica ip e porta porque isso já foi decidido no estabelecimento de conexão
clientSocket.send(sentence.encode())
receivedSentence = clientSocket.recv(1024)
print('From Server: ', receivedSentence.decode())
clientSocket.close()
