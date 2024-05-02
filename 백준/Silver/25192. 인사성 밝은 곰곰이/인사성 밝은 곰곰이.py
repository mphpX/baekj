import sys
n=int(sys.stdin.readline())
ct=0
result=0
for i in range(n):
    c=sys.stdin.readline().strip()
    if(c=='ENTER'):
        d=dict()
    else:
        if(c not in d):
            d[c]=1
            result+=1
print(result)