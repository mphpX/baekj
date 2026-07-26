import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> m = new HashMap<>();
        int n = name.length;
        for(int i = 0; i < n ;i++){
            m.put(name[i], yearning[i]);
        }
        for(int i = 0; i < photo.length; i++){
            for(int j = 0; j < photo[i].length; j++){
                if(m.containsKey(photo[i][j])){
                    answer[i]+= m.get(photo[i][j]);
                }
            }
            
        }
        return answer;
    }
}