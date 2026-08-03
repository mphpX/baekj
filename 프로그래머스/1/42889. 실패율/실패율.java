import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] human = new int[N+2];
        int m= stages.length;
        
        for(int i: stages){
            human[i]++;
        }
        double[] fail_rate= new double[N+2];
        for(int i= 1; i <=N; i++){
            fail_rate[i]= (double)(human[i])/(double)m;
            m-= human[i];
            if(m == 0) break;
        }
        PriorityQueue<double[]> pq= new PriorityQueue<>((o1, o2) -> {
            if(o1[1]== o2[1]) return Double.compare(o1[0], o2[0]);
            return Double.compare(o2[1], o1[1]);
        });
        for(int i = 1; i<= N; i++){
            pq.add(new double[]{(double)(i), fail_rate[i]});
        }
        for(int i = 0; i<N; i++){
            answer[i]= (int)pq.poll()[0];
        }
        return answer;
    }
}