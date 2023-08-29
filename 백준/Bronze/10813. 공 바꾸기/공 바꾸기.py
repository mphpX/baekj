import sys
arr=[]
n,m=map(int,input().split())
for i in range(n+1):
    arr.append(i)

for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    temp=arr[y]
    arr[y]=arr[x]
    arr[x]=temp
for i in range(1,n+1):
    print(arr[i],end=" ")