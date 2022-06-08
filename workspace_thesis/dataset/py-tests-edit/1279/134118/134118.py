k,cad=map(str,input().split())
vol="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while k!="" \
         "":
    cadena = ""
    for i in cad:
        p = vol.find(i.upper())
        if p == -1:
            if i == "_":
                cadena = cadena + " "
            else:
                cadena = cadena + i
        elif p + 1 + int(k) > 26:
            cadena = cadena + vol[((int(k) + p + 1) % 26) - 1]
        else:
            cadena = cadena + vol[int(k) + (p + 1) - 1]
    print(cadena)
    k, cad = map(str, input().split())

