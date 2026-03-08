import java.util.*;
import java.io.*;
public class Main {
    public static int gcd(int a, int b){
        if(a== 0) return b;
        else return gcd(b%a, a);
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[2];
        for(int i = 0; i < 2; i++){
            a[i]= Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int[] b = new int[2];
        for(int i = 0; i < 2; i++){
            b[i]= Integer.parseInt(st.nextToken());
        }
        int c= a[0]*b[1]+ b[0]* a[1];
        int d= a[1]*b[1];
        int mul= gcd(Math.min(c,d), Math.max(c,d));
        System.out.printf("%d %d", c/mul, d/mul);
    }
}