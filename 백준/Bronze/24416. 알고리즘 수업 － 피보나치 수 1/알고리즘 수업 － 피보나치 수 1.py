m=int(input())
f=[0,1,1]
def fib(n):
  for i in range(3,n+1):
        f.append(f[i - 1] + f[i - 2]) 
  return f[n]
print(fib(m),m-2)
