import sys
lista = ['unu', 'du', 'tri', 'kvar', 'Kvin', 'ses', 'Sep', 'OK', 'Nau']
lis = ['dek', 'dudek', 'tridek', 'kvardek', 'Kvindek', 'sesdek', 'Sepdek', 'OKdek', 'Naudek']
for line in sys.stdin:
    a = int(line)
    b = a
    if(a < 10):
        print(lista[a - 1])
    else:
        while(a != 0):
            dig = a % 10
            if(dig == 0):
                x = str(a)
                x = (x.rstrip("0"))
                x = int(x)
                x = (lis[x - 1])
                break
            else:
                if(a == b):
                    m = lista[dig - 1]
                else:
                    n = lis[dig - 1]
            a = a // 10
        if(a == b):
            print(x)
        else:
            print(n, m)