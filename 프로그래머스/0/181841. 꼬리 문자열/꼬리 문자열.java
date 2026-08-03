class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuilder sb = new StringBuilder();
        int n = str_list.length;
        int m = ex.length();
        for(int i = 0; i < n; i++){
            boolean isit = true;
            for(int j = 0; j < str_list[i].length()-m+1; j++){
                if(str_list[i].substring(j, j+ m).equals(ex)){
                    isit = false;
                    break;
                }
            }
            if(isit) sb.append(str_list[i]);
            
            
        }
        
        return sb.toString();
    }
}