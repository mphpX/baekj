import sys
x=int(input())
n=64
l=[64]
while(x<sum(l)):
    l[len(l)-1]//=2
    l.append(l[len(l)-1])
    if(sum(l)-l[len(l)-1]>=x):
        l.pop()
print(len(l))