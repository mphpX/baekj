import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        List<Integer> sort_d= new ArrayList<>();
        for(int i = 0; i < d.length; i++){
            sort_d.add(d[i]);
        }
        sort_d.sort(Comparator.naturalOrder());
        int cur = budget;
        int answer = 0;
        for(int i: sort_d){
            if(cur-i>=0){
                answer+=1;
                cur-= i;
            }
        }
        
        return answer;
    }
}