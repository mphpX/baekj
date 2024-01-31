m=input()
n=len(m)
o=1
for i in range(n//2):
  if m[i]!=m[n-1-i]:
    o=0
    break
print(o)