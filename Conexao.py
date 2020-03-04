from socket import *
import json
class conexao:
	global msg
	global msgJson

	def __init__(self,serverPort,serverHost):
		self.PortServer = serverPort
		self.HostServer = ''
		self.serverSocket = socket(AF_INET, SOCK_STREAM)
		self.serverSocket.bind((self.HostServer,self.PortServer))
		self.serverSocket.listen(5)
		pass

	def read(self,conn):
		g = ''
		h = ''
		msgJson = str()
		length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
		self.msgJson = conn.recv(length_of_message).decode("UTF-8")
		self.msg = json.loads(self.msgJson)
		print(self.msg)
		if self.msg["messageType"] == 0 and self.msg["objectReference"] == 'Historia': 		
			g = self.msg["arrguments"]
			h = self.msg["methodid"]
		else:
			h = 'Erro'
		return g,h
			
	def send(self,msg,conn):
		self.msg["arrguments"] = msg
		self.msg["messageType"] = 1	
		self.msgJson = json.dumps(self.msg)
		print(self.msgJson)
		conn.send(len(self.msgJson.encode("UTF-8")).to_bytes(2, byteorder='big'))
		conn.send(self.msgJson.encode("UTF-8"))

