n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
d_1=[[(1,0),(1,0),(1,0)],   [(0,1),(0,1),(0,1)]]
d_2=[[(1,0),(0,1),(-1,0)]]
d_3=[[(0,1),(1,0),(1,0)],   [(0,-1),(1,0),(1,0)],   [(1,0),(1,0),(0,1)],[(0,1),(-1,0),(-1,0)],
     [(1,0),(0,1),(0,1)], [(-1,0),(0,1),(0,1)], [(1,0),(0,-1),(0,-1)], [(0,1),(0,1),(1,0)]]
d_4=[[(1,0),(0,1),(1,0)], [(1,0),(0,-1),(1,0)],
     [(0,1),(1,0),(0,1)], [(0,1),(-1,0),(0,1)]]
d_5=[[(1,1),(-1,0),(0,1)],  [(-1,1),(1,0),(0,1)],
     [(1,1),(0,-1),(1,0)], [(1,-1), (0,1), (1,0)]]
d=[d_1,d_2,d_3,d_4,d_5]
def bfs(x,y,a):
    ans=0
    for i in d[a]:
        cur_x,cur_y=x,y
        candidate=graph[x][y]
        for dx,dy in i:
            cur_x,cur_y=cur_x+dx,cur_y+dy
            if(0<=cur_x<n and 0<=cur_y<m):
                candidate+=graph[cur_x][cur_y]
            else:
                candidate=0
                break
        ans=max(ans,candidate)
    return ans
result=0
for i in range(n):
    for j in range(m):
        for k in range(5):
            result=max(bfs(i,j,k),result)
print(result)