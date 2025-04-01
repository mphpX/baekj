import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[]
for i in range(n):
    l=list(map(int,input().split()))
    graph.append(l)
def bfs(graph,start_x,start_y,limit):
    q=deque([(start_x,start_y)])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while(q):
        cur_x,cur_y=q.popleft()
        for i in range(4):
            next_x=cur_x+dx[i]
            next_y=cur_y+dy[i]
            if(0<=next_x<n and 0<=next_y<n and visit[next_x][next_y]==False and graph[next_x][next_y]>limit):
                visit[next_x][next_y]=True
                q.append((next_x,next_y))

ans=[]
h=0
while(True):
    ct=0
    visit=[[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(graph[i][j]>h and visit[i][j]==False):
                bfs(graph,i,j,h)
                ct+=1
    ans.append(ct)
    h+=1
    if(ct==0):
        break
print(max(ans))