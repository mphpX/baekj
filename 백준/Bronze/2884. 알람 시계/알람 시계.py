a,b=map(int,input().split())
sum=a*60+b-45
if(sum<0):sum+=60*24
print("%d %d"%(sum//60,sum%60))
