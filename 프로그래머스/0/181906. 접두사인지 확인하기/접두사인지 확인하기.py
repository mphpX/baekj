def solution(my_string, is_prefix):
    ls=len(is_prefix)
    if(my_string[:ls]==is_prefix):
        return 1
    else:
        return 0