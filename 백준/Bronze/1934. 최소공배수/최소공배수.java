import java.io.*;
import java.util.*;

public class Main {
	public static int gcd(int a, int b) {
		if(a ==0) return b;
		else return gcd(b%a, a);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			st= new StringTokenizer(br.readLine());
			int a= Integer.parseInt(st.nextToken());
			int b= Integer.parseInt(st.nextToken());
			
			int x = Math.min(a, b);
			int y = Math.max(a, b);
			bw.write(a*b/gcd(x,y)+ "\n");
		}
		
		bw.flush();
	}
}