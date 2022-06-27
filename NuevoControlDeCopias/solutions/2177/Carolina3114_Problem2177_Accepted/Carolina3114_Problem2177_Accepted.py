def generador(numero,contador):
    dig = 0
    nuevodig = contador
    
    while contador>0:
        dig = dig+(numero%10)
        numero = numero//10
        contador = contador-1
    if dig > 9:
            dig = generador(dig,nuevodig)
    return dig

for i in range(int(input())):
    numero,digitos = map(int,input().split())
    resultado = 0
    contador = 0
    if(numero < pow(10,digitos)):
        print('')
        continue
    while numero >= pow(10,digitos-1):
        auxiliar = generador(numero,digitos)
        resultado = (auxiliar * pow(10,contador))+ resultado
        contador = contador + 1
        numero = numero // 10
    print(resultado)
