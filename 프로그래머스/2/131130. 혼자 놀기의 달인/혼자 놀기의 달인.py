def solution(cards):
    ln=len(cards)
    box=[0 for i in range(ln)]
    ans=[]
    for i in range(ln):
        if(box[i]==0):
            ct=1
            box[i]=1
            j=cards[i]-1
            while(box[j]==0):
                box[j]=1
                ct+=1
                j=cards[j]-1
            ans.append(ct)
    if(len(ans)==1):
        return 0
    else:
        ans.sort(reverse=True)
        return ans[0]*ans[1]