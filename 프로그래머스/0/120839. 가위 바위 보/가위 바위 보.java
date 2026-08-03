class Solution {
    public String solution(String rsp) {
        // 2 -> 0
        // 0 -> 5
        // 5 -> 2
        String str= "205";
        StringBuilder sb= new StringBuilder();
        for(int i = 0; i < rsp.length(); i++){
            int idx= 0;
            for(int j = 0; j < 3; j++){
                if(rsp.charAt(i)== str.charAt(j)) idx= j;
            }
            sb.append(str.charAt((idx+1)%3));
        }
        return sb.toString();
    }
}