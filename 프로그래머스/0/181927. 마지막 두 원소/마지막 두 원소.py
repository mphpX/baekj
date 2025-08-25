def solution(num_list):
    z= num_list[len(num_list)-1]
    y= num_list[len(num_list)-2]
    if(z>y): 
        num_list.append(z-y)
    else:
        num_list.append(z*2)
    return num_list