from socket import *
import random
class Historia:
	
	def __init__(self,i):
		inicializa = i;		

	def gh(self,randNumero):
		StirngHis = ''
		if randNumero == 1:
			StirngHis = '???????????????????????????????????????????'
			pass
		elif randNumero == 2:
			StirngHis = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
			pass
		elif randNumero == 3:
			StirngHis = '0000000000000000000000000000000000000000000'
		return StirngHis
	
	def pergh(self,randNumero,cont):
		StirngPerg = ''
		if randNumero == 1:
			if cont == 0:
				StirngPerg = 'perg\na)h\nb)c\nc)f\n'
				pass 
			pass 
		return StirngPerg

#import Historia 
serverPort = 7897
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
historia = Historia(1)
cont = 0
while True:
    #cria o socket pro cliente e estabelece a conexão
   
    connectionSocket, addr = serverSocket.accept() 
    print('conexão', addr)
    length_of_message = int.from_bytes(connectionSocket.recv(2), byteorder='big')
    sentence = connectionSocket.recv(length_of_message).decode("UTF-8")
    print(sentence)
    randNumero = random.randint(1,3)
    print(randNumero)
    hist = historia.gh(randNumero)
    hist += "\r\n"
    print(hist)
    connectionSocket.send(len(hist.encode("UTF-8")).to_bytes(2, byteorder='big'))
    connectionSocket.send(hist.encode("UTF-8")
    print("oi")