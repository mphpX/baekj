import sys
n,m=map(int,input().split())
l=list(map(int,input().split()))
a=[0]*(n+1)
p=-10000001
if(m==1):
    print(max(l))
else:
    for i in range(1,n+1):
        a[i]=a[i-1]+l[i-1]
    for i in range(n-m+1):
        if(p<a[i+m]-a[i]):
            p=a[i+m]-a[i]
    print(p)