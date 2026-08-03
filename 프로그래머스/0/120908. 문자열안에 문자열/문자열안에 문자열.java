class Solution {
    public int solution(String str1, String str2) {
        char[] chs1= str1.toCharArray();
        char[] chs2= str2.toCharArray();
        int cur = 0;
        for(int i = 0; i < chs1.length; i++){
            if(chs1[i]== chs2[cur]){
                cur++;
                if(cur == chs2.length) return 1;
            }else{
                cur = 0;
            }
        }
        return 2;
    }
}