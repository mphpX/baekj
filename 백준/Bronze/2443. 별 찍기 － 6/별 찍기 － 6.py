n=int(input())
for i in range(n):
    print(' '*i,end='')
    print('*',end='')
    for j in  range(n-i-1):
        print('**',end='')
    print()