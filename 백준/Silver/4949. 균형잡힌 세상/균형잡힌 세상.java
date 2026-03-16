import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String p;
        Stack<Character> stack;
        boolean isit;

        while (true) {
            p = br.readLine();

            if (p.equals(".")) {
                break;
            }

            stack = new Stack<>();
            isit = true;

            for (int i = 0; i < p.length(); i++) {
                char ch = p.charAt(i);

                if (ch == '(' || ch == '[') {
                    stack.push(ch);
                } else if (ch == ')') {
                    if (stack.isEmpty() || stack.peek() != '(') {
                        isit = false;
                        break;
                    }
                    stack.pop();
                } else if (ch == ']') {
                    if (stack.isEmpty() || stack.peek() != '[') {
                        isit = false;
                        break;
                    }
                    stack.pop();
                }
            }

            if (!isit || !stack.isEmpty()) {
                bw.write("no\n");
            } else {
                bw.write("yes\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}