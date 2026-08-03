class Solution {
    public String solution(String my_string, String alp) {
        StringBuilder sb = new StringBuilder();
        char[] chs= my_string.toCharArray();
        char alpha = alp.charAt(0);
        for(int i = 0; i < chs.length; i++){
            if(chs[i]== alpha){
                sb.append(Character.toUpperCase(chs[i]));
            }else{
                sb.append(chs[i]);
            }
        }
        return sb.toString();
    }
}