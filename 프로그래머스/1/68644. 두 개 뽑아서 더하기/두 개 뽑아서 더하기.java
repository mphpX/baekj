class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int idx = 0;
        int count = 0;
        boolean[] check= new boolean[201];
        for(int i = 0; i < n; i++){
            for(int j = i+1; j<n; j++){
                idx= numbers[i]+ numbers[j];
                if(!check[idx]){
                    check[idx]= true;
                    count+=1;
                }
            }
        }
        idx = 0;
        int[] answer= new int[count];
        for(int i = 0 ; i < 201; i++){
            if(check[i])answer[idx++]= i;
        }
        return answer;
    }
}