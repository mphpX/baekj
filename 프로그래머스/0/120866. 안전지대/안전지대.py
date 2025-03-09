def solution(board):
    y=len(board)
    x=len(board[0])
    for i in range(y):
        for j in range(x):
            if(board[i][j]==1):
                if(i+1<y and board[i+1][j]==0):
                    board[i+1][j]=2
                if(j+1<x and board[i][j+1]==0):
                    board[i][j+1]=2
                if(i-1>=0 and board[i-1][j]==0):
                    board[i-1][j]=2
                if(j-1>=0 and board[i][j-1]==0):
                    board[i][j-1]=2
                if(i-1>=0 and j-1>=0 and board[i-1][j-1]==0):
                    board[i-1][j-1]=2
                if(i+1<y and j+1<x and board[i+1][j+1]==0):
                    board[i+1][j+1]=2
                if(i+1<y and j-1>=0 and board[i+1][j-1]==0):
                    board[i+1][j-1]=2
                if(i-1>=0 and j+1<x and board[i-1][j+1]==0):
                    board[i-1][j+1]=2
    answer=0
    for i in range(y):
        for j in range(x):
            if(board[i][j]==0):
                answer+=1
    return answer