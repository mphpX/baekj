import java.util.*;
class Solution {
    public String solution(String s) {
        List<Character> arr = new ArrayList<>();
        for(char ch : s.toCharArray()){
            arr.add(ch);
        }
        arr.sort(Comparator.reverseOrder());
        StringBuilder answer = new StringBuilder();
        for(char ch: arr){
            answer.append(ch);
        }
        
        return answer.toString();
    }
}