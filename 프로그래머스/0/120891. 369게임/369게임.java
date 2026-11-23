class Solution {
    public int solution(int order) {
        int answer = 0;
        int cur = 0;
        while(order > 0){
            cur= order % 10;
            if(cur > 0 && cur % 3 ==0){
                answer++;
            }
            order/=10;
        }
        return answer;
    }
}