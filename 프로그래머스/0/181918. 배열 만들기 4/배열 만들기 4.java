import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> stk = new ArrayDeque<>();
        int i= 0;
        int cur;
        while(i < arr.length){
            if(stk.size()== 0){
                stk.addLast(arr[i]);
                i+=1;
            }else{
                cur = stk.peekLast();
                if(cur < arr[i]){
                    stk.addLast(arr[i]);
                    i+=1;
                }else{
                    stk.pollLast();
                }
            }    
        }
        int[] answer = new int[stk.size()];
        int idx = 0;
        for(int temp : stk){
            answer[idx++]= temp; 
        }
        return answer;
    }
}