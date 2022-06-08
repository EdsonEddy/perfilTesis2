import sys
def falta(tam,cad):
    s=0
    v=lee.split(" ")
    for i in range(tam-1):
        s=s+int(v[i])
    falta=int(((tam*(1+tam))/2))-s
    return falta

for n in sys.stdin:
    n=int(n)
    lee=input()
    print(falta(n,lee))
