import java.util.*;
class Solution {
    public int[] solution(int[] num_list, int n) {
        int count = 0;
        int cur = 0;
        for(int i = 0; i < num_list.length; i+=n){
            count++;
        }
        int[] answer = new int[count];
        for(int i = 0; i < num_list.length; i+=n){
            answer[cur++]= num_list[i];
        }
        return answer;
    }
}