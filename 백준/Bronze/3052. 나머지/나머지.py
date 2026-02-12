num_list=[]
for i in range(10):
    num_list.append(int(input()))
# print(num_list)

left_list=[]
for j in num_list:
    left_list.append(j % 42)
print(len(list(set(left_list))))