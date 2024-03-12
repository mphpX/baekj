import sys 
l=list(map(int,input().split()))
result=0
for i in l:
    result+=i**2
print(result%10)