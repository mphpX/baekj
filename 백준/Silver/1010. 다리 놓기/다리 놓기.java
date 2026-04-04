import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        for(int tc = 0; tc < t; tc++){
            st = new StringTokenizer(br.readLine());
            long n = Long.parseLong(st.nextToken());
            long m = Long.parseLong(st.nextToken());
            n= Math.min(n, m-n);
            long ans = 1;
            for(long i = 0; i < n; i++){
                ans*= m-i;
            }
            for(long i = 2; i <= n; i++){
                ans/=i;
            }
            bw.write(ans+ "\n");
        }
        bw.flush();
        
    }
}
