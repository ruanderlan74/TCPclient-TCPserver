class Historia:
	
	def __init__(self,i):
		inicializa = i;		

	def gh(self,randNumero):
		# A Historia inicial que deve ser contada.
		# então tu faz if elif para cada historia e só muda o valor da variavel randNumero
		StirngHis = ''
		if randNumero == '1':
			StirngHis = '???????????????????????????????????????????'
			pass
		elif randNumero == '2':
			StirngHis = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
			pass
		elif randNumero == '3':
			StirngHis = '0000000000000000000000000000000000000000000'
		return StirngHis
	
	def pergh(self,randNumero,cont):
		#aqui é a parte das perguntas, cada numero do randNumero que é uma historia tem dentro do seu if as perguntas
		# e dentro dele vai ter os cinco if's que é no caso cada pergunta e mais um pra ele selecionar qual é a historia certa.   
		StirngPerg = ''
		if randNumero == '1':
			if cont == 0:
				StirngPerg = '\na)h\nb)c\nc)f\n'
			if cont == 1:
				StirngPerg = 'a)historiaA\nb)historiaB\nc)historiaC'		
		return StirngPerg
	def acertoEerro(self,randNumero,cont,resposta):
		#aqui é a resposta de cada pergunta tipo acho que tu já pegou a ideia, tipo dentro do randNumero de cada historia
		#dentro do 'cont' de cada pergunta tem que ter um if com a resposta certa e o caso errado e caso onde ele acerta a historia 
		StringAcerto = ''
		if randNumero == '1':
			if cont == 0:
				if resposta == 'a':
					StringAcerto = 'Resposta Correta'
				else:
					StringAcerto = 'Resposta Errada'
			if cont == 1:
				if resposta == 'a':
					StringAcerto = 'Ganhou'
				else:
					StringAcerto = 'Perdeu'		
		return StringAcerto
