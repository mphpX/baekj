import java.util.*;
class Solution {
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    public int bfs(int start_x, int start_y, int[][] maps){
        Queue<int[]> q = new ArrayDeque<>();
        int n = maps.length;
        int m = maps[0].length;
        q.offer(new int[] {start_x, start_y});
        int[][] visited = new int[n][m];
        visited[start_x][start_y]= 1;
        while(!q.isEmpty()){
            int[] poll = q.poll();
            for(int i = 0;i < 4; i++){  
                int next_x = poll[0] + dx[i];
                int next_y = poll[1] + dy[i];
                if(next_x >=0 && next_x <n && next_y >=0 && next_y <m){
                    if(visited[next_x][next_y] == 0 && maps[next_x][next_y] == 1){
                        q.offer(new int[] {next_x, next_y});
                        visited[next_x][next_y]= visited[poll[0]][poll[1]]+1;
                    }
                }
            }
        }
        if(visited[n-1][m-1]== 0){
            return -1;
        }
        return visited[n-1][m-1]; 
    }
    public int solution(int[][] maps) {
        int answer = 0;
        
        return bfs(0,0, maps);
    }
}