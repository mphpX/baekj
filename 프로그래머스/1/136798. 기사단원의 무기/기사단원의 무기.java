class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 1;
        int ct= 2;
        for(int i = 2; i <= number; i++){
            ct= 2;
            for(int j = 2; j < i; j++){
                if(i%j == 0) ct++;
            }
            if(ct > limit) ct= power;
            answer+= ct;
        }
        return answer;
    }
}