class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int n= s.length();
        int cur = 0;
        for(int i = 0; i < n; i++){
            if(s.charAt(i)== ' '){
                cur = 0;
                answer.append(' ');
            }else{
                if(cur%2 ==0)answer.append(Character.toUpperCase(s.charAt(i)));
                else answer.append(Character.toLowerCase(s.charAt(i)));
                cur+=1;
            }
        }
        
        return answer.toString();
    }
}