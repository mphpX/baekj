import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr= new int[3];
        int idx = 0;
        int mx = 0;
        for(int i = 0; i < 3; i++){
            arr[i]= Integer.parseInt(st.nextToken());
            if(mx < arr[i]){
                mx= arr[i];
                idx = i;
            }
        }
        int total = 0;
        for(int i = 0; i < 3; i++){
            if(i==idx) continue;
            total+= arr[i];
        }
        while(total<= mx){
            mx--;
        }
        System.out.println(mx+total);
    }
}
