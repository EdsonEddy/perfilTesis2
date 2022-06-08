import sys
def esPrimo(n):
    if n==1: return 0
    if n==2: return 1
    i=3
    while i*i<=n:
        if n%i==0: return 0
        i+=2
    return n%2


for line in sys.stdin:
    print('ES PRIMO' if esPrimo(int(line))==1 else 'NO ES PRIMO')
