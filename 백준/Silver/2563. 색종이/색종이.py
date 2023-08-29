import sys
arr=[[0]*100 for _ in range(100)]
n=int(input())
ct=0
for _ in range(n):
    p,q=map(int,sys.stdin.readline().split())
    for i in range(p-1,p+9):
        for j in range(q-1,q+9):
            arr[i][j]=1
for i in range(100):
    ct+=arr[i].count(1)
print(ct)