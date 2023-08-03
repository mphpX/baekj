#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
int main() {
    int n,m;
    scanf("%d %d",&n,&m);
    long long s[201][201];
    for(int i=1;i<n+1;i++){
        for(int j=1;j<m+1;j++){
            s[i][j]=0;
        }
    }
    for(int j=1;j<m+1;j++){
        s[1][j]=j;
        s[0][j]=1;
    }
    for(int i=1;i<n+1;i++){
        s[i][1]=1;
        s[i][2]=i+1;
    }
    for(int i=2;i<n+1;i++){
        for(int j=3;j<m+1;j++){
            for(int k=1;k<=j;k++){
                s[i][j]+=s[i-1][k]%1000000000;
            }
        }
    }
    
    printf("%lld",s[n][m]%1000000000);
	return 0;
}