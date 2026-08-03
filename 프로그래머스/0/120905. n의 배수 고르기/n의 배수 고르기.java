class Solution {
    public int[] solution(int n, int[] numlist) {
        int count = 0;
        for(int i: numlist){
            if(i% n == 0) count++;
        }
        int[] answer = new int[count];
        int cur = 0;
        for(int i : numlist){
            if(i% n==0) answer[cur++]= i;
        }
        return answer;
    }
}