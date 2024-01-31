m=input().upper()
alp=dict()
for i in m:
  if i in alp:
    alp[i]+=1
  else:
    alp[i]=1
cnt=0
mk=max(alp, key=alp.get)
m=alp[mk]
for i in alp:
  if alp[i]==alp[mk]:
    cnt+=1
if(cnt==1):
  print(mk)
else:
  print("?")