import math
def epicentro(w):
    cd=int(math.log10(w))+1
    de=(cd//2)+1
    contd=0
    while contd != de:
        d=w%10
        w=w//10
        contd+=1
    return(d)

n=int(input())
cd=int(math.log10(n))+1
if cd%2 != 0:
    d=epicentro(n)
    print(d)
else:
    print("*")