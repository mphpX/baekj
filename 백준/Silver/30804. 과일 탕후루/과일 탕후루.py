n=int(input())
l=list(map(int,input().split()))
left=0
count=dict()
max_length=0
for right in range(n):
    count[l[right]]=count.get(l[right], 0) + 1 
    while(len(count)>2):
        count[l[left]]-=1
        if count[l[left]] == 0:
            del count[l[left]]
        left+=1
    max_length=max(max_length, right-left+1)
print(max_length)