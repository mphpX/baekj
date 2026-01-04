def calculate(m, dx,dy):
    fly = 0
    for x in range(1,m):
        for p in range(4):
            cur_i= i + x*dx[p]
            cur_j= j + x*dy[p]
            if(0<=cur_i <n and 0<=cur_j<n):
                fly+=graph[cur_i][cur_j]
    return fly + graph[i][j]
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    graph= [list(map(int,input().split())) for _ in range(n)]
    dead_fly = 0
    for i in range(n):
        for j in range(n):
            ax=[0,0,1,-1]
            ay=[1,-1,0,0] 
            bx=[-1,1,-1,1]
            by=[-1,-1,1,1]
            dead_fly= max(calculate(m, ax, ay), calculate(m, bx, by), dead_fly)
    print('#',test_case,' ',dead_fly, sep='')