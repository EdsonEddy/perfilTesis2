while True:
    entre1a10 = ['','Ara', 'da', 'tra', 'pra','Hra', 'Sea','Xea', 'gua', 'noa', 'Dea']
    dec = ['Dea']
    numero = input()
    lon  = len(numero)
    if lon == 4:
        print('Do '+entre1a10[int(numero[0])],end='')
        if int(numero[1])!=0:
            print(' '+entre1a10[int(numero[1])]+'es',end='')
        if int(numero[2])!=0:
            print(' '+int(numero[2]) * 'Dea', end='')
        if int(numero[3])!=0:
            print(' '+entre1a10[int(numero[3])],end='')
        print()
    elif lon == 3:
        print(entre1a10[int(numero[0])]+'es',end='')
        if int(numero[1])!=0:
            print(' '+int(numero[1]) * 'Dea', end='')
        if int(numero[2])!=0:
            print(' '+entre1a10[int(numero[2])], end='')
        print()
    elif lon == 2:
        print(int(numero[0])*'Dea',end='')
        if int(numero[1])!=0:
            print(' '+entre1a10[int(numero[1])], end='')
        print()
    elif lon == 1:
        if numero != '0':
            print(entre1a10[int(numero)])

