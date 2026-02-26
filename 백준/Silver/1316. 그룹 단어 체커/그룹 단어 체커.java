import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int ct = 0;
		for(int i = 0; i < n; i++) {
			String str = br.readLine();
			int[] visited = new int[26];
			for(int j = 0; j < 26; j++) visited[j]= -1;
			int len = str.length();
			int isit = 1;
			for(int j = 0; j < len; j++) {
				int cur = str.charAt(j)-'a';
				if(visited[cur]== -1 || visited[cur]+1 ==j) visited[cur] = j;
				else {
					isit =0;
					break;
				}
			}
			ct+=isit;
		}
		System.out.println(ct);
		
	}
}
