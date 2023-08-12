#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int p,q,r,s;
    int dp[1025][1025];
    int x;
    for(int i=1;i<=n;i++){
        scanf("%d",&x);
        dp[i][0]=0;
        dp[i][1]=x;
        for(int j=2;j<=n;j++){
            scanf("%d",&x);
            dp[i][j]=dp[i][j-1]+x;
        }
    }
    int sum;
    for(int i=1;i<=m;i++){
        sum=0;
        scanf("%d %d %d %d",&p,&q,&r,&s);
        for(int j=p;j<=r;j++){
            sum+=dp[j][s]-dp[j][q-1];
        }
        printf("%d\n",sum);
    }
    return 0;
}