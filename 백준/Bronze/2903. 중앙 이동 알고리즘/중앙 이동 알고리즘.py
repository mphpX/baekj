n=int(input())
ct=3
for i in range(1,n):
  ct+=2**(i)
print(ct**2)