from collections import deque
def bfs(n, a, graph, no_x, no_y):
    q= deque([a])
    visited=[False for _ in range(n+1)]
    visited[a]= True
    count=1
    while(q):
        cur= q.popleft()
        for next in graph[cur]:
            if(cur== no_x or cur ==no_y):
                if(next == no_x or next ==no_y):
                    continue
            if(visited[next]== False):
                visited[next]=True
                count+=1
                q.append(next)
    return count
            
def solution(n, wires):
    graph=[[] for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    answer= 101
    for x,y in wires:
        req= abs(2*bfs(n, x, graph, x,y) - n)
        answer= min(req, answer)
    return answer