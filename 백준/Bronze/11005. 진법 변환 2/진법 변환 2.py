x,y=map(int,input().split())
z=1
ct=0
while(x//z>0):
  ct+=1
  z*=y
for i in range(ct):
  s=(y**(ct-i-1))
  if(x//s>=10):
    print(chr(x//s+55),end='')
  else:
    print(x//s,end='')
  x-=x//s*s