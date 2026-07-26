import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothing= new HashMap<>();
        for(int i = 0; i< clothes.length; i++){
            clothing.put(clothes[i][1], clothing.getOrDefault(clothes[i][1], 0) + 1);
        }
        int answer = 1;
        for(int v: clothing.values()){
            answer*=(v+1);
        }
        
        return answer-1;
    }
}