class Solution {
    public int[] solution(int[] arr) {
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            count+= arr[i];
        }
        int cur = 0;
         int[] answer = new int[count];
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i]; j++){
                answer[cur++]= arr[i];
            }
        }
        
        return answer;
    }
}