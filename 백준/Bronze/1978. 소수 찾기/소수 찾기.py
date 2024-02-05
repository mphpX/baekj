n=int(input())
lt=map(int,input().split())
ct=0
for i in lt:
  result=0
  for j in range(2,i):
    if(i%j==0):
      result=1
      break
  if(result==0 and i!=1):
    ct+=1
print(ct)