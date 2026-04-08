import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String my = br.readLine();
        String doc = br.readLine();
        if(my.length() >= doc.length()){
            System.out.println("go");
        }else{
            System.out.println("no");
        }
        
    }
}
