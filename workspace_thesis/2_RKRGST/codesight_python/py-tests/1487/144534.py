import math

def prim(n):
    if n < 2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if (n % i == 0):
            return False
    return  True
while True:
    a = int(input())
    if prim(a):
        print('ES PRIMO')
    else:
        print('NO ES PRIMO')