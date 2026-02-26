import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine().toUpperCase();
		int[] rec = new int[26];
		for(int i = 0; i < str.length(); i++) {
			int idx = str.charAt(i)- 'A';
			rec[idx]++;
		}
		char ans = '\0';
		int mx = 0;
		int ct = 0;
		for(int i = 0; i < 26; i++) {
			if(mx < rec[i]) {
				mx = rec[i];
				ans = (char)(i + 'A');
				ct = 0;
			}
			else if(mx == rec[i]) {
				ct+=1;
			}
		}
		System.out.println((ct==0) ? ans : '?');
	}
}
