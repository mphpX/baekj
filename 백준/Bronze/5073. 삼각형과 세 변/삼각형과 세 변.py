x=list(map(int,input().split()))
while(x.count(0)!=3):
  m=0
  if(2*max(x)>=sum(x) and x.count(x[0])!=3):
    print("Invalid")
  else:
    for i in x:
      if(x.count(i)>m):
        m=x.count(i)
    if(m==1):
      print("Scalene")
    elif(m==2):
      print("Isosceles")
    else:
      print("Equilateral")
  x=list(map(int,input().split()))
  