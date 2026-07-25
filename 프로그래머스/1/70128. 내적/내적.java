class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        int idx = 0;
        for(;idx < a.length; idx++){
            answer+= a[idx]*b[idx];
        }
        
        return answer;
    }
}