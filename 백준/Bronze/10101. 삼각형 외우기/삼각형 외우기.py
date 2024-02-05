a=[]
for i in range(3):
  n=int(input())
  a.append(n)
if(sum(a)!=180):
  print("Error")
else:
  if(a.count(60)==3):
    print("Equilateral")
  else:
    r=0
    for i in a:
      if(a.count(i)==2):
        print("Isosceles")
        r=1
        break
    if(r==0):
      print("Scalene")