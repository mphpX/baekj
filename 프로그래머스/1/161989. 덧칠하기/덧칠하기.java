import java.util.*;
class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int idx = 0;
        int l= section.length;
        int cur = section[0]- 1;
        while(idx < l){
            if(cur < section[idx]) {
                cur= section[idx]+ m -1;
                answer+=1;
            }else{
                idx++;
            }
        }
        return answer;
    }
}