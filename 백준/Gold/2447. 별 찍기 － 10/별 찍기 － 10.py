n=int(input())
sample=[['*','*','*'],['*',' ','*'],['*','*','*']]

def recur2(m,x,y):
    if(m==3):
        print(sample[x%3][y%3],end='')
        return
    else:
        if((x%m)//(m//3)==1 and (y%m)//(m//3)==1):
            print(' ',end='')
            return
        recur2(m//3,x,y)
if(n==1):
    print('*')
else:
    for i in range(n):
        for j in range(n):
            recur2(n,i,j)
        print()
