class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int n = numbers.length;
        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                answer= Math.max(numbers[i]*numbers[j], answer);
            }
        }
        return answer;
    }
}