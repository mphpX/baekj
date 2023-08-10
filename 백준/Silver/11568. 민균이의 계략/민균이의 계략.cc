#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int dp[1001];
    int arr[1001];
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    dp[1]=1;
    int mx=1;
    for(int i=2;i<=n;i++){
        m=0;
        dp[i]=1;
        for(int j=1;j<i;j++){
            if(arr[j]<arr[i]&&dp[j]>m){
                m=dp[j];
            }
            dp[i]=m+1;
        }
        if(mx<dp[i]){
            mx=dp[i];
        }
    }
    printf("%d\n",mx);
    return 0;
}