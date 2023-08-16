#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    long long dp[31]={0};
    dp[0]=1;
    dp[1]=1;
    dp[2]=2;
    for(int i=3;i<=30;i++){          
        for(int j=0;j<i;j++){
            dp[i]+=dp[j]*dp[i-j-1];
        }
    }
    while(n!=0){
        printf("%lld\n",dp[n]);
        scanf("%d",&n);
    }
    return 0;
}