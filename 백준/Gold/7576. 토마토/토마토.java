import java.io.*;
import java.util.*;
public class Main {
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int n, m;
	static int[][] graph;
	static int[][] visited;
	public static void bfs() {
		Queue<int[]> q = new ArrayDeque<>();
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if(graph[i][j] == 1) {
					q.offer(new int[] {i, j});
				}
			}
		}
		while(!q.isEmpty()) {
			int[] poll = q.poll();
			int cur_x = poll[0];
			int cur_y = poll[1];
			for(int i = 0; i < 4; i++) {
				int next_x = poll[0]+ dx[i];
				int next_y = poll[1]+ dy[i];
				if(0<= next_x && next_x < m && 0 <= next_y && next_y < n) {
					if(graph[next_x][next_y]==0) {
						q.offer(new int[] {next_x, next_y});
						graph[next_x][next_y]= graph[cur_x][cur_y]+1;
					}
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph= new int[m][n];
		visited = new int[m][n];
		for(int i = 0; i < m; i++) {
			st= new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				graph[i][j]= Integer.parseInt(st.nextToken());
			}
		}
		int result= 0;
		boolean isit = true;
		bfs();
		for(int i = 0; i < m; i++) {
			if(!isit) break;
			for(int j = 0; j < n; j++) {
				if(graph[i][j]==0) {
					isit = false;
					break;
				}else if(graph[i][j]>0) {
					if(result < graph[i][j]-1) result = graph[i][j]-1;
				}
			}
		}
		if(!isit) System.out.println(-1);
		else System.out.println(result);
		bw.flush();
	}		
}			