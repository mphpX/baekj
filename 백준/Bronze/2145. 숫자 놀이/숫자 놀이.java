import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int tmp = 0;
		while(n !=0) {
			while(n > 9) {
				tmp = n;
				n = 0;
				while(tmp > 0) {
					n+=tmp%10;
					tmp/=10;
				}
			}
			bw.write(n + "\n");
			n= Integer.parseInt(br.readLine());
		}
		bw.flush();
	}
}
