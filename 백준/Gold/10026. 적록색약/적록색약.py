import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
gh = [list(input().strip()) for _ in range(n)]

def jbfs(start_x, start_y, graph, wanted, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] in wanted:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 일반 시야
visited = [[False] * n for _ in range(n)]
fct = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            jbfs(i, j, gh, gh[i][j], visited)
            fct += 1

# 적록색약 시야
visited = [[False] * n for _ in range(n)]
sct = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if gh[i][j] in 'RG':
                jbfs(i, j, gh, 'RG', visited)
            else:
                jbfs(i, j, gh, 'B', visited)
            sct += 1

print(fct, sct)
