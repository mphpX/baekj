from collections import deque
n=int(input())
graph=[list(input().strip()) for _ in range(n)]
def bfs(a):
    visited=[0 for _ in range(n)]
    q=deque([a])
    visited[a]=1
    ct=0
    while(q):
        cur=q.popleft()
        if(visited[cur]>3):
            break
        ct+=1
        for next in range(n):
            if(graph[cur][next]=='Y' and visited[next]==0):
                q.append(next)
                visited[next]=visited[cur]+1
    return ct-1
mx=0
for i in range(n):
    mx=max(mx,bfs(i))
print(mx)