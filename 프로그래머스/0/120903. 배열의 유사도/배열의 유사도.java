import java.util.*;
class Solution {
    public int solution(String[] s1, String[] s2) {
        Map<String, Integer> mp= new HashMap<>();
        for(String str: s1){
            mp.put(str, 1);
        }
        for(String str: s2){
            mp.put(str, mp.getOrDefault(str, 0) + 1);
        }
        int answer = 0;
        for(String str: mp.keySet()){
            if(mp.get(str)== 2){
                answer++;
            }
        }
        return answer;
    }
}