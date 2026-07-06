class Solution {
    public int solution(String my_string, String target) {
        int answer = 1;
        int i = 0;
        int m = my_string.length();
        int t = target.length();
        if(m<t){
            return 0;
        }
        while(i < m-t+1){
            answer= 1;
            for(int j= 0; j < t; j++){
                if(my_string.charAt(i+j)== target.charAt(j)){
                    continue;
                }else{
                    answer= 0;
                    break;
                }
            }
            if(answer == 1) return answer;
            i++;
        }
        return answer;
    }
}