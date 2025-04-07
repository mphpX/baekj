import sys
input=sys.stdin.readline
n=int(input())
cur_r,cur_g,cur_b = map(int,input().split())
for i in range(1,n):
    r,g,b=map(int,input().split())
    next_r=min(cur_g,cur_b)+r
    next_g=min(cur_r,cur_b)+g
    next_b=min(cur_r,cur_g)+b
    cur_r,cur_g,cur_b=next_r,next_g,next_b
print(min(next_r,next_g,next_b))