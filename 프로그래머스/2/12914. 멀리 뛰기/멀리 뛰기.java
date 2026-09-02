class Solution {
    public long solution(int n) {
        long[] two = {1, 2};
        for(int i = 3; i <= n; i+=2){
            two[0]= (two[0]+two[1]) % 1234567;
            two[1]= (two[0]+two[1]) % 1234567;
        }
        return two[(n+1)%2];
    }
}