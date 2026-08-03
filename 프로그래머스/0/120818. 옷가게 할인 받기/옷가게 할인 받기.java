class Solution {
    public int solution(int price) {
        double mul= 1;
        if(price >= 500000){
            mul= 0.8;
        }else if( price >= 300000){
            mul= 0.9;
        }else if(price >= 100000){
            mul= 0.95;
        }
        return (int)(price* mul);
    }
}