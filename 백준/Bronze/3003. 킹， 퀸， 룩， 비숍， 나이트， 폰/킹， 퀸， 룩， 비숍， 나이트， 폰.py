#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
l=[1,1,2,2,2,8]
n=list(map(int,input().split()))
for i in range(len(n)):
  print(l[i]-n[i],end=' ')