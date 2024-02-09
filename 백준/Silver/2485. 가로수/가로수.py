def GCD(x, y):
    while y != 0:
        x, y = y, x%y
    return x
a=int(input())
l=[]
for i in range(a):
  b=int(input())
  l.append(b)
s=l[0]
for i in range(a):
  l[i]-=s

ct=0
g=GCD(l[1],l[2])
for i in range(3,a):
  g=GCD(g,l[i])

print(l[a-1]//g+1-a)