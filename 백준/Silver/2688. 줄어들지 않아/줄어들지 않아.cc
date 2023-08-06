#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    long long dp[65][10];
    for(int i=0;i<10;i++){
        dp[1][i]=1;
    }
    for(int i=2;i<65;i++){
        for(int j=0;j<10;j++){
            dp[i][j]=0;
            for(int k=0;k<=j;k++){
                dp[i][j]+=dp[i-1][k];
            }
        }
    }
    int n,m;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&m);
        long long sum=0;
        for(int j=0;j<10;j++){
            sum+=dp[m][j];
        }
        printf("%lld\n",sum);
    }
    
    return 0;
}