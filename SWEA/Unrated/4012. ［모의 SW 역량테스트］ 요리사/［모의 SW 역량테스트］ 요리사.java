import java.io.*;
import java.util.*;
public class Solution {
    static int N, Best;
    static int[][] graph;
    static int[] arr;
    static boolean[] visited;
    static void swap(int[] arr, int idx, int idx2){
        int tmp = arr[idx];
        arr[idx]= arr[idx2];
        arr[idx2]= tmp; 
    }

    static void comb( int idx, int ct){
        if(ct == N/2){
            Best= Math.min(Best, calculate());
            return;
        }else if(idx==N) return;
        
        visited[idx]= true;
        comb(idx+1, ct+1);
        visited[idx]= false;
        comb(idx+1, ct);
    }

    static int calculate(){
        int xid=0;
        int yid=0;
        int sum=0;
        int[] x = new int[N/2];
        int[] y = new int[N/2];
        for(int i = 0; i< N; i++){
            if(visited[i]) {
                x[xid++]=i;
            }else y[yid++]=i;
        }
        for(int i = 0; i < N/2; i++){
            for(int j = i+1; j < N/2; j++){
                sum+=graph[x[i]][x[j]]+graph[x[j]][x[i] ] - graph[y[i]][y[j]] -graph[y[j]][y[i]];
            }
        }
        return Math.max(sum, -sum);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader( System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<= t; tc++){
            N= Integer.parseInt(br.readLine());
            graph = new int[N][N];
            int[] arr = new int[N];
            visited= new boolean[N];
            for(int i = 0; i< N; i++){
                arr[i]=i;
                visited[i]= false;
            }
            for(int i = 0; i < N; i++){
                st= new StringTokenizer(br.readLine());
                for(int j = 0; j< N; j++){
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            Best= 500000;
            comb(0,0);
            System.out.printf("#%d %d\n",tc, Best);
            

        }
    }
}