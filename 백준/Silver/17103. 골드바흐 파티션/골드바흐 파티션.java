import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		boolean[] isPrime= new boolean[1000001];
		boolean isit = true;
		int n, ct;
		isPrime[2]= isPrime[3] = isPrime[5] = true;
		for(int i = 7; i < 1000001; i+=2) {
			isit = true;
			for(int j = 2; j <= Math.sqrt(i); j++) {
				if(isPrime[j]) {
					if(i % j == 0) {
						isit = false;
						break;
					}
				}
			}
			if(isit) isPrime[i]= isit;
		}
		for(int i = 0; i < t; i++) {
			n = Integer.parseInt(br.readLine());
			ct = 0;
			for(int x = 2; x <= n /2; x++) {
				if(isPrime[x] && isPrime[n-x]) {
					ct+=1;
				}
			}
			bw.write(ct+ "\n");
		}
		bw.flush();
	}
}