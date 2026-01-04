n= int(input())
ans = 0
while(n):
    ans+= n%10
    n//=10
print(ans)