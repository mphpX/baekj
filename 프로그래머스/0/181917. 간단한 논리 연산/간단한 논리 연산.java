class Solution {
    public boolean v(boolean x, boolean y){
        if(x||y){
            return true;
        }else{
            return false;
        }
    }
    public boolean w(boolean x, boolean y){
        if(x&& y){
            return true;
        }else{
            return false;
        }
    }
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        return w(v(x1, x2), v(x3, x4));
    }
}