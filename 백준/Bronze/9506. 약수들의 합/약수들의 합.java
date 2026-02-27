import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int x = 0;
		while(n !=-1) {
			x = 1;
			StringBuilder sb = new StringBuilder();
			sb.append(n).append(" = 1");
			for(int i = 2; i < n; i++) {
				if(n%i == 0) {
					x+=i;
					sb.append(" + ").append(i);
				}
			}
			if(x== n) {
				System.out.println(sb.toString());
			}else {
				System.out.printf("%d is NOT perfect.\n", n);
			}
			
			
			n = Integer.parseInt(br.readLine());
		}
		
	}
}