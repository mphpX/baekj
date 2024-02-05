a,b=map(int,input().split())
ct=0
result=0
for i in range(1,a+1):
  if(a%i==0):
    ct+=1
    if(ct==b):
      result=1
      print(i)
      break
if(result==0):
  print("0")