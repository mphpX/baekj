from collections import deque
n, k = map(int, input().split())
dur = list(map(int, input().split()))
st = 0
end = n - 1
level = 0
robot = deque([])
check = 0
for i in dur:
    if i == 0:
        check += 1
while check < k:
    level += 1
    end = (end - 1 + n * 2) % (2 * n)
    st = (st - 1 + n * 2) % (2 * n)
    if len(robot) > 0 and robot[-1] == end:
        robot.pop()
    l = len(robot)
    for i in range(l - 1, -1, -1):
        next = (robot[i] + 1) % (2 * n)
        if i == len(robot) - 1:
            if dur[next] >= 1:
                robot[i] = next
                dur[next] -= 1
                if dur[next] == 0:
                    check += 1
                if robot[i] == end:
                    robot.pop()
        else:
            if robot[i + 1] != next and dur[next] >= 1:
                robot[i] = next
                dur[next] -= 1
                if dur[next] == 0:
                    check += 1
    if dur[st] > 0:
        robot.appendleft(st)
        dur[st] -= 1
        if dur[st] == 0:
            check += 1
print(level)