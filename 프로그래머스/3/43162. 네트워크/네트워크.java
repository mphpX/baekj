
class Solution {
    public void dfs(int start, int n, int[][] graph, int[] visited){
        if(visited[start] == 1) return;
        visited[start] = 1;
        for(int i = 0; i < n; i++){
            if(graph[start][i] == 1 && visited[i]== 0){
                dfs(i, n, graph, visited);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int[] visited= new int[n];
        int answer = 0;
        for(int i = 0; i < n; i++){
            if(visited[i]==0){
                dfs(i, n, computers, visited);
                answer++;
            }
        }
        return answer;
    }
}