n = int(input())
for i in range(n):
    na = int(input())
    s = ''
    while na > 0:
        dig = na % 10
        if dig != 1 and dig != 0:
            for x in range(2, dig):
                if dig % x == 0:
                    break
            else:
                s = str(dig) + s
        na = na//10
    if s == '':
        print('0')
    else:
        print(s)