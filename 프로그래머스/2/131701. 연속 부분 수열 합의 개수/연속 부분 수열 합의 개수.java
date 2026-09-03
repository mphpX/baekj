import java.util.*;
class Solution {
    public int solution(int[] elements) {
        Map<Integer, Integer> map= new HashMap<>();
        
        int answer = 0;
        int cur = 0;
        int n = elements.length;
        for(int i = 0; i < n; i++){
            cur = 0;
            for(int j = 0; j < n- 1; j++){
                cur+= elements[(i+ j)%n];
                map.put(cur, map.getOrDefault(cur, 0) + 1);
            }   
        }
        return map.size() + 1;
    }
}