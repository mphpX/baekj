import sys
def bin(target,data):
    s=0
    e=len(data)-1
    while s<=e:
        mid=(s+e)//2
        if data[mid]==target:
            return mid
        elif data[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return -1
n=int(input())
l=list(map(int,input().split()))
l.sort()
m=int(input())
o=list(map(int,input().split()))
for i in o:
    if(bin(i,l)>=0):
        print(1)
    else:
        print(0)