p=int(input())
for i in range(p):
  q,r=map(int,input().split())
  m=min(q,r)
  n=max(q,r)
  o=1
  for i in range(m):
    o*=n-i
  for i in range(1,m+1):
    o//=i
  print(o)