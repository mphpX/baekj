import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i < want.length; i++){
            map.put(want[i], 0);
        }
        for(int i = 0; i < 10; i++){
            map.put(discount[i], map.getOrDefault(discount[i], 0)+1);
        }
        boolean isit= true;
        for(int i = 0; i < want.length; i++){
            if(map.getOrDefault(want[i], 0) != number[i]){
                isit= false;
                break;
            }
        }
        if(isit) answer++;
        for(int i = 1; i < discount.length - 9; i++){
            map.put(discount[i-1], map.getOrDefault(discount[i-1], 0) - 1);
            map.put(discount[i+9], map.getOrDefault(discount[i+9], 0) + 1);
            isit= true;
            for(int j = 0; j < want.length; j++){
                if(map.getOrDefault(want[j], 0) != number[j]){
                    isit= false;
                    break;
                }
            }
            if(isit) answer++;
        }
        return answer;
    }
}