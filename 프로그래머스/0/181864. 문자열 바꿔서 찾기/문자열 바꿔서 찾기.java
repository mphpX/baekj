class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int n = myString.length();
        int m = pat.length();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < myString.length(); i++){
            char cur = myString.charAt(i);
            if(cur == 'A'){
                sb.append('B');
            }else{
                sb.append('A');
            }
        }
        String diff = sb.toString();
        for(int i = 0 ; i < n-m+1; i++){
            System.out.println(diff.substring(i, i + m));
            if(diff.substring(i, i + m).equals(pat)){
                answer = 1;
            }
        }
        return answer;
    }
}