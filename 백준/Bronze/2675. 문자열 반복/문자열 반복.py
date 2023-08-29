import sys
n=int(input())
for i in range(n):
    arr=sys.stdin.readline()
    for i in range(len(arr)-3):
        for j in range(int(arr[0])):
            print(arr[i+2],end="")
    print()