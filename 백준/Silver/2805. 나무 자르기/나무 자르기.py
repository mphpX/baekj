import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
s=1
e=max(l)
mid=0
while(s<=e):
    mid=(s+e)//2
    ct=0
    for i in range(n):
        if(l[i]>mid):
            ct+=l[i]-mid
    if(ct>=m):
        s=mid+1
    else:
        e=mid-1
print(e)