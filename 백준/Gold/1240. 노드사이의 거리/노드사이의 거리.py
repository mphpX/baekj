import sys
from collections import deque
input=sys.stdin.readline
n,t=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    fn,sn,distance=map(int,input().split())
    graph[fn].append((sn,distance))
    graph[sn].append((fn,distance))
visit=[0 for _ in range(n+1)]
def bfs(start,end):
    q=deque([start])
    while(q):
        cur=q.popleft()
        for i in graph[cur]:
            next_node,next_distance= i[0],i[1]
            if(visit[next_node]==0):
                visit[next_node]=visit[cur]+next_distance
                if(next_node==end):
                    break
                q.append(next_node)
                

for i in range(t):
    visit=[0 for _ in range(n+1)]
    start,end=map(int,input().split())
    bfs(start,end)
    print(visit[end])