import sys
def pal( k ):
    aux = 0
    while(k > 0):
        aux = 10*aux + (k % 10)
        k = k // 10
    return aux
for n in sys.stdin:
    n = int(n)
    cd = 0
    for i in range(n):
        x = int(input())
        a = pal(x)
        if( a == x ):
            cd = cd + 1
    print(cd)
