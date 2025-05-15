from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(input().strip()) for _ in range(n)]
fire=deque([])
dx=[1,0,-1,0]
dy=[0,1,0,-1]
s_x,s_y=0,0
for i in range(n):
    for j in range(m):
        if(graph[i][j]=='F'):
            fire.append((i,j))
        elif(graph[i][j]=='J'):
            s_x=i
            s_y=j
visited=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
for x,y in fire:
    visited[1][x][y]=1
ans=[]
def bfs(a,b):
    q=deque([(a,b)])
    visited[0][a][b]=1
    while(q):
        cur_x,cur_y=q.popleft()
        if(cur_x==n-1 or cur_y==m-1 or cur_x==0 or cur_y==0):
            ans.append((cur_x,cur_y))
        for i in range(4):
            next_x=cur_x+dx[i]
            next_y=cur_y+dy[i]
            if(0<=next_x<n and 0<=next_y<m):
                if(visited[0][next_x][next_y]==0 and graph[next_x][next_y]=='.'):
                    q.append((next_x,next_y))
                    visited[0][next_x][next_y]=visited[0][cur_x][cur_y]+1
#경로 기억해놓고 visited 배열 값이 만약에 같아지면 잡히는거임.
def firing():
    while(fire):
            f_x,f_y=fire.popleft()
            for i in range(4):
                nf_x=f_x+dx[i]
                nf_y=f_y+dy[i]
                if(0<=nf_x<n and 0<=nf_y<m):
                    if(visited[1][nf_x][nf_y]==0 and graph[nf_x][nf_y]!='#'):
                        fire.append((nf_x,nf_y))
                        visited[1][nf_x][nf_y]+=visited[1][f_x][f_y]+1
mn=1000001
bfs(s_x,s_y)
firing()
for x,y in ans:
    if(visited[0][x][y] < visited[1][x][y] or visited[1][x][y]==0):
        if(visited[0][x][y]<mn):
            mn=visited[0][x][y]
'''for i in visited[0]:
    print(i)
print("fire")
for i in visited[1]:
    print(i)
print(ans)'''
if(mn==1000001):
    print("IMPOSSIBLE")
else: print(mn)