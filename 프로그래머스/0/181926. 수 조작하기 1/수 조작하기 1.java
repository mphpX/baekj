class Solution {
    public int solution(int n, String control) {
        int answer = n;
        for(char i : control.toCharArray()){
            if(i== 'w'){
                answer+=1;
            }else if(i== 's'){
                answer-=1;
            }else if(i=='d'){
                answer+=10;
            }else{
                answer-=10;
            }
        }
        return answer;
    }
}