a=int(input())
arr=[90,80,70,60,60,0]
ch='A'
i=0
while(a<arr[i]):
    ch = chr(ord(ch) + 1)
    i+=1
print(ch)