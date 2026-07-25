class Solution {
    public boolean solution(String s) {
        if(s.length() != 4 && s.length() != 6) return false;
        char[] chs= s.toCharArray();
        for(char ch : chs){
            if(!Character.isDigit(ch)) return false;
        }
        return true;
    }
}