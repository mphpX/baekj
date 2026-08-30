class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder answer = new StringBuilder(my_string);
        for(int[] xy: queries){
            int x= xy[0];
            int y= xy[1];
            StringBuilder temp = new StringBuilder(answer.substring(x, y+1));
            answer.replace(x, y+1, temp.reverse().toString());
        }
        return answer.toString();
    }
}