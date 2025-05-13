import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(input().strip()) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs():
    visited=[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(2)]
    q=deque([(0,0,0)])
    ct=0
    visited[0][0][0]=0
    while(q):
        cur_x,cur_y,state=q.popleft()
        for i in range(4):
            next_x,next_y=cur_x+dx[i],cur_y+dy[i]
            if(0<=next_x<n and 0<=next_y<m):
                if(visited[state][next_x][next_y]==-1):
                    if(graph[next_x][next_y]=='0'):
                        q.append((next_x,next_y,state))
                        visited[state][next_x][next_y]=visited[state][cur_x][cur_y]+1
                    else:
                        if(state==0):
                            q.append((next_x,next_y,state+1))
                            visited[state+1][next_x][next_y]=visited[state][cur_x][cur_y]+1
    ans=[]
    if(visited[0][n-1][m-1]!=-1):
        ans.append(visited[0][n-1][m-1])
    if(visited[1][n-1][m-1]!=-1):
        ans.append(visited[1][n-1][m-1])
    return ans
ans=bfs()
if(len(ans)==0):
    print(-1)
else:
    print(min(ans)+1)