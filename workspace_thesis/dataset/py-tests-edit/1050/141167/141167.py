def bin(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
def invertir(x):
    return x[::-1]
def nnatural(x):
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
    print(nnatural(y))