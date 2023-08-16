#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long n, m,o;  
    scanf("%lld",&n);
    long long dp[1000000];
    dp[1]=1;
    dp[2]=2;
    long long a;
    for(int i=3;i<1000000;i++){
        if(i%2==1){
            dp[i]=dp[i-1]-dp[i-2]+1+dp[i-1];
        }
        else{
            dp[i]=dp[i-1]-dp[i-2]+dp[i-1];
        }
    }
    for(long long i=0;i<n;i++){
        scanf("%lld %lld",&m,&o);
        a=o-m;
        long long j=1;
        if(a==1)printf("1\n");
        else{
            while(a<=dp[j]||a>dp[j+1]){
                j++;
            }
            printf("%lld\n",j+1);
        }
    }
    return 0;
}
