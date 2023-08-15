#include <stdio.h>
#include <math.h>
#include <string.h>
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#define min(a,b)  (((a) < (b)) ? (a) : (b))
long long doub(long long a,long long b,long long c){
    if(a==1)return 1;
    if(b==1)return a%c;
    if(b%2==0){
        long long p=doub(a,b/2,c)%c;
        return p*p%c;
    }
    else{
        long long p=doub(a,(b-1)/2,c)%c;
        return ((p*p)%c)*(a%c)%c;
    }
}
int main(){
    long long n,m,o;  
    scanf("%lld %lld %lld",&n,&m,&o);
    printf("%lld",doub(n,m,o)%o);
    return 0;
}
