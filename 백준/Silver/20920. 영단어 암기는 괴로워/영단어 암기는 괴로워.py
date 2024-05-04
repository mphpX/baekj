import sys
n,m=map(int,sys.stdin.readline().split())
d=dict()
for i in range(n):
    l=sys.stdin.readline().strip()
    if(len(l)>=m):
        if(l not in d):
            d[l]=1
        else:
            d[l]+=1
d=sorted(d.items(),key=lambda x : (-x[1],-len(x[0]),x[0]))
for i in d:
    print(i[0])