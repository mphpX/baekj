import sys
n,m=map(int,input().split())
l=list(map(int,input().split()))
a=[0]*(n+1)
for i in range(1,n+1):
    a[i]=a[i-1]+l[i-1]
for i in range(m):
    p,q=map(int,sys.stdin.readline().split())
    print(a[q]-a[p-1])