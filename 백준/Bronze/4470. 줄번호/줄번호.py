n=int(input())
l=[input() for _ in range(n)]
for i in range(n):
    print(i+1,'.',sep='',end=' ')
    print(l[i])