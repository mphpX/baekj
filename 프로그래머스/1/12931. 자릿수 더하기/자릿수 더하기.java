import java.util.*;

public class Solution {
    public int solution(int n) {
        int temp = n;
        int answer = 0;
        while(temp>0){
            answer+= temp%10;
            temp/=10;
        }

        return answer;
    }
}