import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int ra= 0;
		int rb= 0;
		
		while(a!=0) {
			ra+=a%10;
			ra*=10;
			a/=10;
		}
		while(b!=0) {
			rb+=b%10;
			rb*=10;
			b/=10;
		}
		System.out.println(Math.max(ra, rb)/10);
		
	}
}
