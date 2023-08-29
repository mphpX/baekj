import sys
n,m=map(int,input().split())
arr1=[]
arr2=[]
for i in range(n):
    num=list(map(int,sys.stdin.readline().split()))
    arr1.append(num)
for i in range(n):
    num=list(map(int,sys.stdin.readline().split()))
    arr2.append(num)
for i in range(n):
    for j in range(m):
        arr1[i][j]+=arr2[i][j]
        print(arr1[i][j],end=" ")
    print()