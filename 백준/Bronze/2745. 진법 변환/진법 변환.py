x,y=input().split()
y=int(y)
n=len(x)
result=0
for i in range(n):
  if(ord(x[i])-55<10 or ord(x[i])-55>35):
    result+=int(x[i])*(y ** (n-i-1))
  else:
    result+=(ord(x[i])-55) *(y ** (n-i-1))
print(result)