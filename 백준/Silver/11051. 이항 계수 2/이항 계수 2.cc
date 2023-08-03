#include <stdio.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
int main(){
    int n,k;
    scanf("%d %d",&n,&k);
    long long dp[1001][1001];
    dp[0][0]=1;
    dp[1][0]=1;
    dp[1][1]=1;
    for(int i=0;i<=n;i++){
        dp[i][0]=1;
        dp[i][i]=1;
    }
    for(int i=2;i<=n;i++){
        for(int j=1;j<i;j++){
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007;
        }
    }
    printf("%lld",dp[n][k]%10007);
    return 0;
}