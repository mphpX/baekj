class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int cur = 0;
        int mn;
        for(int[] temp: queries){
            mn= 1000001;
            for(int i = temp[0]; i <=temp[1]; i++){
                if(arr[i]> temp[2] && mn > arr[i]){
                    mn= arr[i];
                }
            }
            if(mn == 1000001){
                mn= -1;
            }
            answer[cur++]= mn;
        }
        return answer;
    }
}