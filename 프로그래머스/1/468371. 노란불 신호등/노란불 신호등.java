class Solution {
    public int gcd(int a, int b){
        if(b == 0) return a;
        return gcd(b, a%b);
    }
    
    public int lcm(int a, int b){
        return a/gcd(a, b) * b;
    }
    
    public int solution(int[][] signals) {
        int n = signals.length;
        int[] cycle = new int[n];
        int totalCycle = 1;
        for(int i = 0; i < n;i++){
            cycle[i] = signals[i][0] + signals[i][1] + signals[i][2];
            totalCycle = lcm(cycle[i], totalCycle);
        }
        //후보 시간이 가장 적은 신호등 선택.
        int baseIdx = 0;
        int minCandidate = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++){
            int candidate = totalCycle / cycle[i] * signals[i][1];
            if(candidate < minCandidate){
                    minCandidate = candidate;
                    baseIdx = i;
            }
        }
        int baseG = signals[baseIdx][0];
        int baseY = signals[baseIdx][1];
        int baseR = signals[baseIdx][2];
        int baseCycle = cycle[baseIdx];
        for(int cur = baseG; cur < totalCycle; cur+= baseCycle){
            for(int offset = cur; offset < cur + baseY; offset++){
                boolean allYellow = true;
                for(int i = 0; i < n; i++){
                    int pos = offset % cycle[i];
                    int g = signals[i][0];
                    int y = signals[i][1];
                    if(! ((g <= pos) && (pos < g+y))){
                        allYellow= false;
                        break;
                    }
                }
                if(allYellow){
                    return offset+1;
                }
            }
        }
        return -1;
    }
}