import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] dice = new int[7];
        dice[a]+=1; dice[b]+=1; dice[c]+=1; dice[d]+=1;
        int ct = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i= 1; i<7; i++){
            if(dice[i]>0) {
                ct+=1;
                dq.add(i);
            }
        }
        if(ct == 1){
            answer= 1111 * dq.pollLast();
        }else if(ct == 2){
            int p,q;
            if(dice[dq.peekLast()]==2){
                p= dq.pollLast();
                q= dq.pollLast();
                answer= (p+q)*(p-q);
            }else{
                p= dq.pollLast();
                q= dq.pollLast();
                if(dice[q]==3){
                    answer= 10*q+p;
                }else{
                    answer= 10*p+q;
                }
                answer*=answer;
            } 
        }else if(ct ==4){
            answer = dq.poll();
        }else{
            answer = 1;
            while(dq.size()!=0){
                int x= dq.poll();
                if(dice[x]== 1){
                    answer*= x;
                }
            }
        }
        return answer;
    }
}