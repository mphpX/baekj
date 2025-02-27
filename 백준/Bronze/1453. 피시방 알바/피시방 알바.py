n=int(input())
l=list(map(int,input().split()))
seat=[0 for i in range(101)]
ct=0
for i in l:
    if(seat[i]==0):
        seat[i]=1
    else:
        ct+=1
print(ct)