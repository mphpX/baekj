import java.util.*;

class Solution {
    int N;
    int ans;
    boolean[] visited;
    List<Integer>[] graph;

    public int solution(int n, int[][] wires) {
        N = n;
        ans = Integer.MAX_VALUE;

        graph = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] w : wires) {
            graph[w[0]].add(w[1]);
            graph[w[1]].add(w[0]);
        }

        for (int[] w : wires) {
            int u = w[0], v = w[1];

            graph[u].remove(Integer.valueOf(v));
            graph[v].remove(Integer.valueOf(u));

            visited = new boolean[N+1];
            int cnt = dfs(1);

            ans = Math.min(ans, Math.abs(N - 2 * cnt));

            graph[u].add(v);
            graph[v].add(u);
        }

        return ans;
    }

    int dfs(int node) {
        visited[node] = true;
        int cnt = 1;

        for (int next : graph[node]) {
            if (!visited[next]) {
                cnt += dfs(next);
            }
        }
        return cnt;
    }
}