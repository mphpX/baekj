from collections import deque
Dict=dict()
def bfs(start, graph):
    visited=set([start])
    queue=deque([start])
    result={}
    while queue:
        cur_node= queue.popleft()
        for next in graph[cur_node]:
            if next not in visited:
                visited.add(next)
                result[next]=cur_node
                queue.append(next)
    return result
n=int(input())
graph={i:[] for i in range(1,n+1)}
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=bfs(1,graph)
for i in range(2,n+1):
    print(ans[i])