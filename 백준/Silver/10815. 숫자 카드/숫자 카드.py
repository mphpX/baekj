def bin(target,l):
  start=0
  end=len(l)-1
  while(start<=end):
    mid=(start+end)//2
    if(l[mid]==target):
      return mid
    elif l[mid]<target:
      start=mid+1
    else:
      end=mid-1
  return -1
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))

for i in b:
  if bin(i,a)>=0:
    print("1",end=' ')
  else:
    print("0",end=' ')