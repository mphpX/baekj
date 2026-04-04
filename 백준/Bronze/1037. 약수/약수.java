import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st= new StringTokenizer(br.readLine());
        int mn = 1000000;
        int mx = 0;
        int tmp = 0;
        for(int i = 0; i < n; i++){
            tmp = Integer.parseInt(st.nextToken());
            mn= Math.min(tmp, mn);
            mx= Math.max(tmp, mx);
        }
        System.out.println(mx*mn);
        
    }
}
