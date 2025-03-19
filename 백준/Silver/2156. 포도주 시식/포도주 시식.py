import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]  # 리스트 컴프리헨션 사용 (더 깔끔하고 빠름)

if n == 1:
    print(wine[0])
    exit()

dp = [0] * n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2:
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n-1])  # 최대로 마실 수 있는 와인양 출력