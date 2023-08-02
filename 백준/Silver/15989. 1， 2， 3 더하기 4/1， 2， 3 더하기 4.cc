#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    int dp[10001][4];
    dp[1][1]=1;dp[1][2]=0;dp[1][3]=0;
    dp[2][1]=1;dp[2][2]=1;dp[2][3]=0;
    dp[3][1]=2;dp[3][2]=0;dp[3][3]=1;
    scanf("%d",&n);
    for(int i=4;i<10001;i++){
        dp[i][1]=0;dp[i][2]=0;dp[i][3]=0;
        for(int j=1;j<=3;j++){
            dp[i][1]+=dp[i-1][j];
        }
        for(int j=2;j<=3;j++){
            dp[i][2]+=dp[i-2][j];
        }
        dp[i][3]+=dp[i-3][3];
    }
    for(int i=0;i<n;i++){
        scanf("%d",&m);
        printf("%d\n",dp[m][1]+dp[m][2]+dp[m][3]);
    }
    return 0;
}