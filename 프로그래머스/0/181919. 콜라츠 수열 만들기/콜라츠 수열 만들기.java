import java.util.*;
class Solution {
    public int[] solution(int n) {
        Deque<Integer> dq = new ArrayDeque<>();
        int cur = n;
        while(cur != 1){
            dq.add(cur);
            if(cur%2==0){
                cur/=2;
            }else{
                cur= 3*cur+1;
            }
        }
        dq.add(1);
        int[] answer= new int[dq.size()];
        int idx = 0;
        for(int temp: dq){
            answer[idx++]= temp;
        }
        
        return answer;
    }
}