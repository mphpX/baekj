def bin(target,data):
  start=0
  end=len(data)-1
  while(start<=end):
    mid=(start+end)//2
    if(data[mid]==target):
      return mid
    elif(data[mid]<target):
      start=mid+1
    else:
      end=mid-1
  return

n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
b.sort()
for i in a:
  print(bin(i,b),end=' ')