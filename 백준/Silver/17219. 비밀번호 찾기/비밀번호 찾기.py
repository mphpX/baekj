import sys
n,m=map(int,sys.stdin.readline().split())
a=dict()
for i in range(n):
    x,y=sys.stdin.readline().split()
    a[x]=y
for i in range(m):
    o=sys.stdin.readline().strip()
    print(a[o])