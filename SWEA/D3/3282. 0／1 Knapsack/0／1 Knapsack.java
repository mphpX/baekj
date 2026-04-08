import java.util.*;
import java.io.*;
public class Solution{
    public static class Pack{
        int v;
        int c;
        Pack(int v, int c){
            this.v = v;
            this.c = c;
        }
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t= Integer.parseInt(br.readLine());
        int n, k;
        Pack[] ps;
        int[][] dp;
        for(int tc = 1; tc <= t; tc++){
            st= new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            ps = new Pack[n];
            dp = new int[n][k+1];
            for(int i = 0; i < n; i++){
                st= new StringTokenizer(br.readLine());
                ps[i]= new Pack(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            for(int j = 0; j< k+1; j++){
                if(ps[0].v <= j) dp[0][j]= ps[0].c;
            }
            for(int i = 1; i < n; i++){
                for(int j = 1; j <= k; j++){
                    if(j < ps[i].v){
                        dp[i][j]= dp[i-1][j];
                    }else{
                        dp[i][j]= Math.max(dp[i-1][j], dp[i-1][j- ps[i].v]+ ps[i].c);
                    }
                }
            }
            bw.write("#"+tc+" "+dp[n-1][k]+"\n");
        }
        bw.flush();
        
    }
}
