import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int oneCt= 0; // 1 갯수
        int m = n;
        List<Integer> bin= new ArrayList<>();
     
        //이진법 변환
        while(m> 0){
            bin.add(m%2);
            if(m%2 ==1){ //1 갯수 세기
                oneCt+=1;
            }
            m/=2;
        }   
        bin.add(0);
        int right= 0;
        int consecCt= 0;
        for(int i = 1; i < bin.size(); i++){
            if(bin.get(i)== 0 && bin.get(i-1)==1){
                bin.set(i-1, 0);
                bin.set(i,1);
                right= i;
                break;
            }
        }
        for(int i = right; i < bin.size(); i++){
            if(bin.get(i)==1){
                oneCt-=1;
                answer+= (int)(Math.pow(2, i));
            }
        }
        int two= 1;
        while(oneCt > 0){
            answer+= two;
            oneCt--;
            two*=2;
        }
        return answer;
    }
}    