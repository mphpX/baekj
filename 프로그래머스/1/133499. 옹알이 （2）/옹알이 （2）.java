import java.util.*;
class Solution {
    boolean[] visited= new boolean[4];
    List<String> can= new ArrayList<>();
    String[] fst = {"aya", "ye", "woo", "ma"};
    public void back_track(int previous, String cur, int maxLength){
        if(!cur.isEmpty()){
            can.add(cur);
        }
        if(cur.length() > maxLength){
            return;
        }
        
        for(int i = 0; i < 4; i++){
            if(i!= previous){
                back_track(i, cur+ fst[i], maxLength);
            }
        }
    }
    public int solution(String[] babbling) {
        int answer = 0;
        int maxLength= 0;
        for(String bab: babbling){
            maxLength= Math.max(bab.length(), maxLength);
        }
        back_track(5, "", maxLength);
        for(String bab: babbling){
            for(String c: can){
                if(bab.equals(c)){
                    answer+=1;
                    break;
                }
            }
        }
        return answer;
    }
}