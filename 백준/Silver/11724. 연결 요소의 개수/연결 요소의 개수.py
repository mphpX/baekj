import sys
sys.setrecursionlimit(10**9)
ct=0
n,m=map(int,sys.stdin.readline().split())
visited=[0 for _ in range(n+1) ]
l=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
def dfs(r):
    visited[r]=1
    for i in l[r]:
        if(visited[i]==0):
            dfs(i)
for i in range(1,n+1):
    if(visited[i]==0):
        dfs(i)
        ct+=1
print(ct)