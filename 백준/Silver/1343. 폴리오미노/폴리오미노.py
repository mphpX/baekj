board=list(input())
n=len(board)
ct=0
ans=[]
for i in range(n):
    if(board[i]=='X'):
        ct+=1
    if(i==n-1 or board[i]=='.'):
        if(ct%2==0):
            for j in range(ct//4):
                ans.append('AAAA')
            if(ct%4!=0):
                ans.append('BB')
        else:
            ans=[-1]
            break
        if(board[i]=='.'):
            ans.append('.')
        ct=0
for i in ans:
    print(i,end='')