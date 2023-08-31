import sys
n=int(input())
a=0
b=1
c=0
for i in range(1,n):
    c=a+b
    a=b
    b=c
if(n==0):print(a)
elif(n==1):print(b)
else:print(c)