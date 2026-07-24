import java.util.*;
class Solution {
    public long solution(long n) {
        long temp = n;
        long answer = 0;
        ArrayList<Integer> arr= new ArrayList<>();
        while(temp>0){
            arr.add((int)(temp%10));
            temp/=10;
        }
        arr.sort(Comparator.reverseOrder());
        int idx = 0;
        while(idx < arr.size()){
            answer+= arr.get(idx++);
            answer*=10;
        }
        answer/=10;
        
        
        return answer;
    }
}