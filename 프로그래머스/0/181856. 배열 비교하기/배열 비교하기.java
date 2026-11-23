class Solution {
    public int solution(int[] arr1, int[] arr2) {
        if(arr1.length == arr2.length){
            int arr1_Sum = 0;
            int arr2_Sum = 0;
            for(int x : arr1){
                arr1_Sum+= x;
            }
            for(int x : arr2){
                arr2_Sum+= x;
            }
            if(arr1_Sum== arr2_Sum) return 0;
            return (arr1_Sum- arr2_Sum)/Math.abs(arr1_Sum- arr2_Sum);
        }
        return (arr1.length- arr2.length)/ Math.abs(arr1.length- arr2.length);
    }
}