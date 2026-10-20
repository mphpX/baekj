class Solution {
    public int solution(int hp) {
        int answer = 0;
        int[] attack = {5, 3, 1};
        int cur = 0;
        while(hp% attack[cur] != 0){
            answer+= (int)(hp / attack[cur]);
            hp-= (int)(hp / attack[cur]) * attack[cur];
            cur++;
        }
        if(hp != 0){
            answer+= (int)(hp / attack[cur]);
        }
        return answer;
    }
}