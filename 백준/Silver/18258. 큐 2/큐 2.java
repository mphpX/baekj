import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        LinkedList<Integer> q = new LinkedList<>(); 
        int n = Integer.parseInt(br.readLine());
        String command;
        int x;
        for(int i = 0; i < n; i++){
            st= new StringTokenizer(br.readLine());
            command = st.nextToken();
            switch (command) {
                case "push":
                    x= Integer.parseInt(st.nextToken());
                    q.add(x);
                    break;
                case "pop":
                    if(q.isEmpty()){
                       bw.write(-1+ "\n");
                    }else{
                        bw.write(q.poll()+ "\n");
                    }
                    break;
                case "size":
                    bw.write(q.size()+ "\n");
                    break;
                case "empty":
                    bw.write(((q.isEmpty()) ? 1 : 0)+ "\n");
                    break;
                case "front":
                    bw.write(((q.isEmpty()) ? -1 : q.peek())+ "\n");   
                    break;                 
                case "back":
                    bw.write(((q.isEmpty()) ? -1 : q.peekLast())+ "\n");
                    break;
                default:
                    break;
            }
        }
        bw.flush();
    }
}