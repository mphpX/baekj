import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[] sorq= new int[n];
        Deque<Integer> dq = new ArrayDeque<>();
        st= new StringTokenizer(br.readLine());
        int ct = 0;
        for(int i = 0; i < n; i++){
            sorq[i]= Integer.parseInt(st.nextToken());
        }
        int[] arr = new int[n];
        st= new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            arr[i]= Integer.parseInt(st.nextToken());
            if(sorq[i]==0){
                ct++;
                dq.addLast(arr[i]);
            }
        }
        int m = Integer.parseInt(br.readLine());
        int[] plus = new int[m];
        st= new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++){
            plus[i]= Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i <m ; i++){
            dq.addFirst(plus[i]);
            bw.write(dq.pollLast() + " ");
        }
        bw.flush();
    }
}
