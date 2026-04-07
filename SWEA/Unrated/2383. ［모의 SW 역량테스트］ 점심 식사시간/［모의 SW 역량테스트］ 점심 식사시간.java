import java.util.*;
import java.io.*;
public class Solution {
	static int[][] graph;
	static int[][] goals;
	static int ans = Integer.MAX_VALUE;
	static ArrayList<int[]> peoples;
	
	public static class process{
		int idx;
		int time;
		process(int idx, int time) {
			this.idx = idx;
			this.time = time;
		}
	}
	
	
	static class processComparator implements Comparator<process>{
		@Override
		public int compare(process o1, process o2) {
			return o1.time -o2.time;
		}
	}
	static int ct;
	static int[] where;
	static int calculate() {
		int[] cur;
		int a_time;
		PriorityQueue<process>[] pqs= new PriorityQueue[2];
		for(int i = 0; i < 2; i++) {
			pqs[i]= new PriorityQueue<>(1, new processComparator());
		}
		process p;
		ArrayList<ArrayList<process>> ps = new ArrayList<>();
		ArrayList<process> a = new ArrayList<>();
		ArrayList<process> b = new ArrayList<>();
		for(int i = 0; i < ct; i++) {
			cur = peoples.get(i);
			//도착시간
			a_time = Math.abs(goals[where[i]][0] - cur[0])+ Math.abs(goals[where[i]][1] - cur[1])+1;
			p = new process(i, a_time);
			if(where[i]==0) {
				a.add(p);
			}else {
				b.add(p);
			}
		}
		a.sort((o1, o2) -> o1.time- o2.time);
		b.sort((o1, o2) -> o1.time - o2.time);
		ps.add(a);
		ps.add(b);
	
		int end_time = 0;
		int[] end_times = new int[2];
		for(int i = 0; i < 2; i++) {
			int k = graph[goals[i][0]][goals[i][1]];
			ArrayList<process> processes =ps.get(i);
			int end = processes.size();
			int idx = 0;
			while(idx < end) {
				end_time = processes.get(idx).time;
				if(pqs[i].size()> 2) {
					end_time = pqs[i].poll().time + k;
					if(end_time > processes.get(idx).time) processes.get(idx).time = end_time;
				}
				pqs[i].add(processes.get(idx++));
			}
			while(pqs[i].size()> 0) {
				end_time = pqs[i].poll().time+k;
			}
			end_times[i]= end_time;
		}
		return Math.max(end_times[0], end_times[1]);
	}
	
	static void wheretogo(int x) {
		if(x == ct) {
			int tmp = calculate();
			ans = Math.min(ans, tmp);
			return;
		}
		where[x] = 0;
		wheretogo(x+1);
		where[x] = 1;
		wheretogo(x+1);
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int test= Integer.parseInt(br.readLine());
		//테스트 케이스
		for(int tc= 1; tc <= test; tc++) {
			int n = Integer.parseInt(br.readLine());
			//계단 설정

			//graph 입력
			graph = new int[n][n];
			//goals 입력
			goals = new int[2][2];
			//peoples 입력
			peoples = new ArrayList<>();
			for(int i = 0; i < n; i++) {
				st= new StringTokenizer(br.readLine());
				for(int j = 0; j < n; j++) {
					graph[i][j]= Integer.parseInt(st.nextToken());
				}
			}
			//계단 index
			int a =0;
			//사람 수
			ct = 0;
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					if(graph[i][j]== 1) {
						peoples.add(new int[]{i,j});
						ct++;
					}else if(graph[i][j] >1) {
						goals[a][0]= i;
						goals[a++][1]= j;
					}
				}
			}
			//사람마다 어디 goal으로 갈지
			where = new int[ct];
			ans = Integer.MAX_VALUE;
			wheretogo(0);
			bw.write("#"+tc+" "+ ans+"\n");
		}
		bw.flush();
	}
}
