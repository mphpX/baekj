import math
mn,mx=map(int,input().split())
limit = int(math.sqrt(mx))
is_prime = [True] * (limit + 1)
primes = []
is_ss=[True]*(mx-mn+1)

for i in range(2, limit + 1):
    if is_prime[i]:  # 소수라면
        primes.append(i * i)  # 소수의 제곱 저장
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False  # 배수 제거

for i in primes:
    st=max(i,(mn+i-1)//i*i)
    for j in range(st,mx+1,i):
        if(j-mn>=0):
            is_ss[j-mn]=False

print(is_ss.count(True))