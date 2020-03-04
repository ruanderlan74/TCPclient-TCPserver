import java.net.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.*;
import com.google.gson.Gson;

public class TCPClient {
	public String data = null;
	public Socket s = null;
	public DataInputStream in;
	public DataOutputStream out;
	public BufferedReader inn;
	public PrintWriter outt;
	public Gson g = new Gson();
	public Message message = new Message();
	public int contadorReqs = 0;

	public TCPClient(int ClientPort, int ServerPort, String Ip) {

		try {
			InetAddress idnet = InetAddress.getByName(Ip);

			this.s = new Socket(idnet, ServerPort, idnet, ClientPort);
			// this.in =new BufferedReader(new
			// InputStreamReader(s.getInputStream()));
			// this.out = new PrintWriter(s.getOutputStream(), true);
			this.in = new DataInputStream(this.s.getInputStream());
			this.out = new DataOutputStream(this.s.getOutputStream());
		} catch (UnknownHostException ex) {
			Logger.getLogger(TCPClient.class.getName()).log(Level.SEVERE, null,
					ex);
		} catch (IOException ex) {
			Logger.getLogger(TCPClient.class.getName()).log(Level.SEVERE, null,
					ex);
		}
	}

	public void doOperationsend(String msg, String Metodoid) {
		contadorReqs++;
		message.setArrguments(msg);
		message.setMessageType(0);
		message.setObjectReference("Historia");
		message.setMethodid(Metodoid);
		message.setRequestld(contadorReqs);
		String json = g.toJson(message);

		try {
			this.out.writeUTF(json);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public String doOperationget() {
		String E = "ERRO";
		try {
			data = this.in.readUTF();
		} catch (IOException ex) {
			Logger.getLogger(TCPClient.class.getName()).log(Level.SEVERE, null,
					ex);
		}
		message = (Message) g.fromJson(data, Message.class);
		if (message.getObjectReference().equals("Historia")
				&& message.getRequestld() == contadorReqs
				&& message.getMessageType() == 1)
			E = message.getArrguments();
		return E;
	}

	public void close() {
		try {
			contadorReqs = 0;
			this.s.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}