#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int p,q,r,s;
    int dp[1001][1001];
    int arr[1001][1001];
    int x;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            scanf("%d",&x);
            arr[i][j]=x;
        }
    }
    dp[1][1]=arr[1][1];
    for(int i=2;i<=n;i++){
        dp[i][1]=arr[i][1]+dp[i-1][1];
    }
    for(int i=2;i<=m;i++){
        dp[1][i]=arr[1][i]+dp[1][i-1];
    }
    for(int i=2;i<=n;i++){
        for(int j=2;j<=m;j++){
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])+arr[i][j];
        }
    }
    printf("%d\n",dp[n][m]);
    return 0;
}