visited=[[False for _ in range(101)]for _ in range(101)]
ct=0
for i in range(4):
    fx,fy,sx,sy=map(int,input().split())
    for i in range(fx,sx):
        for j in range(fy,sy):
            if(visited[i][j]==False):
                visited[i][j]=True
                ct+=1
print(ct)