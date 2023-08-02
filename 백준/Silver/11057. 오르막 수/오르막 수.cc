#include <stdio.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
int main(){
    int n;
    scanf("%d",&n);
    int dp[n+1][10];
    for(int i=0;i<=n;i++){
        for(int j=0;j<10;j++){
            dp[i][j]=0;
        }
    }
    for(int i=0;i<10;i++){
        dp[1][i]=1;
    }
    for(int i=2;i<=n;i++){
        for(int j=0;j<10;j++){
            for(int k=0;k<=j;k++){
                dp[i][j]=(dp[i][j]+dp[i-1][k])%10007;
            }
        }
    }
    int sum=0;
    for(int i=0;i<10;i++){
        sum=(sum+dp[n][i])%10007;
    }
    printf("%d",sum);
    return 0;
}