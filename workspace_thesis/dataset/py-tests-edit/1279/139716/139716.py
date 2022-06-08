while True:
    abc = 'abcdefghijklmnopqrstuvwxyz'
    alp = abc
    y = len(abc)
    x, word = input().split()
    x = int(x)
    res = ''
    while x > y:
        x -= y
    cod = abc[x:]
    abc = abc[:x]
    ofi = cod + abc
    for k in word:
        pl = alp.find(k)
        if k == '-':
            res += '-'
        elif k == ',':
            res += ','
        elif pl != -1:
            res += ofi[pl]
        else:
            res += ' '
    res = res.upper()
    print(res)