import sys
input = sys.stdin.readline
n,m=map(int,input().split())
d=dict()
for i in range(n):
    a,b=map(str,input().split())
    d[a]=b
for i in range(m):
    a=input().strip()
    print(d[a])