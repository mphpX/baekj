import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 번호가 작은 정점부터 방문하도록 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 방문 여부
dfs_visit = [False for _ in range(n + 1)]

# DFS 함수
def dfs(start):
    print(start, end=' ')
    dfs_visit[start] = True
    for i in graph[start]:
        if not dfs_visit[i]:
            dfs(i)

# BFS 함수
def bfs(start):
    bfs_visit = [False for _ in range(n + 1)]
    q = deque([start])
    bfs_visit[start] = True
    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for i in graph[cur]:
            if not bfs_visit[i]:
                q.append(i)
                bfs_visit[i] = True
    return ans

# 실행 및 출력
dfs(v)
print()
for i in bfs(v):
    print(i, end=' ')
