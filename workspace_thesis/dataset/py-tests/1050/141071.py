def BinarioAdecimal(x):
    x=str(x)
    longitud=len(x)
    binario=0
    exponente=0
    for i in range(longitud-1,-1,-1):
        if x[i]=='1':
            binario=binario+1*2**exponente
            exponente+=1
        else:
            binario=binario
            exponente+=1
    return binario

def decimalAbinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
while True:
    try:
        x = decimalAbinario(int(input()))
        desAbin=str(x)
        invertido=desAbin[::-1]
        nuevonumero=BinarioAdecimal(invertido)
        print(nuevonumero)
    except ValueError:
        break