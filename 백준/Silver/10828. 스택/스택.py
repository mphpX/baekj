import sys
n=int(sys.stdin.readline())
s=[]
for i in range(n):
    l=list(map(str,sys.stdin.readline().split()))
    m=len(s)
    if(l[0]=='push'):
        a=int(l[1])
        s.append(a)
    elif(l[0]=='pop'):
        if(m==0):
            print(-1)
        else:
            a=s.pop()
            print(a)
    elif(l[0]=='top'):
        if(m==0):
            print(-1)
        else:
            print(s[m-1])
    elif(l[0]=='size'):
        print(m)
    elif(l[0]=='empty'):
        if(m==0):
            print(1)
        else:
            print(0)