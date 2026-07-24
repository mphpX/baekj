class Solution {
    public int[] solution(long n) {
        long x= n;
        int ct =0;
        while(x>0){
            x/=10;
            ct+=1;
        }
        int[] answer = new int[ct];
        x= n;
        int idx= 0;
        while(x>0){
            answer[idx++]= (int)(x%10);
            x/=10;
        }
        return answer;
    }
}