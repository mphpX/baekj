import sys
ch=input()
sum=0
arr=[]
for i in range(26):
    arr.append(-1)
for i in range(len(ch)):
    if(arr[ord(ch[i])-97]==-1):
        arr[ord(ch[i])-97]=i
for i in range(26):
    print(arr[i],end=" ")