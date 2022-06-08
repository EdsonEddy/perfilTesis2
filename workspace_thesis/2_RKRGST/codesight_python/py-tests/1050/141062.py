def bina(decimal):
    binario=''
    while decimal//2 !=0:
        binario,decimal=(str(decimal % 2)+ binario),(decimal//2)
    return str(decimal) + binario
def aDe(nBin):
    nBin,decimal,exp=(str(nBin)),0,(len (nBin)-1)
    for i in nBin:
        decimal += (int(i)*2**(exp))
        exp=exp-1
    return decimal
while True:
    a=int(input())
    b=bina(a)
    d=str(b)[::-1]
    c=aDe(d)
    print(c)