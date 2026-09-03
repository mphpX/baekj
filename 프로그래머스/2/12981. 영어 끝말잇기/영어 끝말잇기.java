import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        Set<String> set = new HashSet<>();
        int cur = 1;
        set.add(words[0]);
        for(int i = 1; i < words.length; i++){
            String word= words[i];
            String prev= words[i-1];
            if(set.contains(word) || prev.charAt(prev.length()-1) != word.charAt(0)){
                answer[0]= cur + 1;
                answer[1]= (int)(i/n) +1;
                break;
            }
            set.add(word);
            cur= (cur+1)%n;
        }

        return answer;
    }
}