import sys
arr=[]
for i in range(9):
    x=int(input())
    arr.append(x)
m=max(arr)
for i in range(9):
    if(arr[i]==m):
        print("%d\n%d" %(arr[i],i+1))
        break