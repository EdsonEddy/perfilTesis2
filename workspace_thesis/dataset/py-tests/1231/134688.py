a, b, c = map(int,input().split())
if a < 24 and b < 60 and c < 60:
    c += 1
    if c >= 60:
        c = c % 10
        b += 1
        if b >=60:
            b = b % 10
            a +=1
    if c == 0:
        c = '00'
    if b == 00:
        b = '00'
    if a == 0 or a == 24:
        a = '00'
    print(str(a)+':'+str(b)+':'+str(c))