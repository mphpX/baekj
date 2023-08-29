import sys
n=int(input())
for i in range(n):
    arr=sys.stdin.readline()
    print(arr[0]+arr[len(arr)-2])