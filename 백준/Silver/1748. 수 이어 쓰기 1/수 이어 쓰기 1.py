n=int(input())
ms=10
ct=9
num=1
ans=0
# 1~9 9개
# 10~99 90개 *2
# 100~999 900개 *3
# 1000~9999 9000개 *4
while(ms<=n):
    ans+=ct*num
    num+=1
    ct*=10
    ms*=10
ans+=(n-ms//10+1)*num
print(ans)