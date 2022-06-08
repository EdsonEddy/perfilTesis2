def conv(x):
    m = ord(x)
    n = bin(m)
    return n


def roll(m):
    r = m[2:]
    if len(r) == 8:
        return r
    else:
        r1 = ''
        z = 8 - len(r)
        for j in range(z):
            r1 = r1 + '0'
        r2 = r1 + r
        return r2


# Principal
cad = input()
s = ''
for i in range(len(cad)):
    m = conv(cad[i])
    f = roll(m)
    s = s + str(f)
print(s)
