import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int x= 0;
		int y= 0;
		int n = Integer.parseInt(br.readLine());
		int[][] visited = new int[101][101];
		for(int i = 0; i < n; i++) {
			st= new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			for(int cx = x; cx < x+10; cx++) {
				for(int cy = y; cy < y+10; cy++) {
					visited[cx][cy]+=1;
				}
			}
		}
		int ans =0;
		for(int i = 0; i < 101; i++) {
			for(int j = 0; j <101; j++) {
				if(visited[i][j]>0) {
					ans++;
				}
			}
		}
		System.out.println(ans);
	}
}