class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        for(int[] swap : queries){
            int temp = answer[swap[0]];
            answer[swap[0]]= answer[swap[1]];
            answer[swap[1]]= temp;
        }
        return answer;
    }
}