import sys
from collections import deque
sys.setrecursionlimit(10**9)
n,m,o=map(int,sys.stdin.readline().split())
l=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
x=[0 for i in range(n+1)]
ct=1
def bfs(graph,start):
    global ct
    x[start]=ct
    ct+=1
    visited[start]=1
    stack=deque()
    stack.append(start)
    while(stack):
        node=stack.popleft()
        for i in graph[node]:
            if(visited[i]==0):
                visited[i]=1
                x[i]=ct
                ct+=1
                stack.append(i)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
for i in l:
    i.sort()
bfs(l,o)
for i in range(1,len(x)):
    print(x[i])