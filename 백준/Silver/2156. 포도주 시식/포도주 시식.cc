#include <stdio.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
int main(){
    int n,m;
    scanf("%d",&n);
    int gph[n+1];
    int dp[n+1];
    int max=0;
    for(int i=1;i<=n;i++){
        scanf("%d",&gph[i]);
    }
    dp[0]=0;
    dp[1]=gph[1];
    dp[2]=gph[1]+gph[2];
    
    for(int i=3;i<=n;i++){
        dp[i]=max(max(dp[i-1],dp[i-3]+gph[i-1]+gph[i]),dp[i-2]+gph[i]);
    }
    for(int i=1;i<=n;i++){
        if(max<dp[i]){
            max=dp[i];
        }
    }
    printf("%d",max);
    return 0;
}