while 1>0:
    lsn = ['','unu', 'du', 'tri', 'kvar', 'Kvin', 'ses', 'Sep', 'OK', 'Nau', 'dek']
    num = int(input())
    #num = 95
    nuDigit= str(num)
    if num < 11:
        print(lsn[num])
    if num >=11 and num<20:
        decena = nuDigit[0]#primer digito
        unidad = nuDigit[1]#seg digito
        print("dek " + lsn[int(unidad)])
    elif num >=20:
        decena = nuDigit[0]
        unidad = nuDigit[1]
        if int(unidad) == 0:
            print(lsn[int(decena)]+"dek")
        else:
            print(lsn[int(decena)]+"dek",lsn[int(unidad)])