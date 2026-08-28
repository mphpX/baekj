class Solution {
    public int[] solution(int[] num_list) {
        int temp = 0; // swap 할 때 쓸 임시 공간.
        int n = num_list.length; // 요소 갯수.
        
        // 오름차순. bubble sort 
        for(int i = 0; i < n; i++){ // 1.
            for(int j = 1; j < n- i; j++){ // 2. 
                if(num_list[j-1] > num_list[j]){ // 3.
                    temp = num_list[j-1];
                    num_list[j-1]= num_list[j];
                    num_list[j]= temp;
                }
            } 
        }
        int[] answer = new int[5];
        for(int i = 0; i < 5; i++){
            answer[i]= num_list[i];
        }
        return answer;
    }
}