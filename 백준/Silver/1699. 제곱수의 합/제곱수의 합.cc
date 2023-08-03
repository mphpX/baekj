#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))
int main(){
    int n;
    scanf("%d",&n);
    int dp[100001]={0};
    dp[1]=1;dp[2]=2;dp[3]=3;
    for(int i=2;i*i<100001;i++){
        dp[i*i]=1;
        for(int j=2;j*i*i<100001;j++){
            dp[j*i*i]=j;
        }
    }
    dp[0]=0;
    for(int i=5;i<=n;i++){
        int x=(sqrt(i));
        if(dp[i]==0)dp[i]=dp[i-1]+1;
        for(int j=2;j<=x;j++){
            int test=dp[j*j]+dp[i-j*j];
            if(dp[i]>test){
                dp[i]=test;
            }
        }
    }
    printf("%d",dp[n]);
    return 0;
}