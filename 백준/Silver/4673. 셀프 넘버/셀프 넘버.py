num=[True for _ in range(10001)]
def check(x):
    result=x
    while(x):
        result+=x%10
        x//=10
    return result
for i in range(1,10001):
    x=check(i)
    if(x<10001):
        num[x]=False
for i in range(1,10001):
    if(num[i]==True):
        print(i)