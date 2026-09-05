import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> {
            return a - b;
        });
        for(int sco : scoville){
            pq.offer(sco);
        }
        int[] plus = new int[2];
        int cur = 0;
        while(pq.size() >= 2 && pq.peek() < K){
            plus[0]= pq.poll();
            plus[1]= pq.poll();
            cur= plus[0] + 2* plus[1];
            pq.offer(cur);
            answer++;
        }
        if(pq.peek() < K){
            answer= -1;
        }
        return answer;
    }
}