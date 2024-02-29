import sys
sys.setrecursionlimit(10 ** 6)
def dfs(t):
    global ct
    visited[t]=ct
    for i in l[t]:
        if(visited[i]==0):
            ct+=1
            dfs(i)
    
n,m,o=map(int,sys.stdin.readline().split())
l=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
ct=1
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
for i in range(n+1):
    l[i].sort()
dfs(o)
for i in range(1,n+1):
    print(visited[i])