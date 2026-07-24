class Solution {
    public long solution(int a, int b) {
        long la= (long)a;
        long lb= (long)b;
        if(a> b){
            long temp = la;
            la= lb;
            lb= temp;
        }
        long answer = 0;
        
        if(la < 0){
            answer-=-la*(-la+1)/2;
            answer+= lb*(lb+1)/2;
        }else{
            answer+= lb*(lb+1)/2;
            answer-= la*(la-1)/2;
        }
        
        return answer;
    }
}