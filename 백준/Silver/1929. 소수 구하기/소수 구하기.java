import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		boolean[] nums = new boolean[1000001];
		boolean isit = true;
		nums[2]= nums[3]= true;
		for(int i = 5; i <= m; i+=2) {
			isit = true;
			for(int j = 3; j <= Math.sqrt(i); j+=2) {
				if(nums[j] && i%j ==0) {
					isit = false;
					break;
				}
			}
			if(isit) nums[i]= true;
		}
		for(int i = n; i <= m; i++) {
			if(nums[i]) bw.write(i+ "\n");
		}
		bw.flush();
	}
}