a=int(input())
b=int(input())
ans=a*b
ct=10
while(b):
    print(a*(b%10))
    b=b//10
print(ans)