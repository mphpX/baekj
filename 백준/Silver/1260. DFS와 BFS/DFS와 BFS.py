import sys
from collections import deque
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,n+1):
    graph[i].sort()
def bfs(n,start):
    bfs_visit=[False for _ in range(n+1)]
    q=deque([start])
    bfs_visit[start]=True
    ans=[]
    while(q):
        cur=q.popleft()
        ans.append(cur)
        for i in graph[cur]:
            if(bfs_visit[i]==False):
                q.append(i)
                bfs_visit[i]=True
    return ans
dfs_visit=[False for _ in range(n+1)]
def dfs(start):
    if(dfs_visit[start]==1):
        return
    print(start,end=' ')
    dfs_visit[start]=True
    for i in graph[start]:
        if(dfs_visit[i]==False):
            dfs(i)
dfs(v)
print()
bfs_ans=bfs(n,v)
for i in bfs_ans:
    print(i,end=' ')
