class Solution {
    public long solution(long n) {
        double x= Math.sqrt(n);
        long answer = 0;
        if((long)x == x){
            answer= (long)(x) + 1;
            answer*=answer;
        }else{
            answer= -1;
        }
        return answer;
    }
}