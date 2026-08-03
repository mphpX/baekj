class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean[] is_nt= new boolean[n+1];
        int m = (int)Math.sqrt(n)+1;
        int cur = 0;
        for(int i = 2; i <= m; i++){
            cur = 2;
            while(cur* i <= n){
                is_nt[cur*i]= true;
                cur++;
            }
        }
        for(int i = 2; i <=n; i++){
            if(!is_nt[i]) answer++;
        }
        return answer;
    }
}