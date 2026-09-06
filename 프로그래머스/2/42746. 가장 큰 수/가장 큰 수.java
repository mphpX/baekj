import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        List<String> ls = new ArrayList<>();
        for(int i : numbers){
            ls.add(Integer.toString(i));
        }
        
        ls.sort((a, b) -> {
            String case1 = a+b;
            String case2 = b+a;
            return case2.compareTo(case1);
        });
        StringBuilder sb= new StringBuilder();
        if(ls.get(0).equals("0")){
            return "0";
        }
        for(String st: ls){
            sb.append(st);
        }
        return sb.toString();
    }
}