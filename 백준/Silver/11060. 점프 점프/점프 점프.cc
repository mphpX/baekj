#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) < (b)) ? (a) : (b))

int main()
{
    int n, s, m;
    scanf("%d", &n);
    int arr[1001] = {0};
    int dp[1001]={0};
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &arr[i]);
    }
    dp[1]=1;
    for(int i=1;i<n;i++){
        if(dp[i]>0){
            for(int j=1;j<=arr[i]&&i+j<=n;j++){
                if(dp[i+j]>0){
                    dp[i+j]=min(dp[i+j],dp[i]+1);
                }
                else{
                    dp[i+j]=dp[i]+1;
                }
            }
        }
    }
    if(dp[n]!=0){
        printf("%d\n",dp[n]-1);
    }
    else{
        printf("-1\n");
    }
    return 0;
}