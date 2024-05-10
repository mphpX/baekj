import sys
l=list(sys.stdin.readline().strip())
n=len(l)
ans=[]
for i in range(1,n-1):
    for j in range(i+1,n):
        a=l[:i]
        b=l[i:j]
        c=l[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append(a+b+c)
ans.sort()
for i in ans[0]:
    print(i,end='')