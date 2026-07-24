import java.util.*;
class Solution {
    public int[] solution(int n) {
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i = 1; i <=n; i++){
            if(i%2 == 1){
                dq.add(i);
            }
        }
        int[] answer = new int[dq.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i]= dq.poll();
        }
        return answer;
    }
}