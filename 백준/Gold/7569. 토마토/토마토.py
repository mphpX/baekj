from collections import deque
n,m,h=map(int,input().split())
graph=[[]for _ in range(h)]
q=deque()
for i in range(h):
    for j in range(m):
        l=list(map(int,input().split()))
        for k in range(n):
            if l[k] == 1:
                q.append((i, j, k))
        graph[i].append(l)

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
while(q):
    cz,cx,cy=q.popleft()
    for i in range(6):
        nz=dz[i]+cz
        nx=dx[i]+cx
        ny=dy[i]+cy
        if(0<=nz<h and 0<=nx<m and 0<=ny<n):
            if(graph[nz][nx][ny]==0):
                graph[nz][nx][ny]=graph[cz][cx][cy]+1
                q.append((nz,nx,ny))
ans=0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if(graph[i][j][k]==0):
                print(-1)
                exit(0)
            elif(graph[i][j][k]>ans):
                ans=graph[i][j][k]-1
print(ans)