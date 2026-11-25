import java.util.*;
class Solution {
    public String solution(String my_string, int num1, int num2) {
        StringBuilder sb= new StringBuilder(my_string);
        char ch = my_string.charAt(num2);
        sb.setCharAt(num2, my_string.charAt(num1));
        sb.setCharAt(num1, ch);
        return sb.toString();
    }
}