while True:
    if int(input()) == 0:
        break
    lista = input().split()
    lista.sort()
    o = ''
    for i in range(len(lista)-1, -1, -1):
        o = o + lista[i]
    print(o)