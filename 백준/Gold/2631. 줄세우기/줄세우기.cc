#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n;
    scanf("%d",&n);
    int dp[201]={0};
    int arr[201]={0};
    int m=0;
    int max=0;
    dp[1]=1;
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=2;i<=n;i++){
        m=1;
        for(int j=1;j<i;j++){
            if(arr[i]>arr[j]&&m<dp[j]+1){
                m=dp[j]+1;
            }
        }
        dp[i]=m;
        if(dp[i]>max){
            max=dp[i];
        }
    }
    printf("%d\n",n-max);
    return 0;
}