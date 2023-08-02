#include <stdio.h>
int main(){
    int p[1001]={0};
    int n,m;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&p[i]);
    }
    int dp[1001]={0};
    dp[0]=0;
    dp[1]=p[1];
    for(int i=2;i<=n;i++){
        dp[i]=p[i];
        for(int j=0;j<i;j++){
            if(dp[i]>dp[j]+p[i-j]){
                dp[i]=dp[j]+p[i-j];
            }
        }
    }
    printf("%d\n",dp[n]);
    return 0;
}