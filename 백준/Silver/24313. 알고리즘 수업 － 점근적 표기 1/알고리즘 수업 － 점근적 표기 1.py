a,b=map(int,input().split())
c=int(input())
n=int(input())
def f(x):
  return x*a+b

if a<c and f(n)<=c*n:
  print("1")

else:
  if(a==c):
    if(f(n)<=c*n):
      print("1")
    else:
      print("0")
  else:
    print("0")  