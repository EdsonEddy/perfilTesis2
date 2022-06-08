# 1533: Impares y pares
# Jhonny

import sys

for linea in sys.stdin:

    if linea == "\n":
        break

    n, k = map(int, linea.split())
    
    m = n // 2
    if n % 2 == 1:
        m = m + 1

    if k <= m:
        print(1 + (k-1) * 2)
    else:
        print((k-m) * 2)