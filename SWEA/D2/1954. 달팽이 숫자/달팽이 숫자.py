T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    snail= [[0 for _ in range(n)] for _ in range(n)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    dxy=0
    idx=1
    x,y=-1,0
    while(idx<=n*n):
        nx= x+dx[dxy]
        ny= y+dy[dxy]
        if(0<=nx <n and 0<=ny<n and snail[ny][nx]==0):
            x,y=nx,ny
            snail[ny][x]= idx
            idx+=1
        else:
            dxy= (dxy+1)%4
    print('#',test_case, sep='')
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()