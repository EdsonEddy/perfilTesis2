e=['dek','unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau' ]
while True:
    num=int(input())
    ld, lu =[],[]
    d, u= num//10,num%10
    if d==1:
        ld.append(e[0])
    elif d>1:
        ld.append(e[d])
        ld.append(e[0])
    lu.append(e[u])
    if u==0:
        print(*ld, sep='')
    elif d==0:
        print(*lu, sep= '')
    else:
        print(*ld, sep= '', end= ' ')
        print(*lu, sep= '')