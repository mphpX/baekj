n=int(input())
l=list(map(int,input().split()))
m=1
x=[]
while(m!=n+1):  
  if(len(l)!=0):
    if(m!=l[0]):
      if(len(x)!=0 and m==x[0]):
        x.pop(0)
        m+=1
      else:
        x.insert(0,l[0])
        l.pop(0)
    else:
      l.pop(0)
      m+=1
  else:
    if(len(x)!=0):
      if(m!=x[0]):
        break
      else:
        x.pop(0)
        m+=1
if(len(x)==0 and len(l)==0):
  print("Nice")
else:
  print("Sad")