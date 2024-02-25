#a 98
import sys
l=sys.stdin.readline().rstrip()
x=[[0 for j in range(26)]for i in range(len(l))]
x[0][ord(l[0])-97]=1
n=int(input())
for i in range(1,len(l)):
    for j in range(26):
        x[i][j]=x[i-1][j]
    x[i][ord(l[i])-97]=x[i-1][ord(l[i])-97]+1
for i in range(n):
    a,m,o=sys.stdin.readline().split()
    m=int(m)
    o=int(o)
    if(m>0):
        print(x[o][ord(a)-97]-x[m-1][ord(a)-97])
    else:
        print(x[o][ord(a)-97])