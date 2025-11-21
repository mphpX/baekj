T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    graph= [ list(map(int,input().split())) for _ in range(n)]
    mx= 0
    cur= 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cur = 0
            for x in range(i, i+m):
                cur+= sum(graph[x][j: j+m])
            mx= max(mx, cur)
    print('#',test_case,' ', mx, sep='')