#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int dp[50001]={0};
    for(int i=1;i*i<=n;i++){
        dp[i*i]=1;
    }
    for(int i=2;i<=n;i++){
        if(dp[i]==0){
            dp[i]=dp[1]+dp[i-1];
            for(int j=2;j*j<i;j++){
                dp[i]=min(dp[j*j]+dp[i-j*j],dp[i]);
            }
        }
    }    
    printf("%d",dp[n]);
    return 0;
}