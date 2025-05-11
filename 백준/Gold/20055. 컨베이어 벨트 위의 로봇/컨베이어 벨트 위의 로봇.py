from collections import deque

# 입력: n은 벨트 길이의 절반, k는 내구도가 0인 칸의 개수가 k개 이상일 때 종료
n, k = map(int, input().split())
dur = list(map(int, input().split()))  # 내구도 배열

st = 0            # 로봇이 올라가는 위치 인덱스 (start)
end = n - 1       # 로봇이 내려가는 위치 인덱스 (end)
level = 0         # 단계 수 (정답)

robot = deque([]) # 로봇의 현재 위치를 저장하는 큐

# 내구도 0인 칸 개수 세기
check = 0
for i in dur:
    if i == 0:
        check += 1

# 시뮬레이션 시작
while check < k:
    level += 1

    # 1. 벨트 한 칸 회전 (start와 end 위치 모두 -1 회전)
    end = (end - 1 + n * 2) % (2 * n)
    st = (st - 1 + n * 2) % (2 * n)

    # 회전 직후, 로봇이 end 위치에 있다면 내려줘야 함
    if len(robot) > 0 and robot[-1] == end:
        robot.pop()

    # 2. 로봇을 한 칸씩 이동
    l = len(robot)
    for i in range(l - 1, -1, -1):  # 뒤에서부터 순서대로 이동 (먼저 올라간 로봇부터)
        next = (robot[i] + 1) % (2 * n)

        if i == len(robot) - 1:
            # 마지막 로봇은 앞에 로봇 없음 → 그냥 조건만 보고 이동
            if dur[next] >= 1:
                robot[i] = next
                dur[next] -= 1
                if dur[next] == 0:
                    check += 1
                if robot[i] == end:  # 이동한 위치가 내리는 위치라면 내려줌
                    robot.pop()
        else:
            # 앞에 로봇이 있다면, 그 위치가 아닌 경우에만 이동 가능
            if robot[i + 1] != next and dur[next] >= 1:
                robot[i] = next
                dur[next] -= 1
                if dur[next] == 0:
                    check += 1

    # 3. 로봇 올리기
    if dur[st] > 0:
        robot.appendleft(st)
        dur[st] -= 1
        if dur[st] == 0:
            check += 1

# 종료되면 현재 level 출력
print(level)
