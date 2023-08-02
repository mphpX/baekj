#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int dp[100001]={0};
    int dp2[100001]={0};
    int n;
    scanf("%d",&n);
    int arr[100001];
    for(int i=1;i<=n;i++){
        scanf("%d",&arr[i]);
    }
    dp[1]=1;
    dp2[1]=1;
    int max=1;
    for(int i=2;i<=n;i++){
        if(arr[i-1]<=arr[i]){
            dp[i]=dp[i-1]+1;
        }
        else{
            dp[i]=1;
        }
        if(arr[i-1]>=arr[i]){
            dp2[i]=dp2[i-1]+1;
        }
        else{
            dp2[i]=1;
        }
        if(max<dp[i]){
            max=dp[i];
        }
        if(max<dp2[i]){
            max=dp2[i];
        }
    }
    printf("%d",max);
    return 0;
}