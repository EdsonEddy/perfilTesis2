lista = []
a1, b1, a2, b2 = map(int, input().split())
if(b1 < a2):
    print("[]")
else:
    m = "["
    n = "]"
    o = ","
    lista = [a1, b1, a2, b2]
    lista.sort()
    x = str(lista[1])
    y = str(lista[2])
    print(m + x + o + y + n)