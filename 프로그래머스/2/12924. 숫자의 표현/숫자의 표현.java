class Solution {
    public int solution(int n) {
        int answer = 0;
        int left= 0;
        int right= 1;
        int cur = 1;
        while(left < right && right < n){
            if(cur == n){
                answer+=1;
                right+=1;
                cur+=right;
            }else if(cur < n){
                right+=1;
                cur+=right;
            }else{
                cur-=left;
                left+=1;
            }
        }
        return answer+1;
    }
}