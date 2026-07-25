class Solution {
    public String solution(int[] food) {
        String answer = "";
        StringBuilder sb= new StringBuilder();
        int cur = 0;
        int n = food.length;
        for(int i = 1; i < n; i++){
            sb.append(Integer.toString(i).repeat(food[i]/2));
            cur+= food[i]/2;
        }
        cur-=1;
        char[] temp = sb.toString().toCharArray();
        sb.append("0");
        for(;cur >=0; cur--){
            sb.append(temp[cur]);
        }
        return sb.toString();
    }
}