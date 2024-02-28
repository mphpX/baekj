import sys
n=int(input())
l=[]
pdp=[1 for i in range(n)]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    l.append([a,b])
l.sort(key=lambda x: x[0])
for i in range(n):
    for j in range(i):
        if(l[i][1]>l[j][1]):
            pdp[i]=max(pdp[j]+1,pdp[i])
print(n-max(pdp))