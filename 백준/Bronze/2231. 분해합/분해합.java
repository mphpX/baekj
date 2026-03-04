import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int std = 1;
		int ct = 0;
		while(std<=n) {
			std*=10;
			ct+=1;
		}
		int cur = 0;
		int sm = 0;
		int ans = 0;
		for(int i = n-9*ct; i < n; i++) {
			cur = i;
			sm = 0;
			while(cur> 0) {
				sm+= cur%10;
				cur/=10;
			}
			if(sm+i == n) {
				ans =i;
				break;
			}
		}
		System.out.println(ans);
	}
}