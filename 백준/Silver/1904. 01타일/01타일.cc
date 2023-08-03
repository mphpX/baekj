#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    int a;
    scanf("%d",&a);
    long long p=1;
    long long q=1;
    long long r=0;
    for(int i=1;i<a;i++){
        r=(p+q)%15746;
        p=q;
        q=r;
    }
    printf("%lld",q);
    return 0;
}