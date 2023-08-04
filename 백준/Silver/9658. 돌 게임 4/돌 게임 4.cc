#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int dp[1001];
    dp[1]=0;
    dp[2]=1;
    dp[3]=0;
    dp[4]=1;
    int n;
    scanf("%d",&n);
    for(int i=5;i<=n;i++){
        if(dp[i-1]==0||dp[i-3]==0||dp[i-4]==0){
            dp[i]=1;
        }
        else{
            dp[i]=0;
        }
    }
    if(dp[n]==1)printf("SK");
    else printf("CY");
    
    return 0;
}