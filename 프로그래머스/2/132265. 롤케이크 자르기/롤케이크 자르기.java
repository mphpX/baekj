class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int[] first = new int[10001];
        int[] second= new int[10001];
        int n = topping.length;
        
        int p = 0;
        int q = 0;
        for(int i = 0; i < n; i++){
            if(second[topping[i]]== 0) q++;
            second[topping[i]]++;
        }
        for(int i = 0; i < n; i++){
            if(second[topping[i]]== 1){
                q-=1;
            }
            if(first[topping[i]]== 0){
                p+=1;
            }
            second[topping[i]]--;
            first[topping[i]]++;
            if(p==q){
                answer++;
            }
        }
        return answer;
    }
}