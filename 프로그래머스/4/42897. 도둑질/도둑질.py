def solution(money):
    n=len(money)
    oans=[0 for _ in range(n)]
    oans[0]=money[0]
    oans[2]=money[0]+money[2]
    oans[3]=money[0]+money[3]
    xans=[0 for _ in range(n)]
    xans[1]=money[1]
    xans[2]=money[2]
    xans[3]=money[1]+money[3]
    for i in range(4,n-1):
        oans[i]=max(oans[i-2], oans[i-3])+money[i]
    for i in range(4,n):
        xans[i]=max(xans[i-2], xans[i-3])+money[i]
    return max(max(xans),max(oans))