import sys
n=int(sys.stdin.readline().strip())
l=[]
for i in range(n):
  a=list(map(int,sys.stdin.readline().split()))
  b=len(l)
  if(a[0]==1):
    l.append(a[1])
  elif(a[0]==2):
    if(b==0):
      print(-1)
    else:
      print(l[b-1])
      l.pop()
  elif(a[0]==3):
    print(b)
  elif(a[0]==4):
    if(b==0):
      print(1)
    else:
      print(0)
  else:
    if(b==0):
      print(-1)
    else:
      print(l[b-1])