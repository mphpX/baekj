import java.io.*;
import java.util.*;

public class Solution {
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int[][] rxy = {{0, 1}, {2,3}};
	static int[][][] graph;
	static int n;
	static void moveAll() {
		int[][][] next= new int[n][n][3];
		
		for(int cur_x = 0; cur_x < n; cur_x++) {
			for(int cur_y = 0; cur_y < n; cur_y++) {
				if(graph[cur_x][cur_y][0] == 0) continue;
				int cur_sum = graph[cur_x][cur_y][0];
				int cur_direction = graph[cur_x][cur_y][2];
				int next_x = cur_x + dx[cur_direction];
				int next_y = cur_y + dy[cur_direction];
				if(next_x == 0 || next_x == n-1 || next_y == 0 || next_y ==n-1) {
					cur_sum/=2;
					cur_direction = rxy[graph[cur_x][cur_y][2]/2][(graph[cur_x][cur_y][2]%2+1)%2];
				}
				if(cur_sum == 0) continue;
				next[next_x][next_y][0]+= cur_sum;
				if(next[next_x][next_y][1] < cur_sum) {
					next[next_x][next_y][2]= cur_direction;
					next[next_x][next_y][1]= cur_sum; 
				}
			}
		}
		graph= next;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int m, k;
		int x, y, u, v;
		StringTokenizer st;
		for(int tc = 1; tc<= t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			graph = new int[n][n][3];
			for(int nn = 0; nn < k; nn++) {
				st = new StringTokenizer(br.readLine());
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				u = Integer.parseInt(st.nextToken());
				v = Integer.parseInt(st.nextToken())-1;
				graph[x][y][0]=u;
				graph[x][y][2]=v;
			}
			for(int time = 0; time< m; time++) {
				moveAll();
			}
			int ans = 0;
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					ans+= graph[i][j][0];
				}
			}
			bw.write("#"+tc+" "+ans + "\n");
		}
		bw.flush();
	}
}