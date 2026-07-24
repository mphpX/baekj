import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int mn = arr[0];
        for(int i = 1; i < arr.length; i++){
            if(mn > arr[i]){
                mn= arr[i];
            }
        }
        int[] answer= new int[arr.length -1];
        int idx = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] != mn){
                answer[idx++]= arr[i];
            }
        }
        if(answer.length == 0) answer = new int[] {-1};
        return answer;
    }
}