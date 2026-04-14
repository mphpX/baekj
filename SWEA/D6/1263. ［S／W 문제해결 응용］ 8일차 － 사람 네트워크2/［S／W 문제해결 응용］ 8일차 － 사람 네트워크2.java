
import java.util.*;
import java.io.*;
public class Solution {	
	static int[][] graph;
	static int m;
	static int n;
	static int bfs(int x) {
		Queue<Integer> q = new LinkedList<>();
		int[] visited = new int[n];
		q.offer(x);
		visited[x] = 1;
		while(!q.isEmpty()) {
			int cur = q.poll();
			for(int i = 0; i < n; i++){
				if(graph[cur][i] == 1 && visited[i] == 0){
					visited[i] = visited[cur] + 1;
					q.offer(i);
				}
			}
		}
		int ans = 0;
		for(int i = 0; i < n; i++){
			ans+= visited[i]-1;
		}
		return ans;
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
			graph = new int[n][n];
			for(int i = 0; i< n; i++){
				for(int j = 0; j < n; j++){
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int ans = bfs(0);
			int cur = 0;
			for(int j = 1; j < n; j++){
				cur = bfs(j);
				if(ans > cur){
					ans = cur;
				}
			}
			bw.write("#" + tc + " " + ans + "\n");
		}
		bw.flush();
	}
}
