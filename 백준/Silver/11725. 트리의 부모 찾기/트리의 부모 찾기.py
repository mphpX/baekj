import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q=deque([1])
visit=[False for _ in range(n+1)]
ans=[0 for _ in range(n+1)]
visit[1]=True
while(q):
    cur=q.popleft()
    for i in graph[cur]:
        if(visit[i]==False):
            q.append(i)
            visit[i]=True
            ans[i]=cur
for i in range(2,n+1):
    print(ans[i])