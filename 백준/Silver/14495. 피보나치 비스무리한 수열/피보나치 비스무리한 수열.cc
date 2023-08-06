#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long dp[117]={0};
    int n;
    scanf("%d",&n);
    dp[1]=dp[2]=dp[3]=1;
    for(int i=4;i<=n;i++){
        dp[i]=dp[i-1]+dp[i-3];
    }
    printf("%lld",dp[n]);
    return 0;
}