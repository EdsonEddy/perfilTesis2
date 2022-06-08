esp = ['dek','unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau']
while True:
    num = int(input())
    ld, lu = [],[]
    dec,u = num//10, num%10
    if dec==1:
        ld.append(esp[0])
    elif dec>1:
        ld.append(esp[dec])
        ld.append(esp[0])
    lu.append(esp[u])
    if u==0:
        print(*ld, sep='')
    elif dec==0:
        print(*lu, sep='')
    else:
        print(*ld, sep='', end=' ')
        print(*lu, sep='')