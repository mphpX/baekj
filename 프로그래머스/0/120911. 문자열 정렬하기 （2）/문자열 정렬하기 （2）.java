import java.util.*;
class Solution {
    public String solution(String my_string) {
        my_string= my_string.toLowerCase();
        char[] stringToChar = my_string.toCharArray();
        Arrays.sort(stringToChar);
        return new String(stringToChar);
    }
}