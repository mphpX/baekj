import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x= 0;
        int y= 0;
        for(int i = 0; i < 3; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = x ^ Integer.parseInt(st.nextToken());
            y = y ^ Integer.parseInt(st.nextToken());
        }
        System.out.println(x + " " + y);

    }
}