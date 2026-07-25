import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> nums = new ArrayList<>();
        for(int i : arr){
            if(i%divisor == 0){
                nums.add(i);
            }
        }
        nums.sort(Comparator.naturalOrder());
        int[] answer = new int[nums.size()];
        int idx = 0;
        for(int i : nums){
            answer[idx++]= i;
        }
        if(answer.length == 0){
            answer= new int[] {-1};
        }
        return answer;
    }
}