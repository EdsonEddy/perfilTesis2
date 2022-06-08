n = int(input())
A = 'ABC'
E = 'BABC'
G = 'CCAABB'
a = e = g = 0
cad = input()
for i in range(n):
    if cad[i] == A[i%3]:
        a += 1
    if cad[i] == E[i%4]:
        e += 1
    if cad[i] == G[i%6]:
        g += 1
if a > e and a > g:
    print(a)
    print('Alvaro')
elif e > a and e > g:
    print(e)
    print('Edwin')
elif g > a and g > e:
    print(g)
    print('Gabriel')
elif a > g and a == e:
    print(a)
    print('Alvaro')
    print('Edwin')
elif a > e and a == g:
    print(a)
    print('Alvaro')
    print('Gabriel')
elif e > a and e == g:
    print(e)
    print('Edwin')
    print('Gabriel')
elif a == e and a == g:
    print(a)
    print('Alvaro')
    print('Edwin')
    print('Gabriel')
