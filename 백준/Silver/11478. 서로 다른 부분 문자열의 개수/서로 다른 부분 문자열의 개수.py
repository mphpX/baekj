d=set()
a=input()
for i in range(len(a)):
  for j in range(i+1,len(a)+1):
    b=str(a[i:j])
    d.add(b)
print(len(d))