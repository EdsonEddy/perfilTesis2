Cadena=input()
sa=""
for i in range(len(Cadena)):
    resultado=str(bin(ord(Cadena[i])))
    resultado=resultado[2:]
    resultado=resultado.zfill(8)
    sa=sa+resultado
print(sa)