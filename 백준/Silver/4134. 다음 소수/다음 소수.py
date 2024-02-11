import sys
n=int(input())
for i in range(n):
  a=int(sys.stdin.readline())
  result=1
  while(result==1):
    if(a==2 or a==1 or a==0):
      print("2")
      break
    for j in range(2,int(a**(1/2)+1)):
      if(a%j==0):
        result=0
        break
    if(result==1):
      print(a)
      break
    else:
      result=1
    a+=1