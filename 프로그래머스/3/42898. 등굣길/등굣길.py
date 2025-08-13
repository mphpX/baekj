def solution(m, n, puddles):
    graph=[[0 for _ in range(m)]for _ in range(n)]
    visited=[[0 for _ in range(m)]for _ in range(n)]
    for x,y in puddles:
        graph[y-1][x-1]=1
    dx=[1,0]
    dy=[0,1]
    visited[0][0]=1
    for i in range(n):
        for j in range(m):
            what= []
            if(visited[i][j]==0 and graph[i][j]==0):
                for k in range(2):
                    pre_x, pre_y = i- dx[k], j-dy[k]
                    if(0<=pre_x<n and 0<=pre_y < m):
                        visited[i][j]=(visited[i][j]+visited[pre_x][pre_y])%1000000007
    return visited[n-1][m-1]