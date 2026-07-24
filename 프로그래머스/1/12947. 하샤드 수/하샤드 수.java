class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sm = 0;
        int temp= x;
        while(temp>0){
            sm+= temp%10;
            temp/=10;
        }
        return x%sm == 0;
    }
}