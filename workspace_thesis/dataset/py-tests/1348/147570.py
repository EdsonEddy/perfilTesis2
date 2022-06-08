while True:
    n=int(input())
    d='dek'
    L=[]
    l=['unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau','dek','dek unu','dek du','dek tri','dek kvar','dek Kvin','dek ses','dek Sep','dek OK','dek Nau']
    for i in range(1,10):
        r=l[i]+d
        l.append(r)
        for y in range(9):
            l.append(r+" "+l[y])
    print(l[n-1])