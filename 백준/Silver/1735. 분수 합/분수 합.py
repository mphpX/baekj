def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=y[0]*x[1]+x[0]*y[1]
b=x[1]*y[1]
c=GCD(a,b)
print(a//c,b//c)