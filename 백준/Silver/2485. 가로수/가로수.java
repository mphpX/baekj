import java.util.*;
import java.io.*;
public class Main {
    public static int gcd(int a, int b){
        if(a== 0) return b;
        else return gcd(b%a, a);
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] lights = new int[n];
        for(int i = 0; i < n; i++){
            lights[i]= Integer.parseInt(br.readLine());
        }
        int a = lights[1]- lights[0];
        for(int i = 2; i < n; i++){
            int b = lights[i]- lights[i-1];
            a= gcd(Math.min(a,b), Math.max(a,b));
        }
        int ans = 0;
        for(int i = 1; i < n; i++){
            int b = lights[i]- lights[i-1];
            ans+= b/a-1;
        }
        System.out.println(ans);
    }
}