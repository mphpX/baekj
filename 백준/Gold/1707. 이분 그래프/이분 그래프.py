import sys
from collections import deque
input=sys.stdin.readline
k=int(input())
def bfs(a):
    q=deque([a])
    visited[a]=1
    prev=0
    while(q):
        cur=q.popleft()
        for i in graph[cur]:
            if(visited[i]==0):
                visited[i]=visited[cur]+1
                q.append(i)
            else:
                if((visited[cur]+1)%2!=visited[i]%2):
                    return -1
        prev=cur
    return 0    
for t in range(k):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited=[0 for _ in range(v+1)]
    result=0
    for i in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if(visited[i]==0):
            result=bfs(i)
        if(result==-1):
            break
    if(result==0):
        print("YES")
    else:
        print("NO")