n=int(input())
vertical=[False for _ in range(n)]
left_c=[False for _ in range(2*n-1)]
right_c=[False for _ in range(2*n-1)]
ans=0
def back_track(row):
    if(row==n):
        global ans
        ans+=1
        return
    for j in range(n):
        if(vertical[j]==False and right_c[row+j]==False and left_c[row-j+n-1]==False):
                vertical[j]=True
                right_c[row+j]=True
                left_c[row-j+n-1]=True
                back_track(row+1)
                vertical[j]=False
                right_c[row+j]=False
                left_c[row-j+n-1]=False
back_track(0)
print(ans)