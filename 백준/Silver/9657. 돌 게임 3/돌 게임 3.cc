#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int dp[1001]={0};
    dp[1]=1;dp[2]=0;dp[3]=1;dp[4]=1;
    int n;
    scanf("%d",&n);
    for(int i=5;i<=n;i++){
        if(dp[i-1]==1&&dp[i-3]==1&&dp[i-4]==1){
            dp[i]=0;
        }
        else{
            dp[i]=1;
        }
    }
    if(dp[n]==1){
        printf("SK");
    }
    else{
        printf("CY");
    }
    return 0;
}