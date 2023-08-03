#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int arr[1001]={0};
    int dp[1001];
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    dp[1]=arr[1];
    int max=arr[1];
    for(int i=2;i<=n;i++){
        m=arr[i];
        dp[i]=arr[i];
        for(int j=1;j<i;j++){
            if(arr[j]<arr[i]&&m<dp[j]+dp[i]){
                m=dp[j]+dp[i];
            }
        }
        dp[i]=m;
        if(max<dp[i]){
            max=dp[i];
        }
    }
    printf("%d",max);
    return 0;
}