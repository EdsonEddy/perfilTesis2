while 1>0:
    x=int(input())
    v=['unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau']
    vd=['dek','dudek','tridek','kvardek','Kvindek','sesdek','Sepdek','OKdek','Naudek']
    if x<=9:
        print(v[x-1])
    else:
        if x%10==0:
            d=x//10
            print(vd[d-1])
        else:
            d=x//10
            d2=x%10
            print(vd[d-1],v[d2-1])