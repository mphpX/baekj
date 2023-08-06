#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n;
    int dp[51]={0};
    scanf("%d",&n);
    dp[0]=1;
    dp[1]=1;

    for(int i=2;i<=n;i++){
        dp[i]=(dp[i-1]+dp[i-2]+1)%1000000007 ;
    }
    printf("%d",dp[n]);
    return 0;
}