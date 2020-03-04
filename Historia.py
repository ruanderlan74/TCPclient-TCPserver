class Historia:
	
	def __init__(self,i):
		inicializa = i;		

	def gh(self,randNumero):
		# A Historia inicial que deve ser contada.
		# então tu faz if elif para cada historia e só muda o valor da variavel randNumero
		StirngHis = ''
		if randNumero == '1':
			StirngHis = 'Pergunta:"Um homem entra num restaurante e pede uma sopa de gaivota ele prova a sopa, pega uma faca e se mata."'
			pass
		elif randNumero == '2':
			StirngHis = 'Pergunta: "Um homem faz uma viagem de trem até a capital, voltando alguns dias depois. No meio da viagem de volta, ele se mata"'
			pass
		elif randNumero == '3':
			StirngHis = 'Pergunta: "Uma mulher entra num bar vazio e pede uma bebida ao homem no balcão, ele a mata imediatamente a tiros."'	
		elif randNumero == '4':
			StirngHis = 'Pergunta: "A mulher acordou durante a noite, viu uma sobra e alguns momentos depois se matou."'
		elif randNumero == '5':
			StirngHis = 'Pergunta: "A mulher assassinou friamente a familia inteira"'
		return StirngHis
	
	def pergh(self,randNumero,cont):
		#aqui é a parte das perguntas, cada numero do randNumero que é uma historia tem dentro do seu if as perguntas
		# e dentro dele vai ter os cinco if's que é no caso cada pergunta e mais um pra ele selecionar qual é a historia certa.   
		StirngPerg = ''
		if randNumero == '1':
			if cont == 0:
				StirngPerg = 'a) Onde o homem estava antes de ir ao restaurante? \n1. Em um bar \n2. Em um cruzeiro \n3. Em um ônibus \n4. Em um lugar deserto\n\n'
			if cont == 1:
				StirngPerg = 'b) O que aconteceu com ele antes do restaurante?\n 1. Foi abduzido por alienigenas \n2. O navio afundou\n3. Estava perdido \n4. Bebeu demais e não sabia onde estava\n\n'
			if cont == 2:
				StirngPerg = 'c) Qual motivo da sua morte? \n1. A sopa esta diretamente relacionada com a sua esposa \n2. A sopa estava envenenada \n3. A sopa era muito ruim \n4. Ele estava tendo alucinações por efeito de drogas\n\n'
			if cont == 3:
				StirngPerg = 'd) Qual a motivação dele cometer suicídio? \n1. Ele estava com problemas mentais. \n2. Ele trabalhava em uma ONG de proteção as gaivotas. \n3. Ele estava insatisfeito com a vida que levava. \n4. Ele era casado, agora sua esposa estava morta.\n\n'
			if cont == 4:
				StirngPerg = 'Finalmente, o que aconteceu?\n\n1. O homem estava num bar com sua mulher, quando uma enchente alagou o local.\nEle foi resgatado por um grupo num bote. O bote virou e a mulher morreu.\nEle bateu a cabeça muito forte e ficou incosciente, quando acordou não lembrava o que tinha acontecido.\nFoi a um restaurante comer, pediu sopa de gaivota, ao provar lembrou imediatamente o que havia acontecido, sentiu-se culpado e suicidou-se.\n\n 2. O homem trabalhava em uma empresa a muitos anos, passava por periodos de crise financeira.\nPois havia sido demitido recentemente, e passou por momentos critícos na sua vida, no qual lhe faltava dinheiro para tudo.\nEle precisava comer apenas o que tinha gratuitamente para sobreviver, uma senhora vizinha ao lado vendo seu sofrimento lhe oferecia sopa todos os dias.\nEle já não aguentava mais aquela comida, vendeu seus sapatos para fazer uma refeição digna e lá chegando o garçon te dar para comer a sopa de gaivota, \nsemelhante a que comia todos os dias, em desespero, suicido-se.\n\n3. O homem estava num cruzeiro com sua mulher, quando uma explosão afundou o navio e o cegou,\nEle foi resgatado por um grupo num bote. O grupo afirmava que sua mulher havia falecido. \nEles ficaram com fome, e tudo o que tinham pra comer era o cadáver da mulher. \nComo o homem estava cego, disseram a ele que o que comiam era uma sopa de gaivota. \nEm terra firme, ele foi ao restaurante, e, ao provar a verdadeira sopa de gaivota, deduziu o ocorrido e suicidou-se.\n\n4. O homem descobriu que estava sendo traido pela esposa, com muita raiva decidiu mata-lá.\nPensou muito e decidiu então preparar o prato preferido da esposa no jantar do dia seguinte "sopa de gaivota".\nNo qual colocou veneno e a matou.\nDias depois afundado em sua própria dor, um misto de culpa e saudade, foi a um restaurante e pediu sopa de gaivota,\nao provar aquela sopa, ficou em estado de choque, pegou uma faca e se matou. \n\n'
		if randNumero == '2':
			if cont == 0:
				StirngPerg = 'a) Qual o motivo para a viagem do homem para a capital?\n1) Foi conhecer um grande amor que morava na capital\n2) Foi buscar o prêmio da loteria que havia ganhado\n3) Foi fazer uma cirurgia para curar sua cegueira\n4) Foi visitar seus filhos que ele não via a anos\n\n'
			if cont == 1:
				StirngPerg = 'b) O motivo da viagem esta ligado diretamente ao motivo da morte?\n1) Sim\n2) Não\n\n'
			if cont == 2:
				StirngPerg = 'c) Caso o homem tivesse viajado em outro meio de transporte, ele teria se matado? \n1) Sim\n2) Não\n\n'
			if cont == 3:
				StirngPerg = 'd) Quais os motivos que o fizeram voltar?\n1) Decepção com o novo amor\n2) O prêmio da loteria havia sido roubado\n3) A cirurgia foi feita com sucesso\n4) Não foi bem recebido pelos filhos\n\n'
			if cont == 4:
				StirngPerg = 'Finalmente, o que aconteceu?\n\n1) O homem era cego. Ele foi à cidade fazer uma cirurgia pra curar a cegueira.\nNa viagem de volta, ele passou por um túnel longo, e pensou que estava cego novamente, ficou revoltado e se matou.\n\nO homem era viuvo a muitos anos, descobriu um novo amor a distância.\nFoi até a capital para conhece-la pessoalmente, mas decepcionou-se com a pessoa imediatamente e resolveu voltar.\nInconsolado, decidiu tomar uma dose de veneno a ter a vida ceifada, já que para ele não valia a pena continuar vivendo.\n\n3) O homem era muito pobre. Ele foi à cidade pegar o dinheiro da loteria que tinha ganhado.\nNa viagem de volta, ele percebeu que estava sendo seguido, ao tentar fugir dos perseguidores resolveu do trem em movimento.\n\n4) O homem tinha dois filhos que moravam na capital e a muito tempo não os via, resolveu ir visitá-los de surpresa.\nAo chegar a capital, descobriu que os dois filhos teriam morrido a algums meses, vitimas de um acidente fatal.\nInconformado e sentindo muita dor, resolveu voltar para casa, se matou ainda durante a viagem.\n\n'
		if randNumero == '3':
			if cont == 0:
				StirngPerg = 'a) A mulher representava algum risco de vida ao homem ou para o bar?\n1) Sim\n2) Não\n\n'
			if cont == 1:
				StirngPerg = 'b) O homem no balcão conhecia a mulher?\n1) Sim\n2) Não\n\n'
			if cont == 2:
				StirngPerg = 'c) A mulher conhecia o homem?\n1) Sim\n2) Não\n\n'
			if cont == 3:
				StirngPerg = 'd) Existe outros fatores externos ao bar que influencie na história?\n1) Sim\n2) Não\n\n'
			if cont == 4:
				StirngPerg = 'Finalmente, o que aconteceu?\n\n1) Ela tinha combinado com o homem que se caso acontecesse algo que a fizesse entrar no bar, a matasse.\n\n2) Ele estava assaltando o bar e resolveu eliminar as testemunhas! \n\n3) Ela estava armada e ele reagiu por medo.\n\n4) Ele notou que a mulher era uma grande procurada da justiça por crimes bárbaros e a matou para obter a recompensa.\n\n'
		if randNumero == '4':
			if cont == 0:
				StirngPerg = 'a) A mulher estava esperando alguém ou algo?\n1) Sim\n2) Não\n\n'
			if cont == 1:
				StirngPerg = 'b) A sombra botava a vida da mulher em risco?\n1) Sim\n2) Não\n\n'
			if cont == 2:
				StirngPerg = 'c) A mulher tinha problemas mentais?\n1) Sim\n2) Não\n\n'
			if cont == 3:
				StirngPerg = 'd) De quem poderia ser a sombra?\n 1) Um pombo\n2) Um ladrão\n3) Um espírito\n4) Um gato\n\n'
			if cont == 4:
				StirngPerg = 'Finalmente, o que aconteceu?\n\n1) Ela tinha combinado com o homem que se caso acontecesse algo que a fizesse entrar no bar, a matasse.\n\n2) Ele estava assaltando o bar e resolveu eliminar as testemunhas! \n\n3) Ela estava armada e ele reagiu por medo.\n\n4) Ele notou que a mulher era uma grande procurada da justiça por crimes bárbaros e a matou para obter a recompensa.\n\n'
		if randNumero == '5':
			if cont == 0:
				StirngPerg = 'a) A mulher tinha motivos para cometer o crime?\n1) Sim\n2) Não\n\n'
			if cont == 1:
				StirngPerg = 'b) O crime pode ser caracterizado como um acidente?\n1) Sim\n2) Não\n\n'
			if cont == 2:
				StirngPerg = 'c) A mulher tinha problemas mentais?\n1) Sim\n2) Não\n\n'
			if cont == 3:
				StirngPerg = 'd) De que forma ela os matou?\n1) Uma explosão\n2) Veneno\n3) Arma de fogo\n4) Arma branca\n\n'
			if cont == 4:
				StirngPerg = 'Finalmente, o que aconteceu?\n\n1) A mulher acordou durante a noite, viu uma sobra de um espírito maligno, que tomou posse do corpo da mulher sufocando-a até a morte.\n\n2) A mulher acordou no meio da noite e viu a sombra de um homem. Segui-lhe e viu que era um famoso serial killer procurado pela policia.\nTemendo os horrores que ele fazia com suas vitimas, se matou antes que ele a encontrasse.\n\n3) A mulher tinha problemas psicológicos e pensou ver seres inanimados, em uma imensa crise se matou.\n\n4) A mulher acordou no meio da noite e viu a sombra de um pombo-correio. A carta era um colega de seu marido dizendo que o mesmo estava morto.\nIncapaz de suportar a perda, ela se matou,\n\n'
		return StirngPerg
					
	def acertoEerro(self,randNumero,cont,resposta):
		#aqui é a resposta de cada pergunta tipo acho que tu já pegou a ideia, tipo dentro do randNumero de cada historia
		#dentro do 'cont' de cada pergunta tem que ter um if com a resposta certa e o caso errado e caso onde ele acerta a historia 
		StringAcerto = ''
		if randNumero == '1':
			if cont == 0:
				if resposta == '2':
					StringAcerto = 'Exatamente, vamos a novas descobertas!\n\n'
				else:
					StringAcerto = 'Calma, pense um pouco mais...\n\n'
			if cont == 1:
				if resposta == '2':
					StringAcerto = 'Resposta correta, continue descobrindo pistas!\n\n'
				else:
					StringAcerto = 'Ops, resposta incorreta\n\n'
			if cont == 2:
				if resposta == '1':
					StringAcerto = 'Muito bem, a historia faz sentido agora? Vamos para a ultima pergunta.\n\n'
				else:
					StringAcerto = 'Infelizmente não aconteceu assim... Preste atenção nos detalhes, vamos para a ultima pergunta.\n\n'
			if cont == 3:
				if resposta == '4':
					StringAcerto = 'Isso mesmo, agora é só reunir todas as informações!\n\n'
				else:
					StringAcerto = 'Resposta errada, releia tudo novamente e preste atenção nos detalhes.\n\n'
			if cont == 4:
				if resposta == '3':
					StringAcerto = 'Desvendou o mistério!\n\n'
				else:
					StringAcerto = 'Não Desvendou o mistério!\n\n'		
		if randNumero == '2':
			if cont == 0:
				if resposta == '3':
					StringAcerto = 'Exatamente, vamos a novas descobertas!\n\n'
				else:
					StringAcerto = 'Calma, pense um pouco mais...\n\n'
			if cont == 1:
				if resposta == '1':
					StringAcerto = 'Resposta correta, continue descobrindo pistas!\n\n'
				else:
					StringAcerto = 'Ops, resposta incorreta\n\n'
			if cont == 2:
				if resposta == '2':
					StringAcerto = 'Muito bem, a historia faz sentido agora? Vamos para a ultima pergunta\n\n'
				else:
					StringAcerto = 'Infelizmente não aconteceu assim... Preste atenção nos detalhes, vamos para a ultima pergunta.\n\n'
			if cont == 3:
				if resposta == '3':
					StringAcerto = 'Isso mesmo, agora é só reunir todas as informações!\n\n'
				else:
					StringAcerto = 'Resposta errada, releia tudo novamente e preste atenção nos detalhes.\n\n'
			if cont == 4:
				if resposta == '1':
					StringAcerto = 'Desvendou o mistério!\n\n'
				else:
					StringAcerto = 'Não Desvendou o mistério!\n\n'		
		if randNumero == '3':
			if cont == 0:
				if resposta == '2':
					StringAcerto = 'Exatamente, vamos a novas descobertas!\n\n'
				else:
					StringAcerto = 'Calma, pense um pouco mais...\n\n'
			if cont == 1:
				if resposta == '2':
					StringAcerto = 'Resposta correta, continue descobrindo pistas!\n\n'
				else:
					StringAcerto = 'Ops, resposta incorreta\n\n'
			if cont == 2:
				if resposta == '2':
					StringAcerto = 'Muito bem, a historia faz sentido agora? Vamos para a ultima pergunta\n\n'
				else:
					StringAcerto = 'Infelizmente não aconteceu assim... Preste atenção nos detalhes, vamos para a ultima pergunta.\n\n'
			if cont == 3:
				if resposta == '2':
					StringAcerto = 'Isso mesmo, agora é só reunir todas as informações!\n\n'
				else:
					StringAcerto = 'Resposta errada, releia tudo novamente e preste atenção nos detalhes.\n\n'
			if cont == 4:
				if resposta == '2':
					StringAcerto = 'Desvendou o mistério!\n\n'
				else:
					StringAcerto = 'Não Desvendou o mistério!\n\n'		
		if randNumero == '4':
			if cont == 0:
				if resposta == '1':
					StringAcerto = 'Exatamente, vamos a novas descobertas!\n\n'
				else:
					StringAcerto = 'Calma, pense um pouco mais...\n\n'
			if cont == 1:
				if resposta == '2':
					StringAcerto = 'Resposta correta, continue descobrindo pistas!\n\n'
				else:
					StringAcerto = 'Ops, resposta incorreta\n\n'
			if cont == 2:
				if resposta == '2':
					StringAcerto = 'Muito bem, a historia faz sentido agora? Vamos para a ultima pergunta\n\n'
				else:
					StringAcerto = 'Infelizmente não aconteceu assim... Preste atenção nos detalhes, vamos para a ultima pergunta.\n\n'
			if cont == 3:
				if resposta == '1':
					StringAcerto = 'Isso mesmo, agora é só reunir todas as informações!\n\n'
				else:
					StringAcerto = 'Resposta errada, releia tudo novamente e preste atenção nos detalhes.\n\n'
			if cont == 4:
				if resposta == '4':
					StringAcerto = 'Desvendou o mistério!\n\n'
				else:
					StringAcerto = 'Não Desvendou o mistério!\n\n'		
		if randNumero == '5':
			if cont == 0:
				if resposta == '2':
					StringAcerto = 'Exatamente, vamos a novas descobertas!\n\n'
				else:
					StringAcerto = 'Calma, pense um pouco mais...\n\n'
			if cont == 1:
				if resposta == '1':
					StringAcerto = 'Resposta correta, continue descobrindo pistas!\n\n'
				else:
					StringAcerto = 'Ops, resposta incorreta\n\n'
			if cont == 2:
				if resposta == '2':
					StringAcerto = 'Muito bem, a historia faz sentido agora? Vamos para a ultima pergunta\n\n'
				else:
					StringAcerto = 'Infelizmente não aconteceu assim... Preste atenção nos detalhes, vamos para a ultima pergunta.\n\n'
			if cont == 3:
				if resposta == '1':
					StringAcerto = 'Isso mesmo, agora é só reunir todas as informações!\n\n'
				else:
					StringAcerto = 'Resposta errada, releia tudo novamente e preste atenção nos detalhes.\n\n'
			if cont == 4:
				if resposta == '3':
					StringAcerto = 'Desvendou o mistério!\n\n'
				else:
					StringAcerto = 'Não Desvendou o mistério!\n\n'		
		return StringAcerto

