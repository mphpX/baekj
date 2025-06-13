n, add_grade, p=map(int,input().split())
if(n==0):
    print(1)
else:
    grade= list(map(int,input().split()))
    ans=1
    ct=0
    for i in grade:
        if(add_grade<=i):
            ct+=1
            if(add_grade<i):
                ans+=1
    if(ct==p):
        print(-1)
    else:
        print(ans)