import java.util.*;
import java.io.*;
public class Main {
    public static int gcd(int a, int b){
        if(a== 0) return b;
        else return gcd(b%a, a);
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String p;
        Stack<Character> stack; 
        char ch;
        boolean isit= true;
        for(int t = 0; t < n; t++){
            p= br.readLine();
            stack= new Stack<>();
            isit = true;
            for(int i = 0; i < p.length(); i++){
                ch= p.charAt(i);
                if(ch == '('){
                    stack.push(ch);
                }else{
                    if(stack.isEmpty()){
                        isit = false;
                        break;
                    }else{
                        stack.pop();
                    }
                }
            }
            if(!isit|| !stack.isEmpty()){
                bw.write("NO\n");
            }else{
                bw.write("YES\n");
            }
        }
        bw.flush();
    }
}
