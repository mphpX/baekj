import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int d = 2;
        while(n >= d){
            if(n%d ==0){
                bw.write(Integer.toString(d));
                bw.write('\n');
                n/= d;
            }else{
                d+=1;
            }
        }
        bw.flush();
    }
}
