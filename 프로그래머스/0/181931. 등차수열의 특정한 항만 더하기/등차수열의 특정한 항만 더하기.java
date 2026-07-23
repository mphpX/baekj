class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int cur= a;
        for(boolean isit: included){
            if(isit){
                answer+= cur;
            }
            cur+=d;
        }
        return answer;
    }
}