class Solution {
    public int solution(int[] box, int n) {
        int answer = 1;
        for(int x : box){
            answer *=(int)(x/n);
        }
        return answer;
    }
}