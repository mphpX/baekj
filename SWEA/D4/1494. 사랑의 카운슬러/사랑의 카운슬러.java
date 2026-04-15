
import java.util.*;
import java.io.*;
public class Solution {	
	static int[] visited;
	static int m;
	static int n;
	static long ans;
	static class Node{
		long x;
		long y;
		public Node(long x, long y) {
			this.x = x;
			this.y = y;
		}
	}
	static ArrayList<Node> list;
	static void backtrack(int ct, int idx, long cur_x, long cur_y) {
		if(ct == n /2) {
			for(int i = 0; i < n; i++) {
				if(visited[i] == 0) {
					cur_x -= list.get(i).x;
					cur_y -= list.get(i).y;
				}
			}
			long tmp = cur_x*cur_x + cur_y*cur_y;
			ans= Math.min(ans, tmp);
			return;
		}
		for(int i = idx+1; i < n; i++){
			if(visited[i] == 0) {
				visited[i] = 1;
				backtrack( ct+1, i, cur_x + list.get(i).x, cur_y + list.get(i).y);
				visited[i] = 0;
			}
		}	
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int test= Integer.parseInt(br.readLine());
		//테스트 케이스
		for(int tc= 1; tc <= test; tc++) {
			n = Integer.parseInt(br.readLine());
			visited = new int[n];
			list = new ArrayList<>();
			ans = Long.MAX_VALUE;
			for(int i = 0; i < n; i++){
				st= new StringTokenizer(br.readLine());
				int x=  Integer.parseInt(st.nextToken());
				int y =  Integer.parseInt(st.nextToken());
				list.add(new Node(x,y));
			}
			backtrack(0, -1, 0, 0);
			bw.write("#"+tc+" "+ans+"\n");
		}
		bw.flush();
	}
}
