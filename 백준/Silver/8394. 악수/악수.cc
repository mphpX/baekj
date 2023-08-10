#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d",&n);
    
    int p=1;
    int q=2;
    int r=0;
    for(int i=1;i<=n;i++){
        r+=p;
    }
    
    for(int i=3;i<=n;i++){
        r=(p+q)%10;
        p=q;
        q=r;
    }
    printf("%d\n",r);
    return 0;
}