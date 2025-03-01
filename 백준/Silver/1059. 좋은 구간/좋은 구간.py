lth=int(input())
l=list(map(int,input().split()))
l.sort()
n=int(input())
x=0
for i in range(lth):
    if(n<l[i]):
        x=i
        break
if(n in l):
    print(0)
elif(x==0):
    print((l[x]-n)*n-1)
else:
    print((l[x]-n)*(n-l[x-1])-1)