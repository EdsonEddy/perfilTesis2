import math
n = int(input())
while n!="" \
         "":
    cad = ()
    for i in range(int(math.sqrt(n))):
        if (n % (i + 1)) == 0:
            c = n // (i + 1)
            p = len(cad) // 2
            cad = cad[:p] + ((i + 1),) + (c,) + cad[p:]
    s, j = "", 0
    for i in cad:

        if j != i:
            s = s + str(i) + " "
        j = i
    print("Divisores de",(str(n)+":"),s[:len(s) - 1])
    n = int(input())