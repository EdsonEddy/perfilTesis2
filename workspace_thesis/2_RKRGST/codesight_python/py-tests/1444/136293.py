def decimalAbinario(decimal):
    contador=0
    x = decimal
    binario = ''
    sw = False
    for i in range(31, -1, -1):
        if x & (1 << i) > 0:
            binario = binario + '1'
            sw = True
        else:
            if sw == True:
                binario = binario + '0'
    return binario
def NumeroDePares(h):
    lon=len(h)
    par = int(0)
    cont=0
    for digitos in range(lon):
        if nuevo[digitos] == '1':
            cont = cont + 1
            if cont == 2:
                par = par+1
                cont = 0
        else:
            cont = 0
    return par

n=int(input())
for casos in range (n):
    numero=(int(input()))
    nuevo=decimalAbinario(numero)
    numerodepares=NumeroDePares(nuevo)
    print(numerodepares)
