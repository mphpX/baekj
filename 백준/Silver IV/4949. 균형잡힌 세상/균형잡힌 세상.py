import sys
a=list(sys.stdin.readline().strip('\n'))
while(a!=['.']):
  if(a[len(a)-1]!='.'):
    b=list(sys.stdin.readline().strip('\n'))
    a=a+b
  else:
    x=[]
    result=0
    for i in a:
      if(i=='(' or i=='['):
        x.append(i)
      elif(i==')'):
        if(len(x)>0 and x[len(x)-1]=='('):
          x.pop()
        else:
          result=1
          break
      elif(i==']'):
        if(len(x)>0 and x[len(x)-1]=='['):
          x.pop()
        else:
          result=1
          break
    if(result==0 and len(x)==0):
      print("yes")
    else:
      print("no")
    a=list(sys.stdin.readline().strip('\n'))