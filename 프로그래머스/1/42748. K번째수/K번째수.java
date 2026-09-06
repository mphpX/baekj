import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++){
            List<Integer> ls = new ArrayList<>();
            for(int j = commands[i][0]-1; j < commands[i][1]; j++){
                ls.add(array[j]);
            }
            ls.sort(Comparator.naturalOrder());
            answer[i]= ls.get(commands[i][2]-1);
        }
        return answer;
    }
}