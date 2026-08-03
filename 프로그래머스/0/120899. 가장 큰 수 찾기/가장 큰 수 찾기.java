class Solution {
    public int[] solution(int[] array) {
        int n = array.length;
        int mx = 0;
        int idx = 0;
        for(int i = 0; i < n; i++){
            if(array[i] > mx){
                mx= array[i];
                idx= i;
            }
        }
        return new int[] {mx, idx};
    }
}