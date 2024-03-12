a=int(input())
b=int(input())
c=int(input())
d=[0 for i in range(10)]
result=a*b*c
while(result>0):
    e=result%10
    result//=10
    d[e]+=1
for i in range(10):
    print(d[i])