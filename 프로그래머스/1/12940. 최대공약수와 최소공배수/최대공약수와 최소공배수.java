class Solution {
    public int gcd(int a, int b){
        if(a == 0) return b;
        return gcd(b%a, a);
    }
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        if(n > m){
            answer[0]= gcd(m, n);
        }else{
            answer[0]= gcd(n, m);
        }
        answer[1]= n*m / answer[0];
        return answer;
    }
}