a=input()
b=input()
fl=[[0 for i in range(len(b)+1)]for j in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if(a[i-1]==b[j-1]):
            fl[i][j]=fl[i-1][j-1]+1
        else:
            fl[i][j]=max(fl[i-1][j],fl[i][j-1])
print(fl[len(a)][len(b)])