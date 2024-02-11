a,b=map(int,input().split())
for i in range(a,b+1):
  if(i<=1):
    i=1
  else:
    result=1
    for j in range(2,int(i**(1/2)+1)):
      if(i%j==0):
        result=0
        break
    if(result==1):
      print(i)