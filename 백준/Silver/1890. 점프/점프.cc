#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    long long n;
    scanf("%lld",&n);
    long long arr[101][101];
    long long dp[111][111];
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            scanf("%lld",&arr[i][j]);
            dp[i][j]=0;
        }
    }
    dp[1][1]=1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(arr[i][j]!=0){
                if(dp[i][j]>0&&i+arr[i][j]<=n){
                    dp[i+arr[i][j]][j]+=dp[i][j];
                }
                if(dp[i][j]>0&&j+arr[i][j]<=n){
                    dp[i][j+arr[i][j]]+=dp[i][j];
                }
            }
        }
    }
    
    printf("%lld\n",dp[n][n]);
    return 0;
}