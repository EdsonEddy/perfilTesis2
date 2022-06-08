def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

import sys
for linea in sys.stdin:
    a = int(linea)
    A=binarizar(a)
    q=A[::-1]
    w=int(q, 2)
    print(w)