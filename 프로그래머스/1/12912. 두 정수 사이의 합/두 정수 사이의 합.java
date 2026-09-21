import java.util.*;
class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int m = Math.min(a,b);
        int n = Math.max(a,b);
        for(int i = m; i <= n; i++){
            answer+=i;
        }
        return answer;
    }
}