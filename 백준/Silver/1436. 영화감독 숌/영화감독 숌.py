n=int(input())
x=665
y=0
ct=0
sct=0
while(ct!=n):
  x+=1
  sct=0
  y=x
  while(sct<3 and y>0):
    if(y%10==6):
      sct+=1
    else:
      sct=0
    y=y//10
  if(sct>=3):
    ct+=1
print(x)