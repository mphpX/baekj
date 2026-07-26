class Solution {
    public String solution(int a, int b) {
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] day= {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int diff= 0;
        for(int i = 0; i < a-1; i++){
            diff+= month[i];
        }
        diff+= b-1;
        String answer = day[diff%7];
        return answer;
    }
}