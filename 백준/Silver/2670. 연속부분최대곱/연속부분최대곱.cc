#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n;
    double m;
    scanf("%d",&n);
    double a[10001];
    double dp[10001];
    for(int i=1;i<=n;i++){
        scanf("%lf",&a[i]);
        dp[i]=a[i];
    }
    m=0;
    for(int i=2;i<=n;i++){
        if(dp[i]<dp[i-1]*dp[i]){
            dp[i]=dp[i-1]*dp[i];
        }
        if(dp[i]>m)m=dp[i];
    }
    printf("%.3f",m);
    return 0;
}