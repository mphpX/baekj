def solution(people, limit):
    n=len(people)
    people.sort()
    left=0
    right = n-1
    ct=0
    while(left<right and n>0):
        if(people[left]+people[right]>limit):
            right-=1
            ct+=1
            n-=1
        else:
            ct+=1
            n-=2
            left+=1
            right-=1
            
    return n+ct