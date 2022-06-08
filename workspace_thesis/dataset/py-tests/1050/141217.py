def bin(D):
    binario = ''
    while D // 2 != 0:
        binario = str(D % 2) + binario
        D = D // 2
    return str(D) + binario
def invertir(x):
    return x[::-1]
def N(x):
    nn=0
    for i in range(len(x)):
        if int(x[i])==0:
            nn=nn
        else:
            nn=int(x[i])*2**(len(x)-(i+1))+nn
    return nn
while True:
    x=int(input())
    y=invertir(bin(x))
    print(N(y))