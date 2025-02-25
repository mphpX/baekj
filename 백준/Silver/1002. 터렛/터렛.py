import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 중심 간 거리 d 계산
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # 반지름의 차이와 합
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)

    # 1. 두 원이 완전히 일치하는 경우 (무한대)
    if d == 0 and r1 == r2:
        print(-1)

    # 2. 두 원이 외부에서 만나지 않는 경우 (멀리 떨어져 있음)
    elif d > r_sum:
        print(0)

    # 3. 두 원이 내부에서 만나지 않는 경우 (한 원이 다른 원 안에 있지만 접하지 않음)
    elif d < r_diff:
        print(0)

    # 4. 두 원이 외접하는 경우 (한 점에서 만남)
    elif d == r_sum:
        print(1)

    # 5. 두 원이 내접하는 경우 (한 점에서 만남)
    elif d == r_diff:
        print(1)

    # 6. 두 점에서 만나는 경우
    else:
        print(2)
