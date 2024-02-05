x=dict()
y=dict()
for i in range(3):
  a,b=map(int,input().split())
  if a in x:
    x[a]+=1
  else:
    x[a]=1
  if b in y:
    y[b]+=1
  else:
    y[b]=1

for i in x:
  if(x[i]==1):
    print(i,end=' ')
for i in y:
  if(y[i]==1):
    print(i,end=' ')