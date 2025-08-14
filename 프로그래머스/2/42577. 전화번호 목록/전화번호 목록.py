def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        pre= phone_book[i]
        word= phone_book[i+1]
        if(pre== word[:len(pre)]):
            return False
    return True