#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(){
    int n;
    int arr[100001][4];
    int adp[4]={0};
    int bdp[4]={0};
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=3;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    adp[1]=arr[1][1];adp[2]=arr[1][2];adp[3]=arr[1][3];
    bdp[1]=arr[1][1];bdp[2]=arr[1][2];bdp[3]=arr[1][3];
    for(int i=2;i<=n;i++){
        for(int j=1;j<=3;j++){
            if(j==1) bdp[j]=max(adp[j],adp[j+1])+arr[i][j];
            else if(j==2)bdp[j]=max(adp[j-1],max(adp[j],adp[j+1]))+arr[i][j];
            else bdp[j]=max(adp[j-1],adp[j])+arr[i][j];
        }
        adp[1]=bdp[1];
        adp[2]=bdp[2];
        adp[3]=bdp[3];
    }
    printf("%d ",max(bdp[3],max(bdp[1],bdp[2])));
    adp[1]=arr[1][1];adp[2]=arr[1][2];adp[3]=arr[1][3];
    for(int i=2;i<=n;i++){
        for(int j=1;j<=3;j++){
            if(j==1) bdp[j]=min(adp[j],adp[j+1])+arr[i][j];
            else if(j==2)bdp[j]=min(adp[j-1],min(adp[j],adp[j+1]))+arr[i][j];
            else bdp[j]=min(adp[j-1],adp[j])+arr[i][j];
        }
        adp[1]=bdp[1];
        adp[2]=bdp[2];
        adp[3]=bdp[3];
    }
    printf("%d ",min(bdp[3],min(bdp[1],bdp[2])));
    return 0;
}