import sys
arr=[[1,0],[0,1]]
n=int(input())
for i in range(2,41):
    arr.append([arr[i-1][0]+arr[i-2][0],arr[i-1][1]+arr[i-2][1]])
for i in range(n):
    a=int(input())
    print("%d %d"%(arr[a][0],arr[a][1]))