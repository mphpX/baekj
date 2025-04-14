import sys
from collections import deque
input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[[0 for _ in range(n)]for _ in range(m)]
for i in range(k):
    min_x,min_y,max_x,max_y=map(int,input().split())
    for j in range(min_x,max_x):
        for l in range(min_y,max_y):
            graph[j][l]=1
visit=[[0 for _ in range(n)]for _ in range(m)]
ans=[]
def bfs(x,y,n,m):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q=deque([(x,y)])
    visit[x][y]=1
    ct=1
    while(q):
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x,next_y=dx[i]+cur_x, dy[i]+cur_y
            if(0<=next_x<m and 0<=next_y<n):
                if(visit[next_x][next_y]==0 and graph[next_x][next_y]==0):
                    visit[next_x][next_y]=1
                    q.append((next_x,next_y))
                    ct+=1
    return ct
for i in range(m):
    for j in range(n):
        if(visit[i][j]==0 and graph[i][j]==0):
            ans.append(bfs(i,j,n,m))
ans.sort()
print(len(ans))
for i in ans:
    print(i,end=' ')