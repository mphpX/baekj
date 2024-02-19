# 1<=n<=123456
import sys
d=dict()
for i in range(1,2*123456):
  d[i]=1
d[1]=0
for i in range(2,int((123456*2)**(1/2))+1):
  m=2
  while(m*i<=123456*2):
    d[m*i]=0
    m+=1
n=int(sys.stdin.readline())
while(n!=0):
  s=0
  for i in range(n+1,2*n+1):
    s+=d[i]
  print(s)
  n=int(sys.stdin.readline())