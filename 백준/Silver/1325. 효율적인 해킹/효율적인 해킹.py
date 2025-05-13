import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
ans=[0 for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
def bfs(x):
    q=deque([x])
    visited=[False for _ in range(n+1)]
    visited[x]=True
    ct=0
    while(q):
        cur=q.popleft()
        for next in graph[cur]:
            if(visited[next]==0):
                q.append(next)
                visited[next]=True
                ct+=1
    return ct

for i in range(1,n+1):
    ans[i]=bfs(i)
mx=max(ans)
for i in range(1,n+1):
    if(ans[i]==mx):
        print(i,end=' ')