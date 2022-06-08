import math
n = int(input())
for i in range(n):
    x=int(input())
    cd=int(math.log10(x))+1
    aux=0
    y=0
    while x!=0:
        d=int(x/(10**(cd-1)))
        x=x%(10**(cd-1))
        cd=cd-1
        y=aux*10+d
        if y==96:
            print("APLAZADO!")
            break
        else:
            aux=d
    if y != 96:
        print("TE SALVAS :D")