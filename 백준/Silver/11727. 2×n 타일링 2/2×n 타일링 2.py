import sys
arr=[0,1,3]
n=int(input())
for i in range(3,n+1):
    arr.append((arr[i-1]+2*arr[i-2])%10007)
print(arr[n])