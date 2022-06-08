from sys import stdin
for line in stdin:
    a = ''
    n, cad = line.split()
    k = int(n) % 26
    for i in range(len(cad)):
        if 97 <= ord(cad[i]) <= 122:
            if ord(cad[i]) - 32 + k <= 90:
                a = a + chr(ord(cad[i]) - 32 + k)
            else:
                a = a + chr(64 + (ord(cad[i]) - 32 + k - 90))
        elif cad[i] == '_':
            a = a + ' '
        else:
            a = a + cad[i]
    print(a)