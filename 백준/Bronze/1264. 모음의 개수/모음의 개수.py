l=input()
while(l[0]!='#' or len(l)!=1):
    s=l.count('a')+l.count('e')+l.count('i')+l.count('o')+l.count('u')+l.count('A')+l.count('E')+l.count('I')+l.count('O')+l.count('U')
    print(s)
    l=input()