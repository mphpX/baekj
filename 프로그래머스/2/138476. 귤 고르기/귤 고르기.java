import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map= new HashMap<>();
        for(int i: tangerine){
            map.put(i, map.getOrDefault(i, 0)+1);
        }
        int sz;
        int ct;
        Queue<int[]> pq = new PriorityQueue<>((a, b)->{
            if(a[1]== b[1]){
                return b[0]- a[0];
            }
            return b[1]- a[1];
        });
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            sz = entry.getKey();
            ct = entry.getValue();
            pq.add(new int[] {sz, ct});
        }
        
        while(k > 0){
            int[] xy= pq.poll();
            k-=xy[1];
            answer++;
        }
        return answer;
    }
}