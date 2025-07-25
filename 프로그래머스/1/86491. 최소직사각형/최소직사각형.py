def solution(sizes):
    w=0
    h=0
    for size in sizes:
        cur_w=size[0]
        cur_h=size[1]
        w=max(max(cur_w,cur_h),w)
        h=max(min(cur_w,cur_h),h)
        
    return w*h