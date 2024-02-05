n=int(input())
m=int(input())
lt=[]
ct=0
for i in range(n,m+1):
  result=0
  for j in range(2,i):
    if(i%j==0):
      result=1
      break
  if(result==0 and i!=1):
    lt.append(i)
    
o=sum(lt)
if(o!=0):
  print(o)
  print(lt[0])
else:
  print("-1")