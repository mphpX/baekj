import java.io.*;
import java.util.*;

public class Solution {
	static char[][] graph;
	static int[][] loc;
	static boolean[][] visited;
	static int n;
	static int boom;
	static int[] dx= {1, 1, 1, 0, 0, -1, -1, -1};
	static int[] dy= {1, 0, -1, 1, -1, 1, 0, -1};
	static int ct;
	static void update(int x, int y) {
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] {x,y});
		visited[x][y]= true;
		int next_x;
		int next_y;
		while(!q.isEmpty()){
			int[] poll = q.poll();
			int cur_x = poll[0];
			int cur_y = poll[1];
			for(int k = 0; k < 8; k++) {
				next_x= cur_x + dx[k];
				next_y= cur_y + dy[k];
				if(0<= next_x && next_x < n) {
					if(0<= next_y && next_y < n) {
						if(!visited[next_x][next_y]) {
							if(loc[next_x][next_y]==0) {
								q.offer(new int[] {next_x,next_y});
							}else if(loc[next_x][next_y]==-1) continue;
							visited[next_x][next_y]= true;
						}
					}		
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		for(int tc= 1; tc<=t; tc++) {
			boom= ct= 0;
			n = Integer.parseInt(br.readLine());
			graph= new char[n][n];
			loc = new int[n][n];
			visited= new boolean[n][n];
			for(int i = 0 ; i < n; i++) {
				String ch = br.readLine();
				for(int j = 0; j < n; j++) {
					graph[i][j]= ch.charAt(j);
					if(graph[i][j]=='*') {
						boom++;
						loc[i][j]= -1;
					}
				}
			}
			int next_x, next_y;
			for(int i = 0; i < n;i++) {
				for(int j = 0; j < n; j++) {
					if(loc[i][j]!=-1) {
						for(int k = 0; k < 8; k++) {
							next_x= i + dx[k];
							next_y= j + dy[k];
							if(0<= next_x && next_x < n) {
								if(0<= next_y && next_y < n) {
									if(graph[next_x][next_y]=='*') {
										loc[i][j]+=1;
									}
								}
							}	
						}
					}
				}
			}
			for(int i = 0; i < n;i++) {
				for(int j = 0; j < n; j++) {
					if(!visited[i][j] && loc[i][j]== 0) {
						update(i,j);
						ct+=1;
					}
				}
			}
			for(int i = 0; i < n;i++) {
				for(int j = 0; j < n; j++) {
					if(!visited[i][j] && loc[i][j]!=-1) {
						ct+=1;
					}
				}
			}
			bw.write("#"+tc+" "+ct+"\n");
		}
		bw.flush();
		
	}
}