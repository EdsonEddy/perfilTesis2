a = int(input())
lista = []
while(a != 0):
    b = input()
    m = ''
    for i in range(len(b)):
        m = m + (b[len(b)-i-1]) 
    lista.insert(0, m)
    a = a - 1
for u in lista:
    print(u)
