from collections import deque
n,k=map(int,input().split())
dur=list(map(int,input().split()))
st=0
end=n-1
level=0
robot=deque([])
visit=[False for _ in range(2*n)]
#내구도 0인 칸이 k개?
check=0
for i in dur:
    if(i==0):
        check+=1
#----------------
while(check<k):
    level+=1
    end=(end-1 + n*2)%(2*n)
    st=(st-1+ n*2)%(2*n)
    #컨베이어 벨트 이동으로 First로 들어온 위치가 end와 같다면, pop.    
    if(len(robot)>0 and robot[-1]==end):
        robot.pop()
    #Second로 들어온 위치의 로봇이 이동했을때, 그 위치가 end와 같다면, pop.
    l=len(robot)
    #나머지 연산
    for i in range(l-1,-1,-1):
        if(i==len(robot)-1):
            next=(robot[i]+1)%(2*n)
            if(dur[next]>=1):
                robot[i]=next
                dur[next]-=1
                if(robot[i]==end):
                    robot.pop()
        else:
            next=(robot[i]+1)%(2*n)
            if(robot[i+1]!=next and dur[next]>=1):
                robot[i]=next
                dur[next]-=1
    if(dur[st]>0):
        robot.appendleft(st)
        dur[st]-=1
    check=0
    for i in dur:
        if(i==0):
            check+=1
print(level)
    