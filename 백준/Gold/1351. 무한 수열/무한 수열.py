from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
n,p,q=map(int,input().split())
d=dict()
d[0]=1
def dfs(n,a,b):
    if(n in d):
        return d[n]
    else:
        if(n//a not in d):
            d[n//a]=dfs(n//a,a,b)
        if(n//b not in d):
            d[n//b]=dfs(n//b,a,b)
        return d[n//a]+d[n//b]
print(dfs(n,p,q))