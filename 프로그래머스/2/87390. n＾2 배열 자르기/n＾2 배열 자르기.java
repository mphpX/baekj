class Solution {
    public int[] solution(int n, long left, long right) {
        // idx를 x y 좌표로 바꾸기.
        int cur_x;
        int cur_y;
        int[] answer = new int[(int)(right- left) + 1];
        long cur= left;
        int idx = 0;
        while(cur <= right){
            cur_x = (int) (cur / n);
            cur_y = (int) (cur % n);
            answer[idx++]= Math.max(cur_x, cur_y)+1;
            cur++;
        }
        
        return answer;
    }
}