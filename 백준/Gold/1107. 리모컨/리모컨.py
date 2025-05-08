import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n=int(input())
m=int(input())
length= len(str(n))
yes=[0,1,2,3,4,5,6,7,8,9]
no=list(map(int,input().split()))
yes=list(set(yes)-set(no))
track=[700000 for _ in range(1000001)]
if(0 in yes):
    track[0]=1
def backtracking(test,l):
    if(len(test)==l):
        index=0
        for i in range(len(test)):
            index=10*index+test[i]
        if(0<=index<1000001):
            track[index]=l
        return
    for i in range(len(yes)):
        if(len(test)==0 and yes[i]==0):
            continue
        test.append(yes[i])
        backtracking(test,l)
        test.pop()
if((length-1)!=0):
    backtracking([],length-1)
backtracking([],length)
backtracking([],length+1)
low_target=n
high_target=n
while(track[low_target]==700000 and low_target>0):
    low_target-=1   
while(track[high_target]==700000 and high_target<1000000):
    high_target+=1     
raw=n-100
if(raw<0):
    raw=-raw
print(min(high_target-n+track[high_target],n-low_target+track[low_target],raw))