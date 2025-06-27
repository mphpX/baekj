n=int(input())
for i in range(1,n):
    print('*'*i,end='')
    print(' '*(2*n-2*i),end='')
    print('*'*i,end='')
    print()
for i in range(n):
    print('*'*(n-i),end='')
    print(' '*(2*i),end='')
    print('*'*(n-i),end='')
    print()