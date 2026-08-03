class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        boolean[] isnt_p = new boolean[3001];
        int m = (int)Math.sqrt(3000) +1;
        int n = nums.length;
        int cur = 2;
        for(int i = 2; i <= m; i++){
            cur= 2;
            while(i* cur <= 3000){
                isnt_p[i*cur] = true;
                cur++;
            }
        }
        int s = 0;
        for(int i = 0; i< n; i++){
            for(int j = i+1; j <n; j++){
                for(int k = j+1; k < n; k++){
                    s= nums[i]+ nums[j]+ nums[k];
                    if(!isnt_p[s]) answer++;
                }
            }
        }
        return answer;
    }
}