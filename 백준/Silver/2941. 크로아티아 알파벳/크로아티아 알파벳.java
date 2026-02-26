import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int ans = 0;
		boolean[] visited = new boolean[str.length()];
		for(int i = 0; i < str.length(); i++) {
			char cur = str.charAt(i);
			if(cur == '-' || cur =='=') {
				int diff = 2;
				if(i-2 > -1 && str.charAt(i-1)=='z' && str.charAt(i-2)== 'd') {
					diff= 3;
				}
				for(int j = 0; j < diff; j++) {
					visited[i-j]= true;
				}
				ans+=1;
				
			}else if(i>0 && cur == 'j') {
				char prev = str.charAt(i-1);
				if(prev=='l'|| prev=='n') {
					visited[i]= visited[i-1] = true;
					ans+=1;
				}
			}
		}
		for(int i = 0; i < str.length();i++) {
			if(!visited[i]) {
				ans+=1;
			}
		}
		System.out.println(ans);
	}
}
