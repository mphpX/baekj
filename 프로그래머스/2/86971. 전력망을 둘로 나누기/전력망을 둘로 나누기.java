import java.util.*;
class Solution {
    int[][] graph;
    int mn= 101;
    boolean[] visited;
    public int bfs(int x, int n){
        Deque<Integer> dq= new ArrayDeque<>();
        dq.add(x);
        visited[x]= true;
        int ct = 1;
        while(!dq.isEmpty()){
            int cur = dq.poll();
            for(int i = 1; i <= n; i++){
                if(graph[cur][i]== 1 && !visited[i]){
                    visited[i]= true;
                    dq.add(i);
                    ct+=1;
                }
            }
        }
        return ct;
    }
    public void back_track(int n, int[][] wires){
        for(int i = 0; i < wires.length; i++){
            for(int j = 0; j < n+1; j++){
                visited[j]= false;
            }
            int idx = 0;
            int[] diff= new int[2];
            int x = wires[i][0];
            int y = wires[i][1];
            graph[x][y] = 0;
            graph[y][x] = 0;
            for(int j = 1; j < n+1; j++){
                if(!visited[j]){
                    diff[idx++]= bfs(j, n);
                }
            }
            mn = Math.min(Math.abs(diff[1]- diff[0]), mn);
            graph[x][y] = 1;
            graph[y][x] = 1;
        }
    }
    public int solution(int n, int[][] wires) {
        int answer = -1;
        graph= new int[n+1][n+1];
        visited= new boolean[n+1];
        for(int i = 0; i < wires.length; i++){
            int x= wires[i][0];
            int y= wires[i][1];
            graph[x][y]= 1;
            graph[y][x]= 1;
        }
        back_track(n, wires);
        return mn;
    }
}