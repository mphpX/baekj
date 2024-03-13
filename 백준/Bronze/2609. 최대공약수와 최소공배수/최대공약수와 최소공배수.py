import sys
n,m=map(int,input().split())
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
x=gcd(n,m)
print(x,n*m//x,sep='\n')
