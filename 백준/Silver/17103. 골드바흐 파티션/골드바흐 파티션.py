import sys
d=[1]*1000001
d[0]=0
d[1]=0
c=[]
for i in range(2,int(1000000**(1/2))+1):
  m=2
  while(m*i<=1000000):
    d[m*i]=0
    m+=1
for i in range(1000001):
  if(d[i]==1):
    c.append(i)
n=int(sys.stdin.readline())
for i in range(n):
  a=int(sys.stdin.readline())
  ct=0
  for j in c:
    if(j>=a):
      break
    if d[a-j]==1 and j<=a-j:
      ct+=1
  print(ct)