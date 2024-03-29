import sys
sys.setrecursionlimit(10 ** 6)
n=int(sys.stdin.readline())
visited=[[0 for _ in range(n) ]for _ in range(n)]
l=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
d=0
rd=0
for i in range(n):
    a=sys.stdin.readline().strip()
    l.append(a)
def rdfs(x,y,ch):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<n and visited[nx][ny]==0):
            if(l[nx][ny]==ch):
                rdfs(nx,ny,ch)
            else:
                if(ch!='B' and l[nx][ny]!='B'):
                    rdfs(nx,ny,ch)
def dfs(x,y,ch):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<n and visited[nx][ny]==0):
            if(l[nx][ny]==ch):
                dfs(nx,ny,ch)
for i in range(n):
    for j in range(n):
        if(visited[i][j]==0):
            dfs(i,j,l[i][j])
            d+=1
visited=[[0 for _ in range(n) ]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(visited[i][j]==0):
            rdfs(i,j,l[i][j])
            rd+=1
print(d,rd)