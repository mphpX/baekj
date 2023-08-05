#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long dp[36]={0};
    dp[0]=1;
    dp[1]=1;
    int n;
    scanf("%d",&n);
    for(int i=2;i<=n;i++){
        for (int j = 0; j < i; j++){
            dp[i]+=dp[j]*dp[i-j-1];
        }
    }
    printf("%lld",dp[n]);
    return 0;
}