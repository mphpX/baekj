import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ids = [i for i in range(n + 1)]

def root(a):
    if ids[a] != a:
        ids[a] = root(ids[a])  # 경로 압축
    return ids[a]

def connected(a, b):
    return root(a) == root(b)

def union(a, b):
    ra = root(a)
    rb = root(b)
    if ra != rb:
        ids[rb] = ra  # 또는 반대로 해도 무방 (union by rank까지 구현하려면 배열 하나 더 필요)

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        print("YES" if connected(a, b) else "NO")
