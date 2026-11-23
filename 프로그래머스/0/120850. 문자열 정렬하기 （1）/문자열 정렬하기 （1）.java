import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        int ct = 0;
        for(int i = 0; i < my_string.length(); i++){
            if(Character.isDigit(my_string.charAt(i))){
                ct++;
            }
        }
        int[] answer = new int[ct];
        ct =0;
        for(int i = 0; i < my_string.length(); i++){
            if(Character.isDigit(my_string.charAt(i))){
                answer[ct++]= (my_string.charAt(i)- '0');
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}