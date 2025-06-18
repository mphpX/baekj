x=input().strip()
while(x!='0'):
    ans=1
    for i in x:
        if(i=='0'):
            ans+=4
        elif(i=='1'):
            ans+=2
        else:
            ans+=3
        ans+=1
    print(ans)
    x=input().strip()