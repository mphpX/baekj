import sys
l=[]
for i in range(8):
    x=sys.stdin.readline().strip()
    l.append(x)
ct=0
for i in range(8):
    for j in range(8):
        if(i%2==0 and j%2==0 and l[i][j]=='F'):
            ct+=1
        elif(i%2!=0 and j%2!=0 and l[i][j]=='F'):
            ct+=1
print(ct)