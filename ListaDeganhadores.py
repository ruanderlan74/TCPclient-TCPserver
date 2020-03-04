from datetime import date
from datetime import datetime
class lista:

    def __init__(self):
       self.jogador = ""
       

    def setJogador(self, msg, msgjogo):
        self.data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = self.data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        self.jogador = str(self.jogador) + data_e_hora_em_texto+ str(' ---->  ')+ str(msg) + str(' ')+ str(msgjogo) + str('\n')
        print(self.jogador)
        
    def getListJogador(self):
        return self.jogador
