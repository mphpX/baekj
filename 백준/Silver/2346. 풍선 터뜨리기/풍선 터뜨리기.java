import java.util.*;
import java.io.*;
public class Main {
    static class Balloon {
        int idx;
        int move;
        Balloon(int idx, int move){
            this.idx = idx;
            this.move = move;
        }
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st= new StringTokenizer(br.readLine());
        Deque<Balloon> dq = new ArrayDeque<>();
        Balloon cur;
        for(int i = 0; i < n; i++){
            dq.addLast(new Balloon(i+1,Integer.parseInt(st.nextToken())));
        }
        cur = dq.poll();
        n-=1;
        bw.write(cur.idx + " ");
        while(dq.size() != 0){
            int move = cur.move;
            if(move > 0){
                move-=1;
                move%= n;
                for(int i = 0 ; i < move; i++){
                    dq.addLast(dq.poll());
                }
            }else{
                move= -move;
                move%= n;
                for(int i = 0 ; i < move; i++){
                    dq.addFirst(dq.pollLast());
                }
            }
            cur = dq.poll();
            n-=1;
            bw.write(cur.idx + " ");
        }
        bw.flush();
    }
}
