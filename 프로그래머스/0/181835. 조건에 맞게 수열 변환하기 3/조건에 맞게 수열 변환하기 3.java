class Solution {
    public int[] solution(int[] arr, int k) {
        int n = arr.length;
        int[] answer = new int[arr.length];
        if(k%2 ==0){
            for(int i = 0; i < n; i++){
                answer[i]= k+ arr[i];
            }
        }else{
            for(int i = 0; i < n; i++){
                answer[i]= k*arr[i];
            }   
        }
        
        return answer;
    }
}