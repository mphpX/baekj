import java.util.*;
class Solution{
    public int solution(String s)
    {
        int answer = 0;
        Stack<Character> stack= new Stack<>();
        char[] char_s= s.toCharArray();
        for(char ch: char_s){
            if(stack.isEmpty()){
                stack.push(ch);
            }else{
                if(ch== stack.peek()){
                    stack.pop();
                }else{
                    stack.push(ch); 
                }
            }
        }
        if(stack.size()==0){
            answer = 1;
        }
        
        return answer;
    }
}