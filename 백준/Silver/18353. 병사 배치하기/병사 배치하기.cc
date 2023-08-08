#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int arr[2001];
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    int dp[2001];
    int max=1;
    dp[1]=1;
    for(int i=2;i<=n;i++){
        m=1;
        for(int j=1;j<i;j++){
            if(arr[j]>arr[i]&&m<dp[j]+1){
                m=dp[j]+1;
            }
        }
        dp[i]=m;
        if(max<dp[i]){
            max=dp[i];
        }
    }
    printf("%d",n-max);

    return 0;
}