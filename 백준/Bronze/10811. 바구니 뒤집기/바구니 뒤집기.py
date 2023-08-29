import sys
arr=[]
n,m=map(int,input().split())
for i in range(n+1):
    arr.append(i)
for i in range(m):
    p,q=map(int,sys.stdin.readline().split())
    for j in range(p,p+(q-p)//2+1):
        temp=arr[j]
        arr[j]=arr[q+p-j]
        arr[q+p-j]=temp
for i in range(n):
    print(arr[i+1],end=" ")