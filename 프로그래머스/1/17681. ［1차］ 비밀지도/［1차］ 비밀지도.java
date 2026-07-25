import java.util.*;
class Solution {
    public String two(int n, int row, int[] arr1, int[] arr2){
        int[][] arrs = {arr1, arr2};
        boolean[][] arr= new boolean[2][n];
        int p = 0;
        for(int i = 0; i < 2; i++){
            for(int j = n-1; j >=0; j--){
                p = (int)Math.pow(2,j);
                arr[i][n-1-j]= arrs[i][row] >= p;
                if(arr[i][n-1-j]) arrs[i][row]-= (int)(arrs[i][row]/p)*p;
            }
        }
        StringBuilder ans = new StringBuilder();
        for(int i = 0; i < n; i++){
            if(arr[0][i] || arr[1][i]){
                ans.append("#");
            }else{
                ans.append(" ");
            }
        }
        return ans.toString();
    }
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for(int i = 0; i < n; i++){
            answer[i]= two(n, i, arr1, arr2);
        }
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));
        return answer;
    }
}