class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i = left; i <= right; i++){
            int ct = 1;
            for(int j = 2; j <= i; j++){
                if(i% j ==0){
                    ct+=1;
                }
            }
            if(ct% 2 == 0){
                answer+= i;
            }else{
                answer-= i;
            }
        }
        return answer;
    }
}