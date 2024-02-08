def fibo(n):
  if(n==0):
    return 1
  while(n>0):
    return fibo(n-1)*n
a=int(input())
print(fibo(a))