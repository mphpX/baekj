class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        char[] my_ch = my_string.toCharArray();
        for(char ch: my_ch){
            if(!(ch=='a'|| ch == 'e'|| ch== 'i'|| ch=='o'|| ch=='u')){
                answer.append(ch);
            }
            
        }
        return answer.toString();
    }
}