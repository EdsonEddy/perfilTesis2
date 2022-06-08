import sys
for n in sys.stdin:
    x = int(n)
    sp = 0
    si = 0
    for j in range(len(n)):
        dig = x % 10
        if j % 2 == 0:
            sp = sp + dig
        else:
            si = si + dig
        x = x // 10
    if sp == si:
        print('SI')
    else:
        print('NO')
