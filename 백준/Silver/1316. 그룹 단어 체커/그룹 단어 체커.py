m=int(input())

ct=0
result=0
for i in range(m):
  result=0
  n=input()
  m=len(n)
  o=n[0]
  alpha={}
  alpha[n[0]]=1
  for k in range(1,m):
    if n[k] in alpha:
      alpha[n[k]]+=1
    else:
      alpha[n[k]]=1
    if n[k]!=o:
      if alpha[n[k]]>1:
        result+=1
        break
      o=n[k]
  if(result==0):
    ct+=1
print(ct)