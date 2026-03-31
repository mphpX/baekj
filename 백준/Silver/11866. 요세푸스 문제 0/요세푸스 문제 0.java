import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Queue<Integer> q = new LinkedList<>();
        bw.write("<");
        for(int i = 1; i <= n; i++){
            q.offer(i);
        }
        for(int i = 0 ; i < n-1; i++){
            for(int j = 0; j < m-1; j++){
                q.offer(q.poll());
            }
            bw.write(q.poll()+ ", ");
        }
        bw.write(q.poll()+"");
        bw.write(">");
        bw.flush();
    }
}