import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int min_x= 10000;
        int max_x= -10000;
        int min_y= 10000;
        int max_y= -10000;
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            min_x= Math.min(x,min_x);
            max_x= Math.max(x,max_x);
            int y = Integer.parseInt(st.nextToken());
            min_y= Math.min(y,min_y);
            max_y= Math.max(y,max_y);
        }
        System.out.println((max_x- min_x)*(max_y-min_y));
    }
}
