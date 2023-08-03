#include <stdio.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
int main(){
    int n;
    scanf("%d",&n);
    int arr[n+1];
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    int dp[n+1];
    dp[1]=1;
    int max=1;
    for(int i=2;i<=n;i++){
        dp[i]=1;
        for(int j=1;j<i;j++){
            if(arr[j]>arr[i]){
                if(dp[i]<dp[j]+1){
                    dp[i]=dp[j]+1;
                }
            }
        }
        if(dp[i]>max){
            max=dp[i];
        }
    }
    printf("%d",max);
    return 0;
}