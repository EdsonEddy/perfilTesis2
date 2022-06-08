def anti_vocal(texto):
    r=len(texto)
    cnt=0
    cadena=""
    while cnt < r:
        if texto[cnt] not in "aeiouyAEIOUY":
            cadena=cadena+"."+texto[cnt]
        cnt+=1
    return cadena

cad=input()
ncad=anti_vocal(cad)

print (ncad.lower())