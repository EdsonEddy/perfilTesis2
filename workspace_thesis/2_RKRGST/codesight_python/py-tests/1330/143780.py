cad=input()
num=int("".join([x for x in cad if x.isdigit()]))
cadena=("".join([x for x in cad if x.isalpha()]))
tam=len(cadena)
rotar=num%tam
a=cadena[(len(cadena)-rotar):]
b=cadena[:(len(cadena)-rotar)]
print(a+b)
