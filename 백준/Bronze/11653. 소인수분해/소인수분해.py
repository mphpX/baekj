n=int(input())
lt=[]
i=2
while(n>=i):
  if(n%i==0):
    n/=i
    lt.append(i)
  else:
    i+=1
for i in lt:
  print(i)