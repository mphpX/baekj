import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int s_h = Integer.parseInt(br.readLine());
		int s_pc = Integer.parseInt(br.readLine());
		int pc_a = Integer.parseInt(br.readLine());
		int a_h = Integer.parseInt(br.readLine());
		bw.write((int)(s_h + s_pc + pc_a + a_h)/60 + "\n");
		bw.write((int)(s_h + s_pc + pc_a + a_h)%60 + "\n");
		bw.flush();
    }
}