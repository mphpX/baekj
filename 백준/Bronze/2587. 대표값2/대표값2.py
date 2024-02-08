l=[0]*10
s=0
for i in range(5):
  b=int(input())
  l[b//10]+=1
  s+=b
ct=0
print(s//5)
for i in range(10):
  if(l[i]>0):
    ct+=l[i]
  if(ct>=3):
    print(i*10)
    break
