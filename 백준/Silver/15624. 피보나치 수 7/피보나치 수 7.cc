#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long dp[1000001]={0};
    int n;
    scanf("%d",&n);
    dp[0]=0;
    dp[1]=1;
    for(int i=2;i<=n;i++){
        dp[i]=(dp[i-1]+dp[i-2])%1000000007;
    }
    printf("%lld",dp[n]);
    return 0;
}