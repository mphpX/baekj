import sys
input = sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
left=0
right=max(l)
tr=0
while(left<=right):
    mid=(left+right)//2
    tr=0
    for i in l:
        if(i-mid>0):
            tr+=i-mid
    if(tr<m):
        right=mid-1
    else:
        left=mid+1
print(right)    