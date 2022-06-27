n = int(input())
for i in range(0, n, 1):
    p = '*'
    if i == n-1:
        print('{:^7}'.format(p))
    else:
        print('{:^7}'.format(p), end='')
for i in range(0, n, 1):
    s = ' /#\ '
    if i == n-1:
        print('{:^7}'.format(s))
    else:
        print('{:^7}'.format(s), end='')
for i in range(0, n, 1):
    t = ' /###\ '
    if i == n-1:
        print('{:^7}'.format(t))
    else:
        print('{:^7}'.format(t), end='')
for i in range(0, n, 1):
    c = '___#___'
    print(c, end='')
