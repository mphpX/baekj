T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    graph= [list(map(int,input().split())) for _ in range(n)]
    dead_fly = 0
    for i in range(n):
        for j in range(n):
            # 격자
            low_i = max(i - m + 1, 0)
            low_j = max(j - m + 1, 0)
            high_i = min(i + m - 1, n - 1)
            high_j = min(j + m - 1, n - 1)
            a_fly = sum(graph[i][low_j: high_j+1])- graph[i][j]
            a_fly += sum(graph[x][j] for x in range(low_i, high_i+1))
            # X자
            b_fly = 0
            dx=[-1,1,-1,1]
            dy=[-1,-1,1,1]
            for x in range(1,m):
                for p in range(4):
                    cur_i= i + x*dx[p]
                    cur_j= j + x*dy[p]
                    if(0<=cur_i <n and 0<=cur_j<n):
                        b_fly+=graph[cur_i][cur_j]
            dead_fly= max(dead_fly, b_fly+ graph[i][j], a_fly)
    print('#',test_case,' ',dead_fly, sep='')