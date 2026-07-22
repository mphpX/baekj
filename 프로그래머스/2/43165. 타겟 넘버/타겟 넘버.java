class Solution {
    int answer = 0;
    public void btk(int[] numbers, int idx, int cur, int target){
        if(idx == numbers.length){
            if(cur == target){
                answer++;
            }
            return;
        }
        btk(numbers, idx+1, cur+ numbers[idx], target);
        btk(numbers, idx+1, cur- numbers[idx], target);
    }
    public int solution(int[] numbers, int target) {
        btk(numbers, 0, 0, target);
        return answer;
    }
}