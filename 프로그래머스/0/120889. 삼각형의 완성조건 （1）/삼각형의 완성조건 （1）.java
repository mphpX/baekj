import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        List<Integer> l = new ArrayList<>();
        for(int i : sides){
            l.add(i);
        }
        l.sort((o1, o2) -> {
            return o1-o2;
        });
        if(l.get(0)+ l.get(1) > l.get(2)){
            return 1;
        }
        return 2;
    }
}