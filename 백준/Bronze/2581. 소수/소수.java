import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		boolean isit = true;
		int sum = 0;
		int min = -1;
		for(int i = m; i <=n; i++) {
			if(i==1) continue;
			isit = true;
			for(int j = 2; j <i; j++) {
				if(i % j == 0) {
					isit = false;
					break;
				}
			}
			if(isit) {
				min = i;
				sum+= i;
				break;
			}
		}
		if(min != -1) {
			for(int i = min+1; i <=n; i++) {
				if(i==1) continue;
				isit = true;
				for(int j = 2; j <i; j++) {
					if(i % j == 0) {
						isit = false;
						break;
					}
				}
				if(isit) {
					sum+=i;
				}
			}
			System.out.println(sum);
		}
		System.out.println(min);
		
	}
}