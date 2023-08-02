#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int dp[1000001]={0};
    int n;
    scanf("%d",&n);
    dp[1]=0;
    dp[2]=1;
    dp[3]=1;
    for(int i=4;i<=n;i++){
        if(i%3==0&&i%2==0){
            dp[i]=min(min(dp[i/3]+1,dp[i/2]+1),dp[i-1]+1);
        }
        else if(i%3==0&&i%2!=0){
            dp[i]=min(dp[i/3]+1,dp[i-1]+1);
        }
        else if(i%2==0){
            dp[i]=min(dp[i/2]+1,dp[i-1]+1);
        }
        else{
            dp[i]=dp[i-1]+1;
        }
    }
    printf("%d\n",dp[n]);
    printf("%d ",n);
    while(n!=1){
        if(n%3==0&&n%2==0){
            if(dp[n]==dp[n/3]+1)n/=3;
            else if(dp[n]==dp[n/2]+1)n/=2;
            else n-=1;
        }
        else if(n%3==0&&n%2!=0){
            if(dp[n/3]<dp[n-1])n/=3;
            else n-=1;
        }
        else if(n%2==0){
            if(dp[n/2]+1<dp[n-1]+1){
                n/=2;
            }
            else{
                n-=1;
            }
        }
        else{
            n-=1;
        }
        printf("%d ",n);
    }
    return 0;
}