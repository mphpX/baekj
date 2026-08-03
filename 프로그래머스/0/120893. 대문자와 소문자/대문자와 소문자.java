class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        char[] my_ch = my_string.toCharArray();
        for(char ch: my_ch){
            if(Character.isUpperCase(ch)){
                answer.append(Character.toLowerCase(ch));
            }else{
                answer.append(Character.toUpperCase(ch));
            }
        }
        return answer.toString();
    }
}