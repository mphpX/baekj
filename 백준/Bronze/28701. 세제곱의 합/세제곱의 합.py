n=int(input())
first=0
third=0
for i in range(1,n+1):
    first+=i
for i in range(1,n+1):
    third+=i*i*i
print(first)
print(first*first)
print(third)