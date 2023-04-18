package db_example;
 
import java.net.ServerSocket;
import java.net.Socket;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.PrintWriter;
 
public class MyEchoServer extends java.lang.Thread {
 
    protected boolean OutServer = false;
    protected ServerSocket server;
    protected final int ServerPort = 8765;// �n�ʱ���port
 
    public MyEchoServer() {
        try {
            server = new ServerSocket(ServerPort);
 
        } catch (java.io.IOException e) {
            System.out.println("Socket�Ұʦ����D !");
            System.out.println("IOException :" + e.toString());
        }
    }
 
	protected String getRetValue(String input) {
		return(input+"\n");
	}
 
    public void run() {
        Socket socket;
        
		System.out.println("���A���w�Ұ� !");
        while (!OutServer) {
            socket = null;
            try {
                synchronized (server) {
                    socket = server.accept();
                }
                System.out.println("���o�s�u : InetAddress = "
                        + socket.getInetAddress());
                // TimeOut�ɶ�
                socket.setSoTimeout(15000);
 
				PrintWriter out = new PrintWriter(socket.getOutputStream(), true); 
				BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream())); 

				String inputLine; 

				while ((inputLine = in.readLine()) != null) { 
					System.out.println ("Server: " + inputLine); 
					if (inputLine.equals("QUIT.")) 
						break;
					out.println(this.getRetValue(inputLine));
					out.flush();
				}	 

                
				in.close();
                in = null;
                socket.close();
 
            } catch (java.io.IOException e) {
                System.out.println("Socket�s�u�����D !");
                System.out.println("IOException :" + e.toString());
            }
 
        }
    }
 
    public static void main(String args[]) {
        (new MyEchoServer()).start();
    }
 
}