class Solution {
    public int solution(int n) {
        int cur = n;
        int answer = 0;
        while(cur > 0){
            answer+= cur%10;
            cur/=10;
        }
        return answer;
    }
}