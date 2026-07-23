class Solution {
    public int solution(String number) {
        int answer = 0;
        for(char ch: number.toCharArray()){
            answer= (answer+ ch-'0')%9;
        }
        return answer;
    }
}