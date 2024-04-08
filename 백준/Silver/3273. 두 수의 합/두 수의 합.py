import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline())
num.sort()
left=0
right=n-1
ct=0
while(left<right):
    s=num[left]+num[right]
    if(s<x):
        left+=1
    elif(s>x):
        right=right-1
    else:
        left+=1
        ct+=1
print(ct)