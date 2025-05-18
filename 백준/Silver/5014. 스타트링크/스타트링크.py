from collections import deque
f,s,g,u,d=map(int,input().split())
visited=[-1 for _ in range(f+1)]
def bfs(s,g,u,d):
    q=deque([s])
    visited[s]=0
    dx=[+u,-d]
    while(q):
        cur=q.popleft()
        if(cur==g):
            return
        for i in range(2):
            next=cur+dx[i]
            if(1<=next<f+1 and visited[next]==-1):
                visited[next]=visited[cur]+1
                q.append(next)
bfs(s,g,u,d)
if(visited[g]==-1):
    print("use the stairs")
else: print(visited[g])