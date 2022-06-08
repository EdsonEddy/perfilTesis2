import sys
for linea in sys.stdin:
    a=int(linea)
    c=bin(a)
    v=len(c)
    v=v-2
    print(v)