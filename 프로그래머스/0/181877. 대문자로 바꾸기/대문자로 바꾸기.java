class Solution {
    public String solution(String myString) {
        int num = 0;
        String answer = "";
        for(int i = 0; i< myString.length() ; i++){
            char cur = myString.charAt(i);
            num = cur;
            if(96 < num && num < 123){
                num -= 32;
                cur = (char)num;
            }
            answer+=cur;
        }
        return answer;
    }
}