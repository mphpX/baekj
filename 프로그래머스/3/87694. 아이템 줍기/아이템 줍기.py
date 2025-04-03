from collections import deque
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배로 확장
    rectangle = [[x * 2 for x in rect] for rect in rectangle]
    characterX, characterY = characterX * 2, characterY * 2
    itemX, itemY = itemX * 2, itemY * 2

    # 그래프 초기화
    graph = [[0] * 102 for _ in range(102)]
    visit = [[0] * 102 for _ in range(102)]

    # 사각형 테두리 및 내부 그리기
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                graph[i][j] = 1  # 우선 모두 채우고

    # 내부 지우기 (테두리만 남김)
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                graph[i][j] = 0  # 내부 제거

    # BFS 시작
    def bfs(x, y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = deque([(x, y)])
        visit[x][y] = 1

        while q:
            curx, cury = q.popleft()
            for i in range(4):
                nextx, nexty = curx + dx[i], cury + dy[i]
                if 0 <= nextx < 102 and 0 <= nexty < 102:
                    if graph[nextx][nexty] == 1 and visit[nextx][nexty] == 0:
                        visit[nextx][nexty] = visit[curx][cury] + 1
                        q.append((nextx, nexty))

    bfs(characterX, characterY)

    # 최종 거리 반환 (절반으로 나눔)
    return (visit[itemX][itemY] - 1) // 2
