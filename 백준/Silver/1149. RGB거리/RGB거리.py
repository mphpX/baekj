import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
cur_r,cur_g,cur_b=graph[0][0],graph[0][1],graph[0][2]
for i in range(1,n):
    next_r=min(cur_g,cur_b)+graph[i][0]
    next_g=min(cur_r,cur_b)+graph[i][1]
    next_b=min(cur_r,cur_g)+graph[i][2]
    cur_r,cur_g,cur_b=next_r,next_g,next_b
print(min(next_r,next_g,next_b))