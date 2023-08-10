#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    m=max(n,-n);
    int arr[101];
    int dp[1000001]={0};
    dp[0]=0;
    dp[1]=1;
    for(int i=2;i<=m;i++){
        dp[i]=(dp[i-1]+dp[i-2])%1000000000;
    }
    if(m%2==0&&n<0){
        printf("-1\n");
    }
    else if(m==0){
        printf("0\n");
    }
    else{
        printf("1\n");
    }
    printf("%d\n",dp[m]);
    return 0;
}