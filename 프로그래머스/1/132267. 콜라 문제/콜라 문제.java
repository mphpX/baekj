class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int left = 0;
        int cur = n;
        int plus = 0;
        while(cur >= a){
            left+= cur% a;
            plus = (cur/ a)* b;
            answer+= plus;
            cur= plus + left;
            left = 0;
        }
        return answer;
    }
}