from collections import deque
n,m,k=map(int,input().split())
graph=[[0 for _ in range(m)] for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
xy=[]
ans=0
for i in range(k):
    x,y=map(int,input().split())
    xy.append((x-1,y-1))
    graph[x-1][y-1]=1
def bfs(a,b):
    q=deque([(a,b)])
    visited[a][b]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    ct=1
    while(q):
        cur_x,cur_y=q.popleft()
        for i in range(4):
            next_x,next_y=cur_x+dx[i], cur_y+dy[i]
            if(0<=next_x<n and 0<=next_y<m):
                if(visited[next_x][next_y]==False and graph[next_x][next_y]==1):
                    visited[next_x][next_y]=True
                    q.append((next_x,next_y))
                    ct+=1
    return ct
for a,b in xy:
    sol=bfs(a,b)
    if(ans<sol):
        ans=sol
print(ans)