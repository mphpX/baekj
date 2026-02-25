import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        String str;
        while((str = br.readLine()) != null){
            st= new StringTokenizer(str);;
            int a= Integer.parseInt(st.nextToken());
            int b= Integer.parseInt(st.nextToken());
            bw.write(Integer.toString(a+b));
            bw.write("\n");
        }
        bw.flush();
    }
}
