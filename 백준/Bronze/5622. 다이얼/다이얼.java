import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int ans = 0;
		int[] rec = {0, 3, 6, 9, 12, 15, 19, 22, 26};
		for(int i = 0; i < str.length(); i++) {
			int cur = str.charAt(i)- 'A';
			for(int j = 0; j < 9; j++) {
				if(rec[j] > cur) {
					ans+= j + 2;
					break;
				}
			}
		}
		System.out.println(ans);
	}
}
