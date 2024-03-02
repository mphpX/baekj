import sys
x = int(sys.stdin.readline())
arr1 =list(map(int,sys.stdin.readline().split()))
arr1.reverse()
arr2 = []
for i in range(x,0,-1):
    a = arr1[x-i]
    arr2.insert(a,i)
for i in range(x):
    print(arr2[i],end=' ')