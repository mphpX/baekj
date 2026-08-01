import java.util.*;
class Solution {
    public int solution(int k, int m, int[] score) {
        List<Integer> scores = new ArrayList<>();
        for(int i : score){
            scores.add(i);
        }
        scores.sort((o1, o2) -> {
            return Integer.compare(o1,o2);
        });
        int n = score.length;
        int start = n - (int)(n / m) *m;
        int answer = 0;
        for(; start < n; start= start+m){
            answer+= scores.get(start) * m;
        }
        
        return answer;
    }
}