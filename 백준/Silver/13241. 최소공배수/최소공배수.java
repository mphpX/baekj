import java.util.*;
import java.io.*;
public class Main {
    public static long gcd(long a, long b){
        if(a == 0) return b;
        else return gcd(b%a, a);
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[2];
        for(int i = 0; i < 2; i++){
            arr[i]= Long.parseLong(st.nextToken());
        }
        long mn = Math.min(arr[0], arr[1]);
        long mx = Math.max(arr[0], arr[1]);
        System.out.println(mn/gcd(mn,mx)*mx);
    }
}
