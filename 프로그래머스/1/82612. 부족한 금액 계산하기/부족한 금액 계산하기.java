class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long cur = 0;
        for(int i = 0; i < count; i++){
            cur+= price;
            answer+= cur;
        }
        
        return Math.max(answer- (long)(money), 0);
    }
}