from socket import *
serverPort = 7897
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    #cria o socket pro cliente e estabelece a conexão
    connectionSocket, addr = serverSocket.accept()
    
    print('conexão', addr)

    length_of_message = int.from_bytes(connectionSocket.recv(2), byteorder='big')
    sentence = connectionSocket.recv(length_of_message).decode("UTF-8")
    
     
    print(sentence)
    
    connectionSocket.send(sentence)
    
    connectionSocket.close()