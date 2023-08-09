#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    int arr[300001];
    int dp[300001]={0};
    for(int i=1;i<=300000;i++){
        arr[i]=i;
    }
    for(int i=2;i<=300000;i++){
        arr[i]+=arr[i-1];
        if(arr[i]>=300001){
            break;
        }
    }
    int ct=2;
    for(int i=2;i<=300000;i++){
        arr[i]+=arr[i-1];
        if(arr[i]>300000){
            break;
        }
        ct++;
    }
    for(int i=1;i<ct;i++){
        dp[arr[i]]=1;
    }
    for(int i=2;i<=n;i++){
        if(dp[i]==0){
            dp[i]=dp[i-1]+1;
            for(int j=1;arr[j]<i;j++){
                dp[i]=min(dp[i],dp[arr[j]]+dp[i-arr[j]]);
            }
        }
    }
    printf("%d",dp[n]);

    return 0;
}