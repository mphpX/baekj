import sys
from collections import deque
input=sys.stdin.readline

r,c=map(int,input().split())
graph=[list(input().rstrip()) for _ in range(r)]
visited=[False] * 26
ans=0

def dfs(x,y,count):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    global ans
    ans=max(ans,count)
    for i in range(4):
        next_x,next_y=dx[i]+x,dy[i]+y
        if(0<=next_x<r and 0<=next_y<c):
            idx=ord(graph[next_x][next_y])-ord('A')
            if(visited[idx]==False):
                visited[idx]=True
                dfs(next_x,next_y,count+1)
                visited[idx]=False

visited[ord(graph[0][0])-ord('A')]=True   
dfs(0,0,1)

print(ans)