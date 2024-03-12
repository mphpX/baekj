import sys
n=int(input())
for i in range(n):
    h,w,n=map(int,sys.stdin.readline().split())
    a=(n-1)//h+1
    b=(n-1)%h+1
    print(b*100+a)        