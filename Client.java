import java.util.Random;
import java.util.Scanner;

public class Client {

	public static void main(String arg[]) throws Exception {
		String op;
		String op2;
		String resposta;
		Scanner scan = new Scanner(System.in);
		int port = 5001;
		int cont = 0;
		Random gerador = new Random();
		while (true) {
			TCPClient c = new TCPClient(port, 8937, "localhost");
			System.out.println("Mortes críticas, suicídios estranhos e bizarrices misteriosas - E o detetive que vai solucionar tudo isso é VOCÊ.\n Descubra a verdadeira história por trás destas cenas se for capaz!\n");
			System.out.println("1 - Gerar Historia\n");
			System.out.println("2 - Lista de Ganhadores \n");
			op = scan.next();
			cont = 0;
			switch (op) {
			case "1":
				c.doOperationsend(Integer.toString((gerador.nextInt(4)+1)), "GerarHistoria");
				resposta = c.doOperationget();
				System.out.println(" Historia \n" + resposta);
				System.out.println(" Apert qualquer tecla para as perquntas\n");
				op2 = scan.next();
				c.doOperationsend(op2, "");
				while (cont <= 4) {
					resposta = c.doOperationget();
					System.out.println(resposta);
					System.out.println("O que vc acha ?");
					op2 = scan.next();
					c.doOperationsend(op2, "");
					resposta = c.doOperationget();
					System.out.println(resposta);
					if (cont == 4) {
						System.out.println("Digite seu Nome");
						op2 = scan.next();
						c.doOperationsend(op2, resposta);
					}
					cont++;
				}
				break;	
			case "2":
				c.doOperationsend("", "ListaDeGanhadores");
				resposta = c.doOperationget();
				System.out.println(resposta);
				break;
			default:
				System.out.println("Opcao Invalida");
				break;
			}
			c.close();
			port++; 

		}
	}

}
