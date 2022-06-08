from sys import stdin
for line in stdin:
    dato = line.split()
    d = int(dato[0])
    m = int(dato[d+1])
    c = 0
    i = 1
    if d > 1:
        i = 1 if int(dato[1]) > int(dato[2]) else d
    while i <= d and i > 0:
        c += (m // int(dato[i]))
        m %= int(dato[i])
        i = i + 1 if int(dato[1]) > int(dato[2]) else i - 1
    if m == 0:
        print(c)
    else:
        print(-1)