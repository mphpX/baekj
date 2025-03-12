from collections import deque
t=int(input())
for i in range(t):
    p=input()
    n=int(input())
    ch=input()
    l=deque(ch[1:-1].split(','))
    ct=0
    error=0
    for i in p:
        if(i=='R'):
            ct+=1
        if(i=='D'):
            if(ct%2==0):
                if(n>0):
                    l.popleft()
                    n-=1
                else:
                    error=1
                    break
            else:
                if(n>0):
                    l.pop()
                    n-=1
                else:
                    error=1
                    break
    if(error==1):
        print('error')
    elif(ct%2==0):
        if(n==0):
            print('[]')
        else:
            print('[',end='')
            for i in range(n-1):
                print(l[i],end=',')
            print(l[n-1],end='')
            print(']')
    else:
        l.reverse()
        if(n==0):
            print('[]')
        else:
            print('[',end='')
            for i in range(n-1):
                print(l[i],end=',')
            print(l[n-1],end='')
            print(']')
            