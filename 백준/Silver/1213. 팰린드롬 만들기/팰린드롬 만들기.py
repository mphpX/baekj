import sys
l=sys.stdin.readline().strip()
d=[0 for _ in range(26)]
result=[]
x=[]
for i in l:
    d[ord(i)-65]+=1
for i in range(26):
    for j in range(d[i]//2):
        result.append(chr(i+65))
    if(d[i]%2==1):
        x.append(chr(i+65))
if(len(x)<=1):
    for i in result:
        print(i,end='')
    for i in x:
        print(i,end='')
    for i in result[::-1]:
        print(i,end='')
else:
    print("I'm Sorry Hansoo")