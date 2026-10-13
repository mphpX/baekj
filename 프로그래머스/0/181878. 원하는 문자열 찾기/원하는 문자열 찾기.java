class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        myString= myString.toLowerCase();
        pat= pat.toLowerCase();
        if(myString.length() < pat.length()){
            return 0;
        }
        for(int i = pat.length()-1; i < myString.length(); i++){
            if(myString.substring(i- pat.length()+1, i+1).equals(pat)){
                return 1;
            }
        }
        return answer;
    }
}