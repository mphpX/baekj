import sys
n = int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
a.sort()
result=0
for i in range(n):
    result+=(n-i)*a[i]
print(result)