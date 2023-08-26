a,b=map(int,input().split())
c=int(input())
sum=a*60+b+c
if(sum>=60*24):sum-=60*24
print("%d %d"%(sum//60,sum%60))