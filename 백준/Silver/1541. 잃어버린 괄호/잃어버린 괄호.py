import sys
a=sys.stdin.readline().strip()
l=[]
result=[]
x=0
for i in range(len(a)):
    if(a[i].isalnum()==True):
        if(x==0):
            x=int(a[i])
        else:
            x*=10
            x+=int(a[i])
        if(i==len(a)-1):
            l.append(x)
    else:
        l.append(x)
        x=0
        l.append(a[i])
ct=0
while(ct<len(l)):
    if(l[ct]=='-'):
        break
    ct+=1
x=0
y=0
for i in range(0,len(l),2):
    if(i<ct):
        x+=l[i]
    else:
        y+=l[i]
print(x-y)