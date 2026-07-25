class Solution {
    public int solution(int n) {
        long th = 0;
        long cur = (long)n;
        long answer = 0;
        while(cur >0){
            th += cur % 3;
            th*=10;
            cur/= 3;
        }
        th/= 10;
        long d = 1;
        while(th > 0){
            answer+= d* (th%10);
            d*=3;
            th/=10;
        }
        return (int)answer;
    }
}