import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int mn = 5000;
		for(int i = 0; i <= n/3; i++) {
			for(int j = 0; j <= (n-3*i)/5; j++) {
				if(3*i + 5*j== n) {
					mn = Math.min(i+j, mn);
				}
			}
		}
		if(mn== 5000) System.out.println(-1);
		else System.out.println(mn);
	}
}