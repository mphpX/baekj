import sys
arr=[0,1,2,4]
n=int(input())
for i in range(4,11):
    arr.append(arr[i-1]+arr[i-2]+arr[i-3])
for i in range(n):
    m=int(input())
    print(arr[m])