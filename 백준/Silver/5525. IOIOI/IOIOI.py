n=int(input())
m=int(input())
s=list(input())
l=[]
for i in range(len(s)):
    if(s[i]=='I'):
        l.append(i)
idx=0
ct=0
ans=[]
for i in range(idx,len(l)-1):
    if(l[i+1]-l[i]==2):
        ct+=1
        if(i==len(l)-2):
            ans.append(ct)
    else:
        ans.append(ct)
        ct=0
answer=0
for i in ans:
    if(i>=n):
        answer+=i-n+1
print(answer)