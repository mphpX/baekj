class Solution {
    public double solution(int[] numbers) {
        double ans = 0;
        for(int x : numbers) ans+= x;
        return ans/numbers.length;
    }
}