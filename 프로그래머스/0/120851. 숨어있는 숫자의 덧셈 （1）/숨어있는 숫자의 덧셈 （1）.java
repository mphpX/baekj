class Solution {
    public int solution(String my_string) {
        int answer = 0;
        char[] my_ch= my_string.toCharArray();
        for(char ch: my_ch){
            if(Character.isDigit(ch)){
                answer+= (int)ch - '0';
            }
        }
        return answer;
    }
}