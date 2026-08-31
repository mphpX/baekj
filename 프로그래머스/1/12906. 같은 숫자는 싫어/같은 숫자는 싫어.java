import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        stack.push(arr[0]);
        for(int a: arr){
            if(stack.peek() != a){
                stack.push(a);
            }
        }
        int[] answer= new int[stack.size()];
        int i = 0;
        for(Integer num: stack){
            answer[i++]= num;
        }
        return answer;
    }
}