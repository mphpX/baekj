class Solution {
    public String solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        int x;
        for(int i = 1; i < numLog.length; i++){
            x= numLog[i]-numLog[i-1];
            if(x== 1){
                sb.append("w");
            }else if(x==-1){
                sb.append("s");
            }else if(x==10){
                sb.append("d");
            }else{
                sb.append("a");
            }
        }
        return sb.toString();
    }
}