import sys
input= sys.stdin.readline
graph=[list(map(int,input().split())) for _ in range(9)]
zero=[]
square=[[],[],[]]
row=[]
column=[]

for i in range(9):
    for j in range(9):
        if(graph[i][j]==0):
            zero.append((i,j))

def valid_set(x,y):
    row=set([0,1,2,3,4,5,6,7,8,9])-set(graph[x])
    cc=set([graph[j][y] for j in range(9)])
    column=set([0,1,2,3,4,5,6,7,8,9])-cc
    cs=[]
    for i in range(3):
        for j in range(3):
            cs.append(graph[x//3*3+i][y//3*3+j])
    square=set([0,1,2,3,4,5,6,7,8,9])-set(cs)
    return row&column&square

def back_track(idx):
    if(idx==len(zero)):
        for i in range(9):
            for j in range(9):
                print(graph[i][j],end=' ')
            print()
        sys.exit(0)
    cur_x,cur_y=zero[idx]
    valid=valid_set(cur_x,cur_y)
    if(len(valid)==0):
        return
    for j in valid:
        graph[cur_x][cur_y]=j
        back_track(idx+1)
        graph[cur_x][cur_y]=0
back_track(0)