from socket import *
import random
import json
from Historia import Historia
from Conexao import	conexao
from ListaDeganhadores import lista
	

#import Historia 
s = conexao(8888,'localhost')

print('The server is ready to receive')
historia = Historia(1)
Lg = lista()
cont = 0
while True:
    #cria o socket pro cliente e estabelece a conexão
	print("oi2")
	connection, addr = s.serverSocket.accept() 
	print('conexão', addr)
	randNumero, metodo = s.read(connection)	
	if metodo == 'GerarHistoria':
		print(randNumero)
		hist = historia.gh(randNumero)
		hist += "\r\n"
		print(hist)
		s.send(hist,connection)
		ok = s.read(connection)
		while True:	
			perg = historia.pergh(randNumero,cont)
			perg += "\r\n"
			print(perg)
			s.send(perg,connection)
			resposta, ok = s.read(connection)
			print(resposta)
			result = historia.acertoEerro(randNumero,cont,resposta)
			result += "\r\n"
			
			print(result)
			print(cont)
			s.send(result,connection)
			if cont == 4:
				NomeGanhador, ok = s.read(connection)
				print(NomeGanhador, ok )
				Lg.setJogador(NomeGanhador,ok)
				break
			cont = cont + 1
		cont = 0
		print("oi")		
		connection.close()
		pass	
	elif metodo == 'ListaDeGanhadores':
		msg = Lg.getListJogador()
		s.send(msg,connection)
		connection.close()
		pass
	elif metodo == 'Erro':
		pass

print('conexão FECHADA')
    #connectionSocket.send(len(sentence.encode("UTF-8")).to_bytes(2, byteorder='big'))
    #connectionSocket.send(sentence.encode("UTF-8"))
    #connectionSocket.close()
