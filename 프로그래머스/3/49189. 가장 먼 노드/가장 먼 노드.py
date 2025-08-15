from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    visited[1]=1
    for i in edge:
        x,y= i[0],i[1]
        graph[x].append(y)
        graph[y].append(x)
    q= deque([1])
    while(q):
        cur = q.popleft()
        for i in range(len(graph[cur])):
            next= graph[cur][i]
            if(visited[next]==0):
                visited[next]= visited[cur]+1
                q.append(next)
    m= max(visited)
    answer = 0
    for i in range(1,n+1):
        if(visited[i]==m):
            answer+=1
    return answer