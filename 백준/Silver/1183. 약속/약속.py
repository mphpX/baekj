n=int(input())
diff=[0 for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    diff[i]=a-b
diff.sort()
if(n%2==0):
    print(diff[n//2]-diff[n//2-1]+1)
else:
    print(1)