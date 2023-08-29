import sys
arr=[]
n,m=map(int,input().split())
for i in range(n+1):
    arr.append(0)
for i in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    for j in range(x,y+1):
        arr[j]=z
for i in range(1,n+1):
    print(arr[i],end=" ")