#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,s,m;
    scanf("%d %d",&n,&m);
    long long dp[1001][1001];
    dp[1][1]=1;
    for(int i=2;i<1001;i++){
        dp[1][i]=1;
        dp[i][1]=1;
    }
    for(int i=2;i<=n;i++){
        for(int j=2;j<=m;j++){
            dp[i][j]=(dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1])%1000000007;
        }
    }
    printf("%lld\n",dp[n][m]);
    return 0;
}