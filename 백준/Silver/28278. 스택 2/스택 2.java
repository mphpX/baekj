import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Stack<Integer> stack = new Stack<Integer>(); 
        int n = Integer.parseInt(br.readLine());
        int command;
        int x;
        for(int i = 0; i < n; i++){
            st= new StringTokenizer(br.readLine());
            command = Integer.parseInt(st.nextToken());
            switch (command) {
                case 1:
                    x= Integer.parseInt(st.nextToken());
                    stack.push(x);
                    break;
                case 2:
                    if(stack.isEmpty()){
                        System.out.println(-1);
                    }else{
                        System.out.println(stack.pop());
                    }
                    break;
                case 3:
                    System.out.println(stack.size());
                    break;
                case 4:
                    System.out.println((stack.isEmpty()) ? 1 : 0);
                    break;
                case 5:
                    System.out.println((stack.isEmpty()) ? -1 : stack.peek());                    
                default:
                    break;
            }
        }
    }
}
