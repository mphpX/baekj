#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n;
    scanf("%d",&n);
    int dp[11]={0};
    dp[1]=0;
    for(int i=2;i<=n;i++){
        dp[i]+=(i/2)*(i-i/2);
        if(i>1){
            dp[i]+=dp[i/2]+dp[i-i/2];
        }
    }
    printf("%d",dp[n]);
    return 0;
}