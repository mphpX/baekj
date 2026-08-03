class Solution {
    public int solution(String str1, String str2) {
        int m = str1.length();
        int n = str2.length();
        for(int i = 0; i < n-m+1; i++){
            if(str2.substring(i,i+m).equals(str1)) return 1;
        }
        return 0;
    }
}