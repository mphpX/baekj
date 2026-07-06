class Solution {
    public int solution(int a, int b) {
        int r = 1;
        int ct = 0;
        while(r <= b){
            r*=10;
            ct++;
        }
        int ans1 = a* ((int)Math.pow(10, ct))+ b;
        r= 1;
        ct= 0;
        while(r <= a){
            r*=10;
            ct++;
        }
        int ans2 = b* ((int)Math.pow(10,ct))+ a;
        return Math.max(ans1,ans2);
        
    }
}