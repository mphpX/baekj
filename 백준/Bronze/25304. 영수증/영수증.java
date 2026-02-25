import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int total = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int ans = 0;
        for(int i = 0; i < n; i++){
            st= new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            total-= a*b;
        }
        System.out.println((total==0) ? "Yes": "No");
    }
}
