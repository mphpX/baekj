import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		boolean isit= true;
		boolean[] nums = new boolean[246913];
		nums[2]= nums[3]= nums[5] = true;
		for(int i = 5; i < 246913; i+=2) {
			isit = true;
			for(int j = 3; j <= Math.sqrt(i); j+=2) {
				if(nums[j] && i%j ==0) {
					isit = false;
					break;
				}
			}
			if(isit) nums[i]= true;
		}
		int ct;
		while(n!=0) {
			ct=0;
			for(int i = n+1; i<=2*n; i++) {
				if(nums[i]) ct++;
			}
			bw.write(ct+"\n");
			
			n = Integer.parseInt(br.readLine());
		}
		bw.flush();
	}
}