def mi_func (cad):
    cad = cad + " "
    suma = ""
    lista = []
    for var in cad:
        if not var == " ":
            suma = suma + var
        else:
            lista.append(int(suma))
            suma=""
    return lista

cad = input()
s = 0
for var in mi_func(cad):
    s = s + var
print(s)