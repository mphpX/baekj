#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long n,m;
    scanf("%lld",&n);
    long long dp[11]={0};
    long long ct=9;
    m=9;
    for(int i=1;i<10;i++){
        dp[i]=ct;
        m*=10;
        ct+=m;
    }
    ct=0;
    for(int i=1;i<10;i++){
        if(n>dp[i]){
            ct+=(dp[i]-dp[i-1])*i;
        }
        else{
            ct+=(n-dp[i-1])*i;
            break;
        }
    }
    printf("%lld\n",ct);
    return 0;
}