import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=int(input())
c=list(map(int,input().split()))
ra=[]
for i in range(n):
    if(a[i]==0):
        ra.append(b[i])
ct=0
while(ct<m and len(ra)-1-ct>=0):
    print(ra[len(ra)-1-ct],end=' ')
    ct+=1
x=m-ct
for i in range(x):
    print(c[i],end=' ')