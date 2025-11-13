def solution(n, bans):
    answer = []
    matter=[]
    for ban in bans:
        index=0
        factor=1
        for j in range(len(ban)-1,-1,-1):
            index+= (ord(ban[j])-ord('a')+1)*factor
            factor*=26
        matter.append(index)
    matter.sort()
    for idx in matter:
        if(idx <= n):
            n+=1
        else:
            break
    while(n):
        r= n % 26
        if(r==0):
            answer.append('z')
            n=n//26-1
        else:
            answer.append(chr(96+r))
            n=n//26
    
    return ''.join(reversed(answer))