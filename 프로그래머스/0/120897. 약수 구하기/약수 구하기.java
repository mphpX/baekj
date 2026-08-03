import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> childs= new ArrayList<>();
        for(int i = 1; i <= n; i++){
            if(n%i == 0) childs.add(i);
        }
        int[] answer = new int[childs.size()];
        for(int i = 0; i < childs.size(); i++){
            answer[i]= childs.get(i);
        }
        return answer;
    }
}