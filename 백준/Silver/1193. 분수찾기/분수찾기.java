import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int idx = 0;
		int x = 1;
		int ct = 1;
		while(idx<n) {
			idx+= x++;
			ct++;
		}
		int[] nums= {ct-1, 1};
		for(int i = 0 ; i< idx - n; i++) {
			nums[0]--;
			nums[1]++;
		}
		int st = 0;
		if(ct%2 ==0) st++;
		System.out.printf("%d/%d\n", nums[st], nums[(st+1)%2]);
	}
}