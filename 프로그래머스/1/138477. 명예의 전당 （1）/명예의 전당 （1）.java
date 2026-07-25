import java.util.*;
class Solution {
    public int[] solution(int k, int[] score) {
        int n = score.length;
        int[] answer = new int[n];
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> a - b);
        for(int i = 0; i < n; i++){
            if(pq.size() < k){
                pq.offer(score[i]);
                answer[i]= pq.poll();
                pq.offer(answer[i]);
            }else{
                pq.offer(score[i]);
                pq.poll();
                answer[i]= pq.poll();
                pq.offer(answer[i]);
            }
            
        }
        
        return answer;
    }
}