def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a,b=map(int,input().split())
print(a*b//GCD(a,b))