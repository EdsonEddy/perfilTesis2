while True:
    valor=int(input())
    num={1:"unu",2:"du",3:"tri",4:"kvar",5:"Kvin",6:"ses",7:"Sep",8:"OK",9:"Nau",10:"dek"}
    if valor <10:
        numero=num.pop(valor)
        print(numero)
    elif valor>10:
        decena=valor//10
        unidad=valor%10
        if unidad==0 and decena!=1:
            print(num.get(decena)+num.get(10))
        elif decena>=2:
            decena1=num.get(decena)+num.get(10)
            print(decena1+" "+num.get(unidad))
        else:
            print(num.get(10)+" "+num.get(unidad))
    else:
        print(num.get(10))