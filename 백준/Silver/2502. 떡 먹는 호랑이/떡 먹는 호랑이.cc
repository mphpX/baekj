#include <stdio.h>
#include <math.h>
#define max(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int a[31][3];
    a[1][1]=1;a[1][2]=0;a[2][1]=0;a[2][2]=1;
    for(int i=3;i<=n;i++){
        a[i][1]=a[i-1][1]+a[i-2][1];
        a[i][2]=a[i-1][2]+a[i-2][2];
    }
    int p=a[n][1];
    int q=a[n][2];
    for(int i=1;i<m;i++){
        int x=(m-i*p);
        if(x%a[n][2]==0){
            printf("%d\n%d\n",i,x/q);
            break;
        }
    }
    return 0;
}