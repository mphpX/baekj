n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)

l.sort()
ans = []

for i in range(n):
    ct = 1
    for j in range(i + 1, n):
        if l[j] < l[i] + 5:
            ct += 1
            if j == n - 1:
                ans.append(ct)
        else:
            ans.append(ct)
            break

if ans:
    m = max(ans)
    if m < 5:
        print(5 - m)
    else:
        print(0)
else:
    print(4) 