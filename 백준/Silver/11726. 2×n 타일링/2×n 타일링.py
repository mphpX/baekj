import sys
arr=[0,1,2]
n=int(input())
for i in range(3,n+1):
    arr.append((arr[i-1]+arr[i-2])%10007)
print(arr[n])