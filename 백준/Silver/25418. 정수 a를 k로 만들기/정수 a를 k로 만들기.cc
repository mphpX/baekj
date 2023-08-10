#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int dp[1000000]={0};
    dp[n+1]=1;
    for(int i=n+2;i<=m;i++){
        dp[i]=dp[i-1]+1;
        if(i%2==0&&i/2>=n){
            dp[i]=min(dp[i-1]+1,dp[i/2]+1);
        }
        
    }
    printf("%d",dp[m]-dp[n]);
    return 0;
}