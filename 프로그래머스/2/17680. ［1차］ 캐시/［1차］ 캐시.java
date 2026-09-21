import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        Queue<String> dq= new ArrayDeque<>();
        int answer = 0;
        if(cacheSize== 0){
            return 5 * cities.length;
        }
        for(int i = 0; i< cities.length; i++){
            String city= cities[i].toLowerCase();
            Queue<String> temp = new ArrayDeque<>();
            boolean isin = false;
            while(dq.size() > 0){
                String cur = dq.poll();
                if(cur.equals(city)){
                    isin = true;
                    break;
                }
                temp.offer(cur);
            }
            temp.addAll(dq);
            dq= temp;
            if(isin){
                answer++;
            }else{
                if(dq.size()== cacheSize) dq.poll();
                answer+= 5;
            }
            dq.offer(city);
        }
        
        return answer;
    }
}