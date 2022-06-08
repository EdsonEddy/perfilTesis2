from sys import stdin
for line in stdin:
    l = len(line)
    n = int(line)
    sP = sI = 1
    for i in range(l):
        if i % 2 == 0:
            sP += n % 10
        else:
            sI += n % 10
        n //= 10
    if sP == sI:
        print('SI')
    else:
        print('NO')
