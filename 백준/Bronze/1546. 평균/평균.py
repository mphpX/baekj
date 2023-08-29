import sys
n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
sum=0
for i in range(n):
    arr[i]=arr[i]/m*100
    sum+=arr[i]
print(sum/n)