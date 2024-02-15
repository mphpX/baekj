import sys
n=int(sys.stdin.readline())
for i in range(n):
  l=[]
  a=list(sys.stdin.readline().strip())
  result=0
  for i in a:
    if(i=='('):
      l.append(i)
    else:
      if(len(l)>0):
        l.pop()
      else:
        result=1
        break
  if(result==0 and len(l)==0):
    print("YES")
  else:
    print("NO")