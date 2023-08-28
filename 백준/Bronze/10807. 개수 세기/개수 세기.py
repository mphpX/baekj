import sys
n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
m=int(input())
ct=0
for i in range(n):
    if(arr[i]==m):
        ct+=1
print(ct)