def autom(aux1,cont):
    c = cont
    digito = 0
    while cont > 0:
        digito = digito + (aux1 % 10)
        aux1 = aux1 // 10
        cont = cont - 1
    if digito > 9:
            digito = autom(digito,c)
    return digito

for i in range(int(input())):
    num,cant = map(int,input().split())
    neonum = 0
    x = 0
    if(num < pow(10,cant)):
        print('')
        continue
    while num >= pow(10,cant-1):
        aux2 = autom(num,cant)
        neonum = (aux2 * pow(10,x))+ neonum
        x = x + 1
        num = num // 10
    print(neonum)
    
