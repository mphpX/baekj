n=int(input())

def recur2(m,x,y):
    if(m==1):
        print('*',end='')
    else:
        if((x%m)//(m//3)==1 and (y%m)//(m//3)==1):
            print(' ',end='')
            return
        recur2(m//3,x,y)

for i in range(n):
    for j in range(n):
        recur2(n,i,j)
    print()
