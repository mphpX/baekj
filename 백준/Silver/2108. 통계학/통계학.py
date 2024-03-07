import sys
n=int(sys.stdin.readline())
l=[]
for i in range(n):
    a=int(sys.stdin.readline())
    l.append(a)
l.sort()
print(round(sum(l)/n))
print(l[n//2])
dic=dict()
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
m=max(dic.values())
dicl=[]
for i in dic:
    if m==dic[i]:
        dicl.append(i)
if len(dicl)>1:
    print(dicl[1])
else:
    print(dicl[0])
print(l[n-1]-l[0])