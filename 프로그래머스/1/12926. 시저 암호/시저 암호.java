class Solution {
    public String solution(String s, int n) {
        char[] chs = s.toCharArray();
        StringBuilder sb= new StringBuilder();
        for(char ch: chs){
            if(ch!= ' '){
                char st= 'a';
                if(Character.isUpperCase(ch)){
                    st= 'A';
                }
                ch= (char)((ch-st + n)%26 + st);
            }
            sb.append(ch);
        }
        return sb.toString();
    }
}