import java.util.*;
import java.io.*;
public class Solution {	
	static int[][] graph;
	static int m;
	static int n;
	static int calculate(int x, int y, int k) {
		int house= 0;
		for(int i = x; i < x+k; i++) {
			for(int j = y - (k-1) +(i-x); j <= y+(k-1) -(i-x); j++) {
				if(0 > i || i >= n || 0 > j || j >= n) continue;
				house+= graph[i][j];
			}
		}
		for(int i = x-k+1; i < x; i++) {
			for(int j = y +(x-k+1-i); j <= y - (x-k+1-i); j++) {
				if(0 > i || i >= n || 0 > j || j >= n) continue;
				house+= graph[i][j];
			}
		}
		return house;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int test= Integer.parseInt(br.readLine());
		//테스트 케이스
		for(int tc= 1; tc <= test; tc++) {
			st= new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			graph = new int[n][n];
			
			for(int i = 0; i < n; i++) {
				st= new StringTokenizer(br.readLine());
				for(int j = 0; j < n; j++) {
					graph[i][j]= Integer.parseInt(st.nextToken());
				}
			}
			int ans= 0;
			int house= 0;
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					for(int k = 1; k <= 2*n; k++) {
						house = calculate(i,j,k);
						if(house*m- (k*k+ (k-1)* (k-1)) >= 0) {
							ans= Math.max(ans, house);
						}
					}
				}
			}
			bw.write("#"+tc + " "+ ans + "\n");
			
		}
		bw.flush();
	}
}
