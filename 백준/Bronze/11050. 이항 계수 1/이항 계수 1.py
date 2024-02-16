n,m=map(int,input().split())
o=1
for i in range(m):
  o*=n-i
for i in range(1,m+1):
  o//=i
print(o)