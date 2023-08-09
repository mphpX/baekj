#include <stdio.h>
#include <math.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int r,c,w;
    scanf("%d %d %d",&r,&c,&w);
    int gph[31][31];
    gph[1][1]=1;
    gph[1][1]=1;
    gph[1][2]=1;
    for(int i=1;i<31;i++){
        gph[i][1]=1;
        gph[i][i]=1;
    }
    for(int i=3;i<31;i++){
        for(int j=2;j<i;j++){
            gph[i][j]=gph[i-1][j-1]+gph[i-1][j];
        }
    }
    int sum=0;
    for(int i=0;i<w;i++){
        for(int j=0;j<=i;j++){
            sum+=gph[i+r][j+c];
        }
    }
    printf("%d",sum);
    return 0;
}