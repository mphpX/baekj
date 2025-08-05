from collections import deque
def solution(maps):
    x= len(maps)
    y= len(maps[0])
    visited= [[0 for _ in range(y)] for _ in range(x)]
    answer = 0
    q=deque([(0,0)])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    visited[0][0]=1
    while(q):
        cur_x,cur_y= q.popleft()
        for i in range(4):
            next_x, next_y = cur_x+ dx[i], cur_y+ dy[i]
            if(0<=next_x<x and 0<= next_y<y):
                if(maps[next_x][next_y]!=0 and visited[next_x][next_y]==0):
                    visited[next_x][next_y]= visited[cur_x][cur_y]+1
                    q.append((next_x,next_y))
    ans=visited[x-1][y-1]
    if ans:
        return ans
    else:
        return -1
        