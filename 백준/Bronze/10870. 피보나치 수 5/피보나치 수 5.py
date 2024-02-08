def fibo(n):
  if(n==1 or n==2):
    return 1
  elif(n==0):
    return 0
  while(n>0):
    return fibo(n-1)+fibo(n-2)
a=int(input())
print(fibo(a))