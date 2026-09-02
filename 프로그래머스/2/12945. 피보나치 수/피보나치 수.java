class Solution {
    public int solution(int n) {
        int[] two = {0, 1};
        int cur = 2;
        for(cur = 2; cur <= n; cur+=2){
            two[0] = (two[0] + two[1]) % 1234567;
            two[1] = (two[1] + two[0]) % 1234567;
        }
        return two[n%2];
    }
}