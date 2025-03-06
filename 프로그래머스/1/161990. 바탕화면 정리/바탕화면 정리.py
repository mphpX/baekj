def solution(paper):
    x=len(paper[0])
    y=len(paper)
    ansx=[]
    ansy=[]
    for i in range(y):
        for j in range(x):
            if(paper[i][j]=='#'):
                ansx.append(i)
                ansy.append(j)
    ans=[min(ansx),min(ansy),max(ansx)+1,max(ansy)+1]
    return ans