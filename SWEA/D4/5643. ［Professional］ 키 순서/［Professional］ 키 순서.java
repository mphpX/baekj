
import java.util.*;
import java.io.*;
public class Solution {	
	static int[][] graph;
	static int m;
	static int n;
	static boolean bfs(int x) {
		Queue<Integer> bigq = new LinkedList<>();
		boolean visited[] = new boolean[n+1];
		bigq.offer(x);
		visited[x]= true;
		while(!bigq.isEmpty()){
			int cur = bigq.poll();
			visited[cur]= true;
			for(int i = 1; i <= n; i++) {
				if(graph[cur][i] ==1 && !visited[i]){
					visited[i]= true;
					bigq.offer(i);
				}
			}
		}
		Queue<Integer> smallq = new LinkedList<>();
		smallq.offer(x);
		while(!smallq.isEmpty()){
			int cur = smallq.poll();
			visited[cur]= true;
			for(int i = 1; i <= n; i++){
				if(graph[cur][i] == -1 && !visited[i]){
					visited[i]= true;
					smallq.offer(i);
				}
			}
		}
		int cnt = 0;
		for(int i = 1; i <= n; i++) {
			if(visited[i]) cnt++;
		}
		return cnt == n;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int test= Integer.parseInt(br.readLine());
		//테스트 케이스
		for(int tc= 1; tc <= test; tc++) {
			n = Integer.parseInt(br.readLine());
			m = Integer.parseInt(br.readLine());
			graph = new int[n+1][n+1];
			int a = 0;
			int b = 0;
			for(int i = 0; i < m; i++) {
				st= new StringTokenizer(br.readLine());
				a= Integer.parseInt(st.nextToken());
				b= Integer.parseInt(st.nextToken());
				graph[a][b]= 1;
				graph[b][a]= -1;
			}
			int ans = 0;
			for(int i = 1; i <= n; i++){
				if(bfs(i))ans++;
			}
			bw.write("#"+tc+" "+ans+"\n");
		}
		bw.flush();
	}
}
