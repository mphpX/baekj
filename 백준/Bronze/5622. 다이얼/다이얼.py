import sys
arr=input()
sum=0
x=1
for i in arr:
    z=ord(i)
    if(z==90):z-=2
    elif(z>=83):z-=1
    x=(z-65)//3+3
    sum+=x
print(sum)
