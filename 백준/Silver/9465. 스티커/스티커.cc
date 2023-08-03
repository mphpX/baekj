#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int arr[2][100001];
    int dp[2][100001];
    int mx=0;
    for(int i=0;i<n;i++){
        scanf("%d",&m);
        mx=0;
        for(int j=0;j<2;j++){
            for(int k=1;k<=m;k++){
                scanf("%d",&arr[j][k]);
            }
        }
        dp[0][1]=arr[0][1];dp[1][1]=arr[1][1];
        dp[0][2]=dp[1][1]+arr[0][2];dp[1][2]=dp[0][1]+arr[1][2];
        for(int i=1;i<=2;i++){
            if(mx<max(dp[0][i],dp[1][i])){
                mx=max(dp[0][i],dp[1][i]);
            }
        }
        for(int i=3;i<=m;i++){
            dp[0][i]=max(dp[1][i-1]+arr[0][i],dp[1][i-2]+arr[0][i]);
            dp[1][i]=max(dp[0][i-1]+arr[1][i],dp[0][i-2]+arr[1][i]);
            if(mx<max(dp[0][i],dp[1][i])){
                mx=max(dp[0][i],dp[1][i]);
            }
        }
        printf("%d\n",mx);
    }
    return 0;
}