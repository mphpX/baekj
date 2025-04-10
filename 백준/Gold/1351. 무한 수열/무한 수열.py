from collections import deque
n,p,q=map(int,input().split())
d=dict()
d[0]=1
def solve(n,a,b):
    if(n in d):
        return d[n]
    else:
        if(n//a not in d):
            d[n//a]=solve(n//a,a,b)
        if(n//b not in d):
            d[n//b]=solve(n//b,a,b)
        return d[n//a]+d[n//b]
print(solve(n,p,q))