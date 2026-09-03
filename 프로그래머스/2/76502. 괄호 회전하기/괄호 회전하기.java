import java.util.*;
class Solution {
    public int solution(String s) {
        int n = s.length();
        char[] x = {'(', '[', '{'};
        char[] y = {')', ']', '}'};
        int answer = 0;
        for(int i = 0; i < n; i++){
            Stack<Character> stack= new Stack<>();
            boolean valid = false;
            for(int j = 0; j < n; j++){
                int idx= (i+j) % n;
                for(int k = 0; k < 3; k++){ // 괄호 가능?
                    if(x[k]== s.charAt(idx)){
                        stack.push(x[k]);
                        valid = true;
                        break;
                    }
                    else if(stack.size() != 0 && x[k]== stack.peek() && y[k]== s.charAt(idx)){         
                        stack.pop();
                        valid = true;
                        break;
                    }
                }
            }
            if(valid && stack.size()==0) answer++;
        }

        return answer;
    }
}