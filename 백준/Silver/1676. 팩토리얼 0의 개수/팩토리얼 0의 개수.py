n=int(input())
a=0
b=0
x=1
y=1
ct1=0
ct2=0
while(x<n):
    x*=2
    a+=1
while(y<n):
    y*=5
    b+=1
for i in range(1,a+1):
    x=2**i
    ct1+=n//x
for i in range(1,b+1):
    y=5**i
    ct2+=n//y
print(min(ct1,ct2))