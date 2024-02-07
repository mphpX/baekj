n,m=map(int,input().split())
c=list(map(int,input().split()))
l=len(c)
x=0
for i in range(l-2):
  for j in range(i+1,l-1):
    for k in range(j+1,l):
      s=c[i]+c[j]+c[k]
      if(s<=m and x<s):
        x=s
print(x)