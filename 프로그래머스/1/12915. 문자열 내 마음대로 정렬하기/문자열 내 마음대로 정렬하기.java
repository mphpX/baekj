import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = strings;
        
        Arrays.sort(answer, (o1, o2) -> {
            if(o1.charAt(n)== o2.charAt(n)){
                return o1.compareTo(o2);
            }
            return Character.compare(o1.charAt(n), o2.charAt(n));
            });
        
        return answer;
    }
}