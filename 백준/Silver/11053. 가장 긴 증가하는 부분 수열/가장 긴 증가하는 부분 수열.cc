#include <stdio.h>
int main(){
    int n,m;
    scanf("%d",&n);
    int gph[n+1];
    int dp[n+1];
    for(int i=1;i<=n;i++){
        dp[i]=1;
    }
    for(int i=1;i<=n;i++){
        scanf("%d",&gph[i]);
    }
    for(int i=2;i<=n;i++){
        for(int j=1;j<i;j++){
            if(gph[i]>gph[j]&&dp[i]<dp[j]+1){
                dp[i]=dp[j]+1;
            }
        }
    }
    int max=0;
    for(int i=1;i<=n;i++){
        if(dp[i]>max){
            max=dp[i];
        }
    }
    printf("%d",max);
    return 0;
}