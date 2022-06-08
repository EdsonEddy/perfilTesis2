from sys import stdin
for i in stdin:
    n = int(i)
    s = 0
    b = ''
    while n > 0:
        if n % 2 == 0:
            b = b + '0'
        else:
            b = b + '1'
        n = n // 2
    a = len(b)
    for j in range(len(b)):
        if b[a - 1] == '1':
            s = s + (2 ** j)
            a = a - 1
        else:
            a = a - 1
    print(s)
