import sys
input=sys.stdin.readline
t=int(input())
nums=[1,1,1,2,2,3]
for i in range(6,100):
    nums.append(nums[i-1]+nums[i-5])
for i in range(t):
    n=int(input())
    print(nums[n-1])