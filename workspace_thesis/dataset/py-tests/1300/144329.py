import sys
for l in sys.stdin:
    nlia = int(l)
    a = list(input().split())
    cont = 0
    udig= ''.join(a[len(a)-1:])
    for i in range(len(a)):
            if a[i] == udig :
                cont = cont + 1
    print(cont)
