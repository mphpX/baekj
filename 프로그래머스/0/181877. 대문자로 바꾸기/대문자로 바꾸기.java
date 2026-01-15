class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < myString.length(); i++){
            char cur = myString.charAt(i);
            if('a' <= cur && cur <= 'z') cur = (char)(cur - 32);
            sb.append(cur);
        }
        return sb.toString();
    }
}