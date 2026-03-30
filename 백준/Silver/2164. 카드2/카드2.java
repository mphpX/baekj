import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = (int)(n/2)*2;
        ArrayDeque<Integer> arrayDeque = new ArrayDeque<>();
        if(n==1)System.out.println(1);
        else{
            for(int i = (1 + (n%2))*2; i <= ans; i+=2){
                arrayDeque.addLast(i);
            }
            if(n%2==1) arrayDeque.addLast(2);
            int x = arrayDeque.size();
            while(x!=1){
                arrayDeque.pollFirst();
                x-=1;
                if(x==1) break;
                arrayDeque.addLast(arrayDeque.pollFirst());
            }
            System.out.println(arrayDeque.poll());
        }
    }
}
