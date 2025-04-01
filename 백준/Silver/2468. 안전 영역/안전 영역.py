import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# BFS로 안전 영역 탐색
def bfs(start_x, start_y, limit):
    q = deque([(start_x, start_y)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if (
                0 <= next_x < n and 0 <= next_y < n
                and not visit[next_x][next_y]
                and graph[next_x][next_y] > limit
            ):
                visit[next_x][next_y] = True
                q.append((next_x, next_y))

# 높이(h)를 0부터 1씩 올려가며 시뮬레이션
ans = []
h = 0

while True:
    ct = 0
    visit = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visit[i][j]:
                bfs(i, j, h)
                ct += 1

    ans.append(ct)
    h += 1
    if ct == 0:
        break

# 안전 영역 최대 개수 출력
print(max(ans))
