import sys
input= sys.stdin.readline
n=int(input())
weight=[int(input()) for _ in range(n)]
weight.sort()
previous=weight[n-1]
for i in range(n-2,-1,-1):
    previous=max(previous, weight[i]*(n-i))
print(previous)