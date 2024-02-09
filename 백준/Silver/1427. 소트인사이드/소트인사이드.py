a=list(input())
for i in range(len(a)):
  a[i]=int(a[i])
a.sort(reverse=True)
for i in a:
  print(i,end='')